from __future__ import print_function


import copy
import errno
import sys


from pathlib import Path, PurePath


class Qcalc(object):

    def __init__(
        self,
        path=Path.cwd(),
        mkdir=False,
        console=False,
    ):
        self.__is_dir = True
        self.__is_file = False
        self.console = console  # Change to True in console.py
        self.mkdir = mkdir
        self._pwd = Path.cwd()
        self._module = "qcalc"
        self.alert, self.mtype = self.default_alerts()
        self.palette = {
            "w": {"alert": "\033[93m\033[1mWARNING:\033[0m\033[93m", "exit": 0},
            "e": {"alert": "\033[91m\033[1mERROR:\033[0m\033[91m", "exit": 1},
            "n": {"alert": "\033[0m", "exit": 0},
            "s": {"alert": "\033[92m\033[1mSUCCESSFUL:\033[0m\033[92m", "exit": 0}
        }
        self.path = path

    def __repr__(self):
        return "Current path: {} (directory={}, mkdir={})".format(
            self.path,
            self.is_dir(),
            self.mkdir
        )

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, var):

        new_path = Path(var) if isinstance(var, str) else var
        if isinstance(new_path, PurePath):
            if new_path.exists():
                self._path = new_path.absolute()
                self.__is_dir = new_path.is_dir()
                self.__is_file = new_path.is_file()
                # Caso seja solicitado para criar uma pasta que ja existe
                if self.mkdir:
                    # Imprimir que a pasta existe
                    self.mkdir = False
            elif self.mkdir:
                try:
                    # Python v3
                    new_path.mkdir(parents=True, exist_ok=True)
                except TypeError:
                    # Python v2
                    try:
                        new_path.mkdir(parents=True)
                    except OSError as e:
                        if e.errno != errno.EEXIST:
                            self._print_console(
                                self.alert[405]("mkdir - " + str(e)),
                                self.mtype[405]
                            )
                            raise OSError("mkdir - " + str(e))
                self._path = new_path.absolute()
                self.__is_dir = new_path.is_dir()
                self.__is_file = new_path.is_file()
                self.mkdir = False
            else:
                self._print_console(
                    self.alert["path"][404](var),
                    self.mtype[404]
                )
                raise ValueError(self.alert["path"][404](var)+" If you want to "
                                 "create a new folder, set mkdir as 'True'.")
        else:
            self._print_console(
                "Internal error has occurred. " + self.alert["path"][415] +
                "Please, report this error!",
                self.mtype[415]
            )
            raise TypeError(self.alert["path"][415])

    @property
    def mkdir(self):
        return self._mkdir

    @mkdir.setter
    def mkdir(self, var):
        if not isinstance(var, bool):
            self._print_console(
                self.alert[405]("'mkdir' is not a bool."),
                self.mtype[405]
            )
            raise TypeError("'mkdir' is not a bool.")
        self._mkdir = var

    def is_dir(self):
        return self.__is_dir

    def is_file(self):
        return self.__is_file

    def retrv(self, constraints=None, check=False, relative=True):
        """
        Checks whether a path belongs to a folder with calculations.

        Parameters
        ----------
        path: str or Pathlib-like object
            Source folder with the calculations files.
        constraints: list, default None
            Files that the folder should have.
        check: bool, default False
            Check if the path contains a prefix followed by a number
        relative: bool, default True
            Relative path
        Returns
        -------
        A list with all calculations paths.
        """
        if not self.is_dir():
            msg = "{} - '{}' is a file.".format(self._module, self.path)
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise ValueError(msg)

        if not constraints:
            return [p for p in self.path.iterdir() if p.is_dir()] + [self.path]
        
        retrv_paths = []
        for p in self.path.rglob(constraints[0]):
            exist = True
            for c in constraints[1:]:
                if not p.parent.joinpath(c).exists():
                    exist = False
                    break
            if exist:
                if check:
                    try:
                        prefix = p.parent.name.split("_")
                        _, _ = prefix[0], int(prefix[1])
                    except:
                        msg = " Ignoring the following folder since it does not"\
                              " contain a prefix followed by a number (i.e., " \
                              "prefix_001): {}. Try to use --no-pattern to perform"\
                              " the operation for this folder".format(p)
                        self._print_console(msg, self.mtype[406], exit=False)
                        continue
                if relative:
                    retrv_paths.append(p.relative_to(self.path).parent)
                else:
                    retrv_paths.append(p.parent)
    
        if len(retrv_paths) == 0:
            self._print_console(
                self.alert["__retrv"][404](constraints),
                self.mtype[404]
            )
            raise ValueError(self.alert["__retrv"][404](constraints))

        return retrv_paths

    def _print_console(self, alert, mtype, exit=True):

        if self.console:
            print(self.palette[mtype]["alert"] + alert, end="\033[0m\n")
            if exit:
                sys.exit(self.palette[mtype]["exit"])

    def default_alerts(self):

        alerts = {
            "path": {
                404: lambda path: "'{}' does not exist.".format(path),
                415: "'path' is not a str or pathlib-like object. Consider to "
                "use the pathlib package and declare your path as a Path class.",
            },
            405: lambda msg: " Unexpected error occurred. {}".format(msg),
            200: lambda msg: "Ignore the following message if you submitted "
            "this task using a job file: You are executing a {} for several"
            " files. This action may put your account at risk by taking a "
            "block from the server for 30 consecutive days.".format(msg),
            "__retrv": {
                404: lambda const: " {} - '{}' does not contain the following"
                " files: {}".format(
                    self._module,
                    self.path,
                    ", ".join(const)
                )
            }
        }

        mtype = {404: "e", 415: "e", 405: "e", 100: "n",
                 406: "w", 200: "w", 202: "s"}

        return alerts, mtype