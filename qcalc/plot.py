from .qcalc import Qcalc
from numpy import array
from pathlib import Path


class Plots(Qcalc):

    def __init__(self, path=Path.cwd(), console=False):
        super(Plots, self).__init__(path, console=console)
        self.matplotlib = True
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            msg = "Plots - Matplotlib package not found. Please, if you want to" \
                  " use this option, install Matplotlib in your environment."
            self._print_console(self.alert[406](msg), self.mtype[406], exit=False)
            self.matplotlib = False

    def update(self, qcalc_obj):
        self.__dict__.update(qcalc_obj.__dict__)

    def __file_reader(self, file_info, filename):
        """
        Analysis results reader.

        Parameters
        ----------
        file_info: str
            A list with instructions of how to read the file.
        filename: str or Pathlib-like object
            Path with the file.
        """

        data = []
        with open(str(filename), "r") as file:
            for idl, line in enumerate(file):
                if idl <= file_info[1]:
                    continue
                data.append([
                    float(v) for idv, v in enumerate(line.split()) if idv <= file_info[3]
                ])

        return array(data)

    def get_plot(self):
        """
        Plots the analysis files from a path.
        """

        # Creating a folder to save the plots
        import matplotlib.pyplot as plt

        folder = self.path
        self.mkdir = True

        info = [("relaxation.info",  # file name
                    2,  # skiprows (-1 to ignore)
                    ["# Step", "Total energy [eV]", "E-E(1) [meV]",  # columns name
                    "Free energy [eV]", "F-F(1) [meV]", "max. force [eV/AA]"],
                    5,  # ignore columns above a number
                    "Step"  # x-label
                ), 
                ("charge_convergence_all.info", -1,
                    ["Change of Charge","Spin density"], 1, "S.C.F. Iterations"),
                ("convergence.info", 0, ["# Step","S.C.F. Iterations Taken"],
                    1, "Step"),
                ("eigenvalues_convergence_all.info", -1, 
                    ["Eigenvalues Convergence"], 0, "S.C.F. Iterations"),
                ("forces_convergence_all.info", -1, ["Forces Convergence"],
                    0, "S.C.F. Iterations"),
                ("homo_all.info", -1, ["HOMO"], 0, "S.C.F. Iterations"),
                ("lumo_all.info", -1, ["LUMO"], 0, "S.C.F. Iterations"),
                ("mag_moments_all.info", -1, ["Mag Moments"], 0, "S.C.F. Iterations"),
                ("total_energy_all.info", -1, ["Total Energy"], 0, "S.C.F. Iterations"),
                ("total_energy_convergence_all.info", -1, ["Total Energy Convergence"],
                    0, "S.C.F. Iterations"),
                ]
        for file_info in info:

            self.path = folder
            aux = folder / file_info[0]
            # Only if the file exist
            if aux.is_file():
                # Creating the folder
                self.mkdir = True
                self.path = self.path / "plots"
                data = self.__file_reader(file_info, aux)

                if data.size == 0:  # if the file is empty
                    continue

                # For each column in the file
                for col in range(data.shape[1]):
                    if file_info[2][col] == "# Step":
                        continue
                    plt.plot(data[:, col], "green")
                    plt.ylabel(file_info[2][col])
                    plt.xlabel(file_info[4], fontsize=12)
                    plt.grid(True)
                    plt.tick_params(axis='x', labelsize=12)
                    plt.tick_params(axis='y', labelsize=12)
                    plt.savefig(
                        str(self.path.joinpath("{}.pdf".format(file_info[2][col].replace("/", "")))),
                        dpi=300,
                        bbox_inches='tight'
                    )
                    plt.clf()


    def plot(self, add_OK=False):
        """
        Plots all analysis results from a path.

        Parameters
        ----------
        add_OK: bool, default False
            Add '_OK' at the end of the path string.
        """
        if self.matplotlib:

            if add_OK:
                self.path = str(self.path) + "_OK"

            if self.is_file():
                self.get_plot()
            else:
                folders = self.retrv()
                for folder in folders:
                    self.path = folder
                    self.get_plot()
