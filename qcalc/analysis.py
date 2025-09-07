from __future__ import print_function


from .inout import IO
from .qcalc import Qcalc
from .utils import Utils
from pathlib import Path
from numpy.linalg import norm
from shutil import copy2


class Analysis(Qcalc):

    def __init__(
        self,
        path=Path.cwd(),
        get_relaxation=True,
        get_convergence=True,
        get_geometry=True,
        get_homo=True,
        get_lumo=True,
        get_mag=True,
        get_energy=True,
        get_change_energy=True,
        console=False,
        singlepoint=False,
        table_energy=True
    ):
        super(Analysis, self).__init__(path, console=console)
        self._module = "analysis"
        self.io = IO()
        self.io.update(self)
        self.utils = Utils()
        self.utils.update(self)
        self.get_relaxation = get_relaxation
        self.get_convergence = get_convergence
        self.get_geometry = get_geometry
        self.get_homo = get_homo
        self.get_lumo = get_lumo
        self.get_mag = get_mag
        self.get_energy = get_energy
        self.get_change_energy = get_change_energy
        self.get_properties = (self.get_homo or self.get_lumo or self.get_mag or \
                               self.get_energy or self.get_change_energy)
        self.singlepoint = singlepoint 
        self.table_energy = table_energy

    def update(self, qcalc_obj):
        self.__dict__.update(qcalc_obj.__dict__)

    def relaxation_info(self, aims_file, line):
        """
        Function based on the 'get_relaxation_info' script.

        Parameters
        ----------
        aims_file: file object
            The aims.out file object.
        line: file object
            The current file position.
        """

        # Checking optimizer
        if "Geometry relaxation: Textbook BFGS" in line:
            self.relaxation["opt"] = 1
        elif "Geometry relaxation: Modified BFGS - TRM" in line:
            self.relaxation["opt"] = 2
        # Read energies
        elif "| Total energy uncorrected" in line:
            self.relaxation["energy"] = float(line.split()[5])
            # Go to the next line
            next(aims_file)
            self.relaxation["free_energy"] = float(next(aims_file).split()[5])

            if self.relaxation["1st_energy"] is None:
                self.relaxation["1st_energy"] = self.relaxation["energy"]
                self.relaxation["1st_free_energy"] = self.relaxation["free_energy"]
        # Read forces
        elif "Maximum force component is" in line:
            self.relaxation["max_force"] = float(line.split()[4])
            self.relaxation["n_rel"] += 1
        # Main check
        elif "Advancing" in line:

            msg = "{:5d}   {:16.8f} {:14.6f}   {:16.8f} {:14.6f} {:10.6f} ".format(
                self.relaxation["n_rel"],
                self.relaxation["energy"],
                1000*(self.relaxation["energy"] - self.relaxation["1st_energy"]),
                self.relaxation["free_energy"],
                1000*(self.relaxation["free_energy"] - self.relaxation["1st_free_energy"]),
                self.relaxation["max_force"],
            )

            # Check rejection
            # Optimizer: BFGS
            if self.relaxation["opt"] == 1:
                next(aims_file)
                next(aims_file)
                if next(aims_file).split()[0] not in ["Predicted", "x"]:
                    return msg + " rejected. \n"
            # Optimizer: TRM
            elif self.relaxation["opt"] == 2:
                for _ in range(10):
                    try:
                        aux = next(aims_file)
                    except StopIteration:  # if (!$_) {last;}
                        break
                    if "| Contraproductive step" in aux:
                        return msg + " rejected. \n"
                    elif "**" in aux:
                        return msg + " rejected: force <-> energy inconsistency? \n"
                    # This should only happen for BFGS->TRM switch
                    elif "Optimizer is stuck" in aux:
                        return msg + " stuck. \n"
                    elif "Updated atomic structure:":
                        break
                return msg + "\n"

        elif "Present geometry is converged." in line:
            return "{:5d}   {:16.8f} {:14.6f}   {:16.8f} {:14.6f} {:10.6f} converged. \n".format(
                self.relaxation["n_rel"],
                self.relaxation["energy"],
                1000*(self.relaxation["energy"] - self.relaxation["1st_energy"]),
                self.relaxation["free_energy"],
                1000*(self.relaxation["free_energy"] - self.relaxation["1st_free_energy"]),
                self.relaxation["max_force"],
            )
        return ""

    def convergence_info(self, line):
        """
        Function based on the 'grep_convergence' script.

        Parameters
        ----------
        line: file object
            The current file position.
        """

        if "Self-consistency cycle converged" in line:
            self.convergence["now"] = 1

        if self.convergence["now"] and "iteration" in line:
            self.convergence["n_SCF"] = int(line.split()[4])
            self.convergence["iter"] += 1
            self.convergence["now"] = 0
            return "{:8d} {:8d} \n".format(self.convergence["iter"], self.convergence["n_SCF"])
        return ""

    def geometry_info(self, aims_file, line):
        """
        Function based on the 'create_geometry_zip' script.

        Parameters
        ----------
        aims_file: file object
            The aims.out file object.
        line: file object
            The current file position.
        """

        def read_atoms(aims_file):
            atoms = []
            for _ in range(self.geometry["n_atoms"]):
                aux = next(aims_file)
                if "velocity" in aux:
                    aux = next(aims_file)
                    if "atom" not in aux:
                        continue
                aux = aux.split()
                # Saving in XYZ format
                if self.geometry["n_iter"] == 0:
                    atoms.append([aux[3], aux[4], aux[5], aux[6]])
                else:
                    atoms.append([aux[4], aux[1], aux[2], aux[3]])
            self.geometry["n_iter"] += 1
            return atoms

        def write_geometry(atoms, lattice_vector):
            file_name = self.utils.path / \
                "geometry-{:06d}.in".format(self.geometry["n_iter"])
            if self.geometry["n_LV"] > 0:
                # write_lattice_vectors
                with open(str(file_name), "w") as lattice:
                    for i in range(self.geometry["n_LV"]):
                        lattice.write(
                            "lattice_vector {:16.6f} {:16.6f} {:16.6f}\n".format(
                                float(lattice_vector[i][0]),
                                float(lattice_vector[i][1]),
                                float(lattice_vector[i][2])
                            )
                        )

            self.io.write(atoms, file_name.stem, file_name.parent, True, "a")

        def read_LV(aims_file):
            lattice_vector = []
            for _ in range(3):
                aux = next(aims_file).split()
                lattice_vector.append([aux[1], aux[2], aux[3]])

            return lattice_vector

        lattice_vector = []
        if "| Number of atoms" in line:
            self.geometry["n_atoms"] = int(line.split()[5])
        elif "| Number of lattice vectors" in line:
            self.geometry["n_LV"] = int(line.split()[6])
        elif "Input geometry:" in line:
            try:
                aux = next(aims_file)
                if "| Unit cell:" in aux:
                    lattice_vector = read_LV(aims_file)
                next(aims_file)
                next(aims_file)
                atoms = read_atoms(aims_file)
                write_geometry(atoms, lattice_vector)
            except StopIteration:
                msg = " analysis - 'aims.out' contains an error in the input geometry."
                self._print_console(msg, self.mtype[406], exit=False)
        elif "Updated atomic structure:" in line:
            next(aims_file)
            if self.geometry["n_LV"] > 0:
                lattice_vector = read_LV(aims_file)
                next(aims_file)
            atoms = read_atoms(aims_file)
            write_geometry(atoms, lattice_vector)

    def properties_info(self, line):
        """
        Function based on the 'script_energy_order' script.

        Parameters
        ----------
        line: file object
            The current file position.
        """

        if self.get_energy and "Total energy, T -> 0" in line:
            self.property["last_energy"] = line.split()[9]
            self.property["total_energy"] += "{}\n".format(
                self.property["last_energy"])
        elif self.get_mag and "N_up - N_down" in line:
            self.property["last_mag"] = line.split()[7]
            self.property["mag"] += "{}\n".format(self.property["last_mag"])
        elif self.get_homo and "Highest occupied state" in line:
            self.property["last_homo"] = line.split()[5]
            self.property["homo"] += "{}\n".format(self.property["last_homo"])
        elif self.get_lumo and "Lowest unoccupied state" in line:
            self.property["last_lumo"] = line.split()[5]
            self.property["lumo"] += "{}\n".format(self.property["last_lumo"])
        elif self.get_change_energy:
            if "Change of charge" in line:
                self.property["change_charge"] += "{} {}\n".format(
                    line.split()[6], line.split()[7] if len(line.split()) > 7 else "0"
                )
            elif "Change of sum of eigenvalues" in line:
                self.property["change_eign"] += "{}\n".format(line.split()[7])
            elif "Change of total energy" in line:
                self.property["change_total_energy"] += "{}\n".format(line.split()[6])
            elif "Change of forces" in line:
                self.property["change_forces"] += "{}\n".format(line.split()[5])

    def check_convergence(self, line):
        """
        Function based on the 'script_finish' script.

        Parameters
        ----------
        line: file object
            The current file position.
        """

        if "Present geometry is converged" in line:
            self.is_ok["Present"] = 1
        elif "Have a nice day" in line:
            self.is_ok["Have"] = 1

    def fhi_aims_analysis(self, calc_dir, ignore_ok=False):
        """
        Function based on the 'fhi-aims_analysis' script.

        Parameters
        ----------
        calc_dir: Pathlib-like object
            Path with the aims.out file.
        ignore_ok: bool, default False
            If True, the analysis will also be performed for the
            folders with 'OK' at its name.
        """

        if not ignore_ok and calc_dir.name.endswith("_OK"):
            msg = " analysis - '{}' contains '_OK' at the end. Try to use the " \
                  "--ignore-ok argument to perform the analysis for this folder.".format(
                calc_dir.name
            )
            self._print_console(msg, self.mtype[406], exit=False)
            return
        else:

            calc_files = ["relaxation.info", "convergence.info",
                          "total_energy_all.info", "mag_moments_all.info",
                          "homo_all.info", "lumo_all.info", "ecn_results",
                          "eigenvalues_convergence_all.info", "vesta.xyz",
                          "geometry.in.next_step", "final_energy_t0.info",
                          "total_energy_convergence_all.info", "ECNOUTPUT",
                          "forces_convergence_all.info", "mag_moments.info",
                          "total_energies_t0.info", "total_energy_all.info",
                          "charge_convergence_all.info", "RADIUSOUT", "geometries"
                          ]

            self.utils.path = calc_dir
            self.utils.remove(calc_files)

            # Initializing geometry info
            # Salvar o path antigo em alguma variavel
            if self.get_geometry:
                self.utils.mkdir = True
                self.utils.path = self.utils.path / "geometries"

            # ================= HEADERS =================
            # Initializing relaxation info
            relaxation = "\n# Step Total energy [eV]   E-E(1) [meV]   Free " \
                                "energy [eV]   F-F(1) [meV]   max. force [eV/AA]\n \n"
            # Initializing convergence info
            convergence = "#   Step  s.c.f._iterations_taken \n"
            # ===========================================

            # Relaxation dictionary
            self.relaxation = {"opt": 0, "1st_energy": None, "n_rel": 0}
            # Convergence dictionary
            self.convergence = {"iter": 0, "now": 0}
            # Geometry dictionary
            self.geometry = {"n_iter": 0, "n_LV": 0, "n_atoms": 0}
            # Properties dictionary
            self.property = {"total_energy": "", "change_forces": "",
                             "lumo": "", "change_eign": "", "mag": "",
                             "change_total_energy": "", "homo": "",
                             "change_charge": "", "last_energy": "",
                             "last_mag": "", "last_homo": "", "last_lumo": ""}

            # Convergence dictionary
            self.is_ok = {"Have": 0, "Present": 0}

            with open(str(calc_dir / "aims.out"), "r") as aims:
                for line in aims:
                    if self.get_relaxation:
                        relaxation += self.relaxation_info(aims, line)
                    if self.get_convergence:
                        convergence += self.convergence_info(line)
                    if self.get_geometry:
                        self.geometry_info(aims, line)
                    if self.get_properties:
                        self.properties_info(line)
                    self.check_convergence(line)

            # Renaming the folder (check_convergence)
            # So salva as informacoes se o calculo estiver convergido
            if (self.is_ok["Have"] and self.is_ok["Present"]) or (self.is_ok["Have"] and self.singlepoint):
                # Saving all files
                if self.get_relaxation:
                    with open(str(calc_dir / calc_files[0]), "w") as file:
                        file.write(relaxation)

                if self.get_convergence:
                    with open(str(calc_dir / calc_files[1]), "w") as file:
                        file.write(convergence)

                if self.get_energy:
                    with open(str(calc_dir / calc_files[2]), "w") as file:
                        file.write(self.property["total_energy"])

                if self.get_mag:
                    with open(str(calc_dir / calc_files[3]), "w") as file:
                        file.write(self.property["mag"])

                if self.get_homo:
                    with open(str(calc_dir / calc_files[4]), "w") as file:
                        file.write(self.property["homo"])

                if self.get_lumo:
                    with open(str(calc_dir / calc_files[5]), "w") as file:
                        file.write(self.property["lumo"])

                if self.get_change_energy:
                    with open(str(calc_dir / calc_files[17]), "w") as file:
                        file.write(self.property["change_charge"])
                    with open(str(calc_dir / calc_files[7]), "w") as file:
                        file.write(self.property["change_eign"])
                    with open(str(calc_dir / calc_files[11]), "w") as file:
                        file.write(self.property["change_total_energy"])
                    with open(str(calc_dir / calc_files[13]), "w") as file:
                        file.write(self.property["change_forces"])

                if not calc_dir.name.endswith("_OK"):
                    try:
                        calc_dir.replace(str(calc_dir) + "_OK")
                    except NotImplementedError:
                        calc_dir.rename(str(calc_dir) + "_OK")

                # energy_order
                if self.get_energy and self.get_mag and self.get_homo and self.get_lumo:
                    return [float(self.property["last_energy"]) if self.property["last_energy"] else 0, 
                            float(self.property["last_mag"]) if self.property["last_mag"] else 0,
                            float(self.property["last_homo"]) if self.property["last_homo"] else 0, 
                            float(self.property["last_lumo"]) if self.property["last_lumo"] else 0]
            return 

    def energy_order(self, nunits=1, ignore_ok=False, save="parent", check_convergence=False):
        """
        Function based on the 'script_energy_order' script.

        Parameters
        ----------
        nunits: float, default 1
            script_energy_order's units parameter
        ignore_ok: bool, default False
            If True, the analysis will also be performed for the
            folders with 'OK' at its name.
        save: str, default parent
            If 'parent', then the 'structures' and 'table_energy_order'
            will be saved in the parent folder of the calculations. If
            'auto', then the 'structures' and 'table_energy_order' will
            be saved in the current folder.
        """

        if not isinstance(nunits, (float, int)):
            msg = "analysis - optional field 'nunits' is not a float."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        if not isinstance(ignore_ok, bool):
            msg = "analysis - optional field 'ignore_ok' is not a bool."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        if not isinstance(save, str):
            msg = "analysis - optional field 'save' is not a str."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        if save not in ["parent", "auto"]:
            msg = "analysis - optional field 'save' is not valid."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)         

        def fhi_aims_to_vesta(calc_dir, prefix, num_dir):
            """
            Function based on the 'Fhi-aims_to_vesta_1.x' script.

            Parameters
            ----------
            calc_dir: str or Pathlib-like object
                Path with the geometry folder.
            """

            if not calc_dir.exists():
                if not calc_dir.name.endswith("_OK"):
                    calc_dir = calc_dir.parent / (calc_dir.name + "_OK")

            if calc_dir.exists():
                geom_in = -1
                for geom in list(calc_dir.joinpath("geometries").glob("geometry*.in")):
                    # caso exista um erro no nome try: ..;
                    aux = int(geom.stem.split("-")[1])
                    if aux >= geom_in:
                        geom_in = aux

                if geom_in == -1:
                    msg = "analysis - required field 'calc_dir' ({}) has no 'geometry.in' in 'geometries' folder.".format(calc_dir)
                    self._print_console(self.alert[405](msg), self.mtype[405], exit=False)
                    # raise ValueError(msg)
                else:
                    # Converting the geometry.in to vesta.xyz
                    arr = self.io.read(calc_dir / "geometries/geometry-{:06d}.in".format(geom_in), True)
                    self.io.write(arr, "vesta.xyz", calc_dir)

                    self.io.write(arr, "geometry.in", calc_dir, geometryIn=True)

                    # Creating a new folder for the structures
                    if self.table_energy:
                        self.io.mkdir = True
                        if save == "parent":
                            self.io.path = calc_dir.parent / "{}_structures".format(prefix)
                        else:
                            self.io.path = self.path / "structures"
                        # Copying the vesta.xyz to the new structure folder
                        copy2(
                            str(calc_dir / "vesta.xyz"),
                            str(self.io.path / "{}_{:03d}.xyz".format(prefix, num_dir))
                        )

        retrv_check = self.table_energy
        if check_convergence:
            retrv_check = False
            self.get_relaxation = retrv_check
            self.get_convergence = retrv_check
            self.get_geometry = retrv_check
            self.get_homo = retrv_check
            self.get_lumo = retrv_check
            self.get_mag = retrv_check
            self.get_energy = retrv_check
            self.get_change_energy = retrv_check
            self.get_properties = retrv_check

        aims_folder = self.retrv(["aims.out"], check=retrv_check, relative=False)

        if len(aims_folder) == 0:
            msg = "The source path ({}) has no 'aims.out' file(s).".format(self.path)
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise ValueError(msg)
        else:
            # Initializing energy_order
            properties = []
            for calc_dir in aims_folder:
                aux = self.fhi_aims_analysis(calc_dir, ignore_ok)

                try:
                    prefix = calc_dir.name.split("_")
                    prefix, num_dir = prefix[0], int(prefix[1])
                except:
                    prefix, num_dir = "", ""
                    self.table_energy = False
                if aux and self.table_energy:
                    # Get folder information
                    if save == "auto":
                        prefix = "--".join(calc_dir.parent.parts) + "--" + prefix
                        properties.append(aux + [prefix + "--" + str(num_dir)])
                    else:
                        properties.append(aux + [num_dir])
                fhi_aims_to_vesta(calc_dir, prefix, num_dir)

            if len(properties) > 1 and self.table_energy:
                # Getting total energy values and sorting
                sorting = sorted(
                    [(v[0], idx) for idx, v in enumerate(properties)],
                    key=lambda x: x[0],
                    reverse=True
                )
                delta = sorting[-1][0]  # Getting the value not the index

                with open(str(self.path / "table_energy_order"), "w") as table:
                    for _, i in sorting:
                        table.write(
                            "{: <14} {} {:12.8f} {:14.8f} {:14.8f} {:8.4f} {:8.4f} {:8.4f} {:8.4f}  \n".format(
                                aims_folder[i].name.split("_")[0] if "_" in str(aims_folder[i]) else str(aims_folder[i]), 
                                properties[i][-1],
                                properties[i][0] if self.get_energy else 0, # t_energy
                                ((properties[i][0] - delta)/nunits)*1000 if self.get_energy else 0,
                                properties[i][0] + 453051.79777208 if self.get_energy else 0,  # E_ad
                                properties[i][1] if self.get_mag else 0,  # mag
                                properties[i][2] if self.get_homo else 0,  # homo
                                properties[i][3] if self.get_lumo else 0,  # lumo
                                (properties[i][3] - properties[i][2]) if self.get_lumo and self.get_homo else 0,  # gap
                            )
                        )

    def structure_analysis(self, filename, f=1.25):
        """
        Function based on the 'comp' script.

        Parameters
        ----------
        filename: str
            XYZ file.
        f: float, default 1.25
            script_energy_order's factor parameter
        """

        if not isinstance(f, (float, int)):
            msg = "analysis - optional field 'f' is not a float."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)   

        try:
            mol = self.io.read(self.path / filename, filename.suffix.lower() != ".xyz")
        except:
            msg = "analysis - No such file: {}.".format(filename)
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise ValueError(msg)

        var_f = [0] * len(mol)
        p1 = "Cutoff Radius Factor: {}\n\nClosest neighbor for each atom:\n".format(f)
        p2 = ""

        for idx, atom in enumerate(mol):
            dist = [[
                norm([atom[1]-atomy[1], atom[2]-atomy[2], atom[3]-atomy[3]]),
                idy] for idy, atomy in enumerate(mol) if idy != idx
            ]

            min_distance, y = min(dist, key=lambda x: x[0])
            p1 += "{} {} {} {} distance: {}\n".format(atom[0], idx, mol[y][0], y, min_distance)

            # Second part
            coff = min_distance * f

            p2 += "\nClosest neighbors for {} {}:\n".format(atom[0], idx)

            e = []
            for value, k in dist:
                if value <= coff:
                    e.append(value)
                    p2 += "{} {} distance: {}\n".format(mol[k][0], k, value)

            var_f[idx] = len(e)

            p2 += "Coordination number: {}\nAverage bond distance: {}\n".format(
                var_f[idx], sum(e)/var_f[idx]
            )

        p2 += "\nAverage CN: {}".format(sum(var_f)/len(var_f))

        with open(str(self.path / "structure_analysis.info"), "w") as file:
            file.write(p1 + p2)
