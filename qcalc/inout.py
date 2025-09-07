from .qcalc import Qcalc
from pathlib import Path


class IO(Qcalc):

    def __init__(self, path=Path.cwd(), console=False):
        super(IO, self).__init__(path, console=console)

    def update(self, qcalc_obj):
        self.__dict__.update(qcalc_obj.__dict__)

    def __read_XYZ(self, file):
        """
        Standard XYZ file reader.

        Parameters
        ----------
        file: Pathlib-like object
            The name of a XYZ file.

        Returns
        -------
        list
            Each column of the array will be the atom symbol, X, Y, and
            Z coordinates, respectively.
        """
        with open(str(file), "r") as xyz:
            # SKip the first two lines.
            next(xyz)
            next(xyz)
            for line in xyz:
                atom = line.split()
                if not line.strip(): # empty line
                    continue
                yield [
                    atom[0],  # atom symbol
                    float(atom[1]),  # X
                    float(atom[2]),  # Y
                    float(atom[3])   # Z
                ]

    def __read_geometry_in(self, file):
        """
        Reader of the XYZ file for FHI-aims application.

        Parameters
        ----------
        file: Pathlib-like object
            The name of a XYZ file.

        Returns
        -------
        list
            Each column of the array will be the atom symbol, X, Y, and
            Z coordinates, respectively.
        """
        with open(str(file), "r") as xyz:
            for idx, line in enumerate(xyz):
                if line.startswith("#") and idx == 0:
                    continue
                if not line.strip(): # empty line
                    continue
                atom = line.split()[1:]
                yield [
                    atom[3],  # atom symbol
                    float(atom[0]),  # X
                    float(atom[1]),  # Y
                    float(atom[2])   # Z
                ]

    def read(self, file, geometryIn=False):
        """
        XYZ file reader.

        Parameters
        ----------
        file: str or Pathlib-like object
            The name of the XYZ file.
        geometryIn: bool, default False
            If True, the input file should be a XYZ for FHI-aims
            application.

        Returns
        -------
        list
        """

        if not isinstance(geometryIn, bool):
            msg = "input/output - optional field 'geometryIn' is not a bool."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)
        try:
            if geometryIn:
                return list(self.__read_geometry_in(file))
            return list(self.__read_XYZ(file))
        except:
            msg = "input/output - Invalid XYZ input: {}.".format(file)
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise ValueError(msg)

    def write(self, arr, file, path, geometryIn=False, mode="w"):
        """
        Writer of XYZ file.

        Parameters
        ----------
        arr: list
            List with the atom symbol and XYZ coordinates.
        file: str or Pathlib-like object
            The name to save the XYZ file.
        path: str or Pathlib-like object
            The folder's name to save the XYZ file.
        geometryIn: bool, default False
            If True, the input file should be a XYZ for FHI-aims application.
        mode:  str, default w
            A string, define which mode you want to open the file in:
            "r" - Opens a file for reading, error if the file does not exist
            "a" - Opens a file for appending, creates the file if it does
             not exist
            "w" - Opens a file for writing, creates the file if it does
             not exist
            "x" - Creates the specified file, returns an error if the file exist
        """

        self.mkdir = True
        self.path = path

        if not isinstance(arr, list):
            msg = "input/output - required field 'arr' is not a list."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        if not isinstance(geometryIn, bool):
            msg = "input/output - optional field 'geometryIn' is not a bool."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        # Checking if the file format is the same as the geometryIn option
        file_name = self.path / file
        if file_name.suffix.lower() not in [".in", ".xyz"]:
            if geometryIn:
                file_name = file_name.with_suffix(".in")
            else:
                file_name = file_name.with_suffix(".xyz")

        with open(str(file_name), mode) as xyz:
            if geometryIn:
                xyz.write("#geometry.in{:16d}\n".format(len(arr)))
                for elem in arr:
                    try:
                        # Style get from create_geometry_zip
                        xyz.write(
                            "atom {:16.6f} {:16.6f} {:16.6f} \t {}\n".format(
                                float(elem[1]),
                                float(elem[2]),
                                float(elem[3]),
                                elem[0]
                            )
                        )
                    except ValueError:
                        self._print_console(
                            self.alert[405](
                                "input/output - wrong XYZ format.\n{}\t{}\t{}\t"
                                "{}\n[...]\nThe XYZ should contain in the first"
                                " column the atom symbol, and for the second to"
                                " the fourth, the X, Y, and Z coordinates".format(
                                    elem[0], elem[1], elem[2], elem[3]
                                )
                            ),
                            self.mtype[405]
                        )
                        raise ValueError(
                            "input/output - required field 'arr' should contain"
                            " in the first column the atom symbol, and for the "
                            "second to the fourth, the X, Y, and Z coordinates."
                        )
            else:
                xyz.write("{}\n\n".format(len(arr)))
                for elem in arr:
                    try:
                        xyz.write(
                            "{:4s}{: 24.16f}{: 24.16f}{: 24.16f}\n".format(
                                elem[0],
                                float(elem[1]),
                                float(elem[2]),
                                float(elem[3])
                            )
                        )
                    except ValueError:
                        self._print_console(
                            self.alert[405](
                                "input/output - wrong XYZ format.\n{}\t{}\t{}\t"
                                "{}\n[...]\nThe XYZ should contain in the first"
                                " column the atom symbol, and for the second to"
                                " the fourth, the X, Y, and Z coordinates".format(
                                    elem[0], elem[1], elem[2], elem[3]
                                )
                            ),
                            self.mtype[405]
                        )
                        raise ValueError(
                            "input/output - required field 'arr' should contain"
                            " in the first column the atom symbol, and for the "
                            "second to the fourth, the X, Y, and Z coordinates."
                        )
