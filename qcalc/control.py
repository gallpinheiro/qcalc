from .light import _ATOMINFO_


from numpy import unique
from pathlib import Path
from .qcalc import Qcalc


_ATOMS_ = {
    "Emptium": "00",
    "H": "01",
    "He": "02",
    "Li": "03",
    "Be": "04",
    "B": "05",
    "C": "06",
    "N": "07",
    "O": "08",
    "F": "09",
    "Ne": "10",
    "Na": "11",
    "Mg": "12",
    "Al": "13",
    "Si": "14",
    "P": "15",
    "S": "16",
    "Cl": "17",
    "Ar": "18",
    "K": "19",
    "Ca": "20",
    "Sc": "21",
    "Ti": "22",
    "V": "23",
    "Cr": "24",
    "Mn": "25",
    "Fe": "26",
    "Co": "27",
    "Ni": "28",
    "Cu": "29",
    "Zn": "30",
    "Ga": "31",
    "Ge": "32",
    "As": "33",
    "Se": "34",
    "Br": "35",
    "Kr": "36",
    "Rb": "37",
    "Sr": "38",
    "Y": "39",
    "Zr": "40",
    "Nb": "41",
    "Mo": "42",
    "Tc": "43",
    "Ru": "44",
    "Rh": "45",
    "Pd": "46",
    "Ag": "47",
    "Cd": "48",
    "In": "49",
    "Sn": "50",
    "Sb": "51",
    "Te": "52",
    "I": "53",
    "Xe": "54",
    "Cs": "55",
    "Ba": "56",
    "La": "57",
    "Ce": "58",
    "Pr": "59",
    "Nd": "60",
    "Pm": "61",
    "Sm": "62",
    "Eu": "63",
    "Gd": "64",
    "Tb": "65",
    "Dy": "66",
    "Ho": "67",
    "Er": "68",
    "Tm": "69",
    "Yb": "70",
    "Lu": "71",
    "Hf": "72",
    "Ta": "73",
    "W": "74",
    "Re": "75",
    "Os": "76",
    "Ir": "77",
    "Pt": "78",
    "Au": "79",
    "Hg": "80",
    "Tl": "81",
    "Pb": "82",
    "Bi": "83",
    "Po": "84",
    "At": "85",
    "Rn": "86",
    "Fr": "87",
    "Ra": "88",
    "Ac": "89",
    "Th": "90",
    "Pa": "91",
    "U": "92",
    "Np": "93",
    "Pu": "94",
    "Am": "95",
    "Cm": "96",
    "Bk": "97",
    "Cf": "98",
    "Es": "99",
    "Fm": "100",
    "Md": "101",
    "No": "102",
}


