from __future__ import print_function


import copy


from pathlib import Path
from shutil import rmtree, copy2, move as move2
from .qcalc import Qcalc


class Utils(Qcalc):

    def __init__(self, path=Path.cwd(), console=True):
        super(Utils, self).__init__(path, console=console)

    def update(self, qcalc_obj):
        self.__dict__.update(qcalc_obj.__dict__)

    def remove(self, files):
        """
        Delete a list of files in a specific path.

        Parameters
        ----------
        files: str or list
            List with the files or folders to be deleted.
        """

        if self.is_file():
            msg = "remove - It is not possible to remove files from a file path"\
                  ": '{}'.".format(self.path)
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise ValueError(msg)

        if isinstance(files, str):
            file_list = [files]
        elif isinstance(files, list):
            file_list = files
        else:
            msg = "remove - required field 'files' is not a str or list."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        for file in file_list:
            file_name = self.path / file
            if not file_name.exists():
                continue
            elif file_name.is_file():
                # Removing a file
                file_name.unlink()
            elif file_name.is_dir:
                # Removing all files in the folder,
                # then removing the folder itself.
                rmtree(str(file_name))

    def move(
        self,
        prefix,
        suffix="",
        copy=False,
        fmt="",
        keep_name=False,
        set_name="vesta_inicial.xyz"
    ):
        """
        Move files from the source folder to a destination folder.

        Parameters
        ----------
        prefix: str
            Prefix of the destination folder.
        suffix: str, optional
            Suffix of the destination folder.
        copy: bool, default False
            If True, this option will maintain a version of the file in
            the source folder.
        fmt: str, optional
            Move files with a specific format.
        keep_name: bool, default False
            Maintains the original file names.
        set_name: str, default "vesta_inicial.xyz"
            Set a new name to the moved files. If keep_name is False,
            this option will not work.
        """

        if not isinstance(prefix, str):
            msg = "move - required field 'prefix' is not a str."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        if not isinstance(suffix, str):
            msg = "move - optional field 'suffix' is not a str."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        if not isinstance(fmt, str):
            msg = "move - optional field 'fmt' is not a str."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        if not isinstance(copy, bool):
            msg = "move - optional field 'copy' is not a bool."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        if not isinstance(keep_name, bool):
            msg = "move - optional field 'keep_name' is not a bool."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        if not isinstance(set_name, str):
            msg = "move - optional field 'set_name' is not a str."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        if self.is_file():
            msg = " move - The source path ({}) is a file. Try to use the mv, "\
                  "or cp, Linux shell command to move, or copy, a file.".format(
                      self.path
                  )
            self._print_console(msg, self.mtype[406])
            raise ValueError(msg)

        new_suffix = "_" + suffix.replace("_", "") if suffix else suffix
        new_prefix = prefix.replace("_", "")

        # Getting all files in a folder
        new_fmt = "." + fmt.strip(".") if fmt else fmt

        files = list(self.path.rglob("*{}".format(new_fmt)))

        if len(files) == 0:
            msg = " The source path ({}) has no {}files to move.".format(
                self.path,
                "'" + new_fmt + "' " if new_fmt else ""
            )
            self._print_console(msg, self.mtype[404])
            raise ValueError(msg)

        ck_name = Path(set_name).suffix
        if not ck_name:
            msg = " move - Default name '{}' has no extension. It may introduce"\
                  " problems in future to find a file by its extension.".format(
                    set_name
                )
            self._print_console(msg, self.mtype[404])
            raise ValueError(msg)

        suffix_list = []
        for file in files:
            if file.suffix not in suffix_list and file.is_file():
                suffix_list.append(file.suffix)

        fixed_name = set_name
        if len(suffix_list) > 1 and not keep_name:
            msg = " move - Files with different extension were found (e.g.: {})."\
                  " Be careful when using this command, since it will rename all"\
                  " these files to '{}'. We strongly recommend filtering these "\
                  "files using the -f (or --format) argument or maintain the "\
                  "original name by using -k (or --keep-name) argument".format(
                    ", ".join(suffix_list),
                    set_name
                )
            self._print_console(msg, self.mtype[405])
            raise ValueError(msg)

        elif suffix_list[0] != ck_name:
            fixed_name = fixed_name.replace(ck_name, suffix_list[0])
            self._print_console(
                " Default name '{}' has a different extension of the founded files"
                ". '{}' were renamed to '{}'".format(set_name, set_name, fixed_name),
                self.mtype[200],
                exit=False
            )

        tmp = self.path
        file_num = 0
        for file_name in files:

            if file_name.is_file():
                # Creating a folder if path does not exist.
                file_num += 1
                self.mkdir = True
                self.path /= "{}_{:03d}{}".format(
                    new_prefix,
                    file_num,
                    new_suffix
                )

                out = self.path
                if not keep_name:
                    out /= fixed_name

                if copy:
                    copy2(str(file_name), str(out))
                else:
                    move2(str(file_name), str(out))

            self.path = tmp