class ControlIn(Qcalc):

    def __init__(self, path=Path.cwd(), console=False):
        super(ControlIn, self).__init__(path, console=console)

    def update(self, qcalc_obj):
        self.__dict__.update(qcalc_obj.__dict__)

    def params_template(self):

        with open(str(self._pwd / "params.txt"), "w") as file:
            file.write("################################################################################\n")
            file.write("# This is the template file to set the parameters for the 'control.in' file.\n")
            file.write("# 1. Lines starting with '#' will be considered as comments.\n")
            file.write("# 2. The default value for each parameter is shown below.\n")
            file.write("# 3. Invalid parameter name will not be considered.\n")
            file.write("################################################################################\n")
            file.write("sc_accuracy_etot==1.0E-6\n")
            file.write("sc_accuracy_rho==1.0E-5\n")
            file.write("sc_accuracy_eev==1.0E-3\n")
            file.write("sc_accuracy_forces==1.0E-4\n")
            file.write("sc_iter_limit==500\n")
            file.write("relax_geometry trm==1.0E-3")

    def get_params_template(self):

        params_dict = {
            "sc_accuracy_etot": 1.0E-6,
            "sc_accuracy_rho": 1.0E-5,
            "sc_accuracy_eev": 1.0E-3,
            "sc_accuracy_forces": 1.0E-4,
            "sc_iter_limit": 500,
            "relax_geometry trm": 1.0E-3
        }

        params_file = self._pwd / "params.txt"
        if not params_file.exists():
            msg = "controlIn - 'params.txt' file was not found in the source path ({}).".format(self.path)
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise ValueError(msg)


        with open(str(params_file), "r") as file:
            for idx, line in enumerate(file):
                # not line.strip() >>  empty line
                if line.startswith("#") or not line.strip():
                    continue
                data = line.strip().split("==")
                if len(data) != 2:
                    msg = "controlIn - line {} is in the wrong format.".format(idx + 1)
                    self._print_console(self.alert[405](msg), self.mtype[405])
                    raise ValueError(msg)

                if data[0] not in params_dict:
                    msg = "controlIn - '{}' is not a valid parameter.".format(data[0])
                    self._print_console(self.alert[405](msg), self.mtype[405])
                    raise ValueError(msg)
                params_dict[data[0]] = data[1].replace(" ", "")

        return list(params_dict.values())

    def generate_controlIn(self, arr, tier=None, params="normal", charge="0.0", singleṕoint=False, load_params=False, from_path=""):
        """
        control.in file generator.

        Parameters
        ----------
        arr : list
            List with the atom symbol and XYZ coordinates.
        tier : int, default None
            Tier for the control.in file. The possible values are 1, 2,
            3, 4 and 5.
        params : str, default 'normal'
            Select the parameters' values of the control.in file.
        load_params: bool, default True
            Whether to load a file with the parameters

            If minim, then

                >> sc_accuracy_etot     1.0E-5
                >> sc_accuracy_rho      1.0E-4
                >> sc_accuracy_eev      1.0E-2
                >> sc_accuracy_forces   1.0E-3
                >> sc_iter_limit        1000
                >> relax_geometry trm   1.0E-2

            If normal, then

                >> sc_accuracy_etot     1.0E-6
                >> sc_accuracy_rho      1.0E-5
                >> sc_accuracy_eev      1.0E-3
                >> sc_accuracy_forces   1.0E-4
                >> sc_iter_limit        500
                >> relax_geometry trm   1.0E-3

            If accurate, then

                >> sc_accuracy_etot     1.0E-7
                >> sc_accuracy_rho      1.0E-6
                >> sc_accuracy_eev      1.0E-4
                >> sc_accuracy_forces   1.0E-5
                >> sc_iter_limit        1000
                >> relax_geometry trm   1.0E-4
        """

        level = {
            "minim":    ["1.0E-5", "1.0E-4", "1.0E-2", "1.0E-3", "1000", "1.0E-2"],
            "normal":   ["1.0E-6", "1.0E-5", "1.0E-3", "1.0E-4", "500", "1.0E-3"],
            "accurate": ["1.0E-7", "1.0E-6", "1.0E-4", "1.0E-5", "1000", "1.0E-4"],
        }

        if not isinstance(arr, list):
            msg = "controlIn - required field 'arr' is not a list."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        if not isinstance(params, str):
            msg = "controlIn - optional field 'params' is not a str."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        if params not in level.keys():
            msg = "controlIn - optional field 'params' received a invalid level. Valid argumers are: 'minim', 'normal', and 'accurate'."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise ValueError(msg)

        if not isinstance(load_params, bool):
            msg = "controlIn - optional field 'load_params' is not a bool."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        if isinstance(tier, int):
            if tier < 1 or tier > 5:
                msg = "controlIn - optional field 'tier' accepts values between 1 to 5."
                self._print_console(self.alert[405](msg), self.mtype[405])
                raise ValueError(msg)
        elif tier is not None:
            msg = "controlIn - optional field 'tier' is not an int."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        if load_params:
            level = {"normal": self.get_params_template()}
            params = "normal"

        cont = """#control.in
#
# Physical model
xc                       pbe
charge                   {0}
spin                     collinear
relativistic             atomic_zora scalar
default_initial_moment   hund

# SCF convergence
    occupation_type      gaussian 0.010

    mixer                pulay
    n_max_pulay          6
    charge_mix_param     0.10

    sc_accuracy_etot     {1[0]}
    sc_accuracy_rho      {1[1]}
    sc_accuracy_eev      {1[2]}
    sc_accuracy_forces   {1[3]}

    sc_iter_limit        {1[4]}
    vdw_correction_hirshfeld

# Relaxation
{2}    relax_geometry trm   {1[5]}
#    harmonic_length_scale  0.0025
#    energy_tolerance       1.00E-3\n""".format(charge, level[params], "#" if singleṕoint else "")

        atoms_arr = unique([elem[0] for elem in arr])

        if from_path != "":

            is_ok = True
            for key in atoms_arr:
                aux = Path(from_path) / "{}_{}_default".format(_ATOMS_[key], key)
                if not aux.exists():
                    is_ok = False
                    break

            if not is_ok:
                msg = "controlIn - File not found: {}.".format(aux)
                self._print_console(self.alert[405](msg), self.mtype[405])

            # Initializing control.in file
            with open(str(self.path / "control.in"), "w") as file:
                file.write(cont)
                for key in atoms_arr:
                    aux = str(Path(from_path) / "{}_{}_default".format(_ATOMS_[key], key))
                    is_one = is_two = is_three = is_four = is_five = False

                    with open(aux, "r") as template:
                        for line in template:
                            if line.strip() == "":
                                continue
                            if isinstance(tier, int):
                                if '"Further functions"' in line or 'Further basis' in line or 'Further functions' in line or "One more function" in line or "Two extra functions" in line or is_five:
                                    if tier == 5 and is_five and "#" in line and ("ionic" in line or "hydro" in line):
                                        line = line[1:]
                                    file.write(line)
                                    is_four, is_five = False, True
                                elif '"Fourth tier"' in line or 'Fourth tier -' in " ".join(line.split()) or is_four:
                                    if tier >= 4 and is_four and "#" in line and ("ionic" in line or "hydro" in line):
                                        line = line[1:]
                                    file.write(line)
                                    is_three, is_four = False, True
                                elif '"Third tier"' in line or 'Third tier -' in " ".join(line.split()) or is_three:
                                    if tier >= 3 and is_three and "#" in line and ("ionic" in line or "hydro" in line):
                                        line = line[1:]
                                    file.write(line)
                                    is_two, is_three = False, True
                                elif '"Second tier"' in line or 'Second tier -' in " ".join(line.split()) or is_two:
                                    if tier >= 2 and is_two and "#" in line and ("ionic" in line or "hydro" in line):
                                        line = line[1:]
                                    file.write(line)
                                    is_one, is_two = False, True
                                elif '"First tier"' in line or 'First tier -' in " ".join(line.split()) or is_one:
                                    if tier >= 1 and is_one and "#" in line and ("ionic" in line or "hydro" in line):
                                        line = line[1:]
                                    file.write(line)
                                    is_one = True  
                                else:
                                    file.write(line)
                            else:
                                file.write(line)
        else:

            # Initializing control.in file
            with open(str(self.path / "control.in"), "w") as file:
                # Printing header
                file.write(cont)
                # For each atom in the molecule
                for elem in atoms_arr:
                    # Check if the atom exists
                    if elem in _ATOMS_:
                        # Printing atom's header
                        file.write(_ATOMINFO_[elem]["head"])
                        # Printing atom's tiers
                        for key in range(1, 6):
                            try:
                                # If None, print the default configuration
                                if tier is None:
                                    for ltier in _ATOMINFO_[elem][key]:
                                        file.write(
                                            ltier[1] if ltier[0] is None else ltier[0] + ltier[1]
                                        )
                                # If the actual tier is bigger than the
                                # selected tier, comment all lines
                                elif key > tier:
                                    # Getting all lines
                                    for ltier in _ATOMINFO_[elem][key]:
                                        file.write(
                                            ltier[1] if ltier[0] is None else "#" + ltier[1]
                                        )
                                else:
                                    for ltier in _ATOMINFO_[elem][key]:
                                        file.write(ltier[1])
                            except (IndexError, KeyError):
                                # In the case of the element do not contain a key
                                pass
                    else:
                        msg = "controlIn - '{}' is not a valid atom.".format(elem)
                        self._print_console(self.alert[405](msg), self.mtype[405])
                        raise ValueError(msg)
