#!/usr/bin/env python

from __future__ import print_function

import argparse
import sys
import signal

from pathlib import Path
from .inout import IO
from .qcalc import Qcalc
from .utils import Utils
from .control import ControlIn
from .job import Job
from .analysis import Analysis
from .plot import Plots


MINUTES = 60


class MakeArgparser(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description="",
            epilog="Project developed by the QTNano group.",
            usage='''qcalc <command> [<args>]

qcalc offers a command-line interface for automatize FHI-aims
calculation. These are qcalc commands used in various situations:
   run           run the calculations
   move          moves an directory's files to an output directory
   convert       convert a XYZ (or geometry.in) to geometry.in (or XYZ) file
   controlin     generates the control.in file
   job           creates a job file to execute a calculation
   analysis      make an analysis in the calculation's output file
   plot          plots the analysis' output
''')

        parser.add_argument("command", help="Subcommand to run")
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if (not hasattr(self, args.command) or
                args.command in ["get_command", "get_arguments"]):
            print("Unrecognized command. Use 'qcalc -h' for help")
            exit(1)
        # use dispatch pattern to invoke method with same name
        self.__command = args.command
        self.__arguments = getattr(self, args.command)()

    def get_command(self):
        return self.__command

    def get_arguments(self):
        return self.__arguments

    def run(self):

        parser = argparse.ArgumentParser(
            description="Run a calculation."
        )

        parser.add_argument(
            "-j",
            "--job",
            action="store_true",
            help=argparse.SUPPRESS,
        )

        # job adjustments
        parser.add_argument(
            "num_cores",
            metavar="NUMBER OF CORES",
            nargs=1,
            type=int,
            help="set the number of cores.",
        )

        parser.add_argument(
            "queue_sys",
            metavar="QUEUE SYSTEM",
            nargs=1,
            type=str,
            choices=["longq", "workq", "shortq"],
            help="set the queue system.",
        )

        parser.add_argument(
            "prefix",
            metavar="PREFIX",
            nargs=1,
            type=str,
            help="prefix of the destination folder."
        )

        parser.add_argument(
            "path",
            metavar="FILE OR DIR",
            nargs="?",
            type=str,
            help="directory with the calculation files or a calculation file.",
            default=Path().cwd()
        )

        # move adjustment
        parser.add_argument(
            "-s",
            "--suffix",
            metavar="SUFFIX",
            nargs=1,
            type=str,
            help="suffix of the destination folder.",
            default=[""]
        )

        # control.in adjustment
        parser.add_argument(
            "-t",
            "--tier",
            type=int,
            choices=[1, 2, 3, 4, 5],
            help="select a specific tier for the control.in file."
        )

        parser.add_argument(
            "-l",
            "--level",
            type=str,
            choices=["minim", "normal", "accurate"],
            help="select a level with the parameters' values"
            " for the control.in file.",
            default="normal"
        )

        parser.add_argument(
            "--ignore-move",
            action="store_true",
            help="skip the move files process.",
        )

        parser.add_argument(
            "--ignore-conversion",
            action="store_true",
            help="skip the conversion process.",
        )

        parser.add_argument(
            "--ignore-controlin",
            action="store_true",
            help="skip the control.in generation process.",
        )

        parser.add_argument(
            "--ignore-job",
            action="store_true",
            help="skip the generation of the job file.",
        )

        parser.add_argument(
            "-c",
            "--charge",
            metavar="n",
            nargs="?",
            type=str,
            help="Charge of the control.in file.",
            default="0.0"
        )

        parser.add_argument(
            "--singlepoint",
            action="store_true",
            help="control.in for singlepoint calculation.",
        )

        parser.add_argument(
            "--set-template",  
            action="store_true",
            help="Define the parameters of the 'control.in' file according to the values in the 'params.txt'.",
        )
        
        parser.add_argument(
            "-b",
            "--batch",
            type=int,
            help="create job files with a maximum of calculations equal to the batch.",
            default=-1
        )

        parser.add_argument(
            "-o",
            "--ignore-ok",
            action="store_true",
            help="create a job file for the concluded calculations (with the 'OK'"
            " at the end of the folder name).",
        )

        parser.add_argument(
            "-d",
            "--dir-name",
            type=int,
            help="set directory's name as the prefix of the name of the job file.",
            default=-1
        )

        # skip confirmation
        parser.add_argument(
            "-y",
            "--skip",
            action="store_false",
            help="skip the message that confirms all operations.",
        )

        return parser.parse_args(sys.argv[2:])

    def convert(self):

        parser = argparse.ArgumentParser(
            description="Convert a xyz (or geometry.in) to geometry.in (or xyz)"
            " file"
        )

        parser.add_argument(
            "-j",
            "--job",
            action="store_true",
            help=argparse.SUPPRESS,
        )

        parser.add_argument(
            "-k",
            "--keep-name",
            action="store_true",
            help="maintains the original file names.",
        )

        parser.add_argument(
            "file_format",
            type=str,
            choices=["xyz", "geometry.in"],
            help="select the format of the input file.",
            default="xyz"
        )

        parser.add_argument(
            "path",
            metavar="FILE OR DIR",
            nargs="?",
            type=str,
            help="input file or directory with the input files.",
            default=Path().cwd()
        )

        parser.add_argument(
            "-y",
            "--skip",
            action="store_false",
            help="skip the message that confirms all operations.",
        )

        return parser.parse_args(sys.argv[2:])


    def move(self):

        parser = argparse.ArgumentParser(
            description="Moves a directory's files to an output directory"
        )

        parser.add_argument(
            "-j",
            "--job",
            action="store_true",
            help=argparse.SUPPRESS,
        )

        parser.add_argument(
            "-c",
            "--copy",
            action="store_true",
            help="if selected, this option will keep a version of the file"
            " in the source and destination folder."
        )

        parser.add_argument(
            "-k",
            "--keep-name",
            action="store_true",
            help="maintains the original file names.",
        )

        parser.add_argument(
            "-f",
            "--format",
            metavar="FILENAME EXTENSION",
            nargs=1,
            type=str,
            help="move files with a specific format.",
            default=[""]
        )

        parser.add_argument(
            "--set-name",
            metavar="NAME",
            nargs=1,
            type=str,
            help="the name to be used to rename the files.",
            default=["vesta_inicial.xyz"]
        )

        parser.add_argument(
            "-s",
            "--suffix",
            metavar="SUFFIX",
            nargs=1,
            type=str,
            help="suffix of the destination folder.",
            default=[""]
        )

        parser.add_argument(
            "path",
            metavar="FILE OR DIR",
            nargs="?",
            type=str,
            help="source folder with the files.",
            default=Path().cwd()
        )

        parser.add_argument(
            "prefix",
            metavar="PREFIX",
            nargs=1,
            type=str,
            help="prefix of the destination folder."
        )

        parser.add_argument(
            "-y",
            "--skip",
            action="store_false",
            help="skip the message that confirms all operations.",
        )

        return parser.parse_args(sys.argv[2:])

    def controlin(self):

        parser = argparse.ArgumentParser(
            description="Generate the control.in file"
        )

        parser.add_argument(
            "-j",
            "--job",
            action="store_true",
            help=argparse.SUPPRESS,
        )

        parser.add_argument(
            "-t",
            "--tier",
            type=int,
            choices=[1, 2, 3, 4, 5],
            help="select a specific tier for the control.in file."
        )

        parser.add_argument(
            "-l",
            "--level",
            type=str,
            choices=["minim", "normal", "accurate"],
            help="select a level with the parameters' values for the control.in file.",
            default="normal"
        )

        parser.add_argument(
            "path",
            metavar="FILE OR DIR",
            nargs="?",
            type=str,
            help="input XYZ file or directory with XYZ files.",
            default=Path().cwd()
        )

        parser.add_argument(
            "--from-path",
            metavar="templates",
            nargs=1,
            type=str,
            help="path with templates for the control.in file.",
            default=[""]
        )

        parser.add_argument(
            "-c",
            "--charge",
            metavar="n",
            nargs="?",
            type=str,
            help="Charge of the control.in file.",
            default="0.0"
        )

        parser.add_argument(
            "--singlepoint",
            action="store_true",
            help="control.in for singlepoint calculation.",
        )

        parser.add_argument(
            "-g",
            "--get-template",
            action="store_true",
            help="Generate the 'params.txt' file.",
        )

        parser.add_argument(
            "--set-template",  
            action="store_true",
            help="Define the parameters of the 'control.in' file according to the values in the 'params.txt'.",
        )

        parser.add_argument(
            "-y",
            "--skip",
            action="store_false",
            help="skip the message that confirms all operations.",
        )

        return parser.parse_args(sys.argv[2:])

    def job(self):

        parser = argparse.ArgumentParser(
            description="Create a job file to execute a calculation"
        )

        parser.add_argument(
            "-j",
            "--job",
            action="store_true",
            help=argparse.SUPPRESS,
        )

        parser.add_argument(
            "num_cores",
            metavar="NUMBER OF CORES",
            nargs=1,
            type=int,
            help="set the number of cores.",
        )

        parser.add_argument(
            "queue_sys",
            metavar="QUEUE SYSTEM",
            nargs=1,
            type=str,
            help="set the queue system.",
        )

        parser.add_argument(
            "path",
            metavar="DIR",
            nargs="?",
            type=str,
            help="directory with the calculations' files.",
            default=Path().cwd()
        )

        parser.add_argument(
            "-b",
            "--batch",
            type=int,
            help="create job files with a maximum of calculations equal to the batch.",
            default=-1
        )

        parser.add_argument(
            "-o",
            "--ignore-ok",
            action="store_true",
            help="create a job file for the concluded calculations (with the 'OK'"
            " at the end of the folder name).",
        )

        parser.add_argument(
            "-d",
            "--dir-name",
            action="store_true",
            help="set directory's name as the prefix of the name of the job file."
        )

        parser.add_argument(
            "-y",
            "--skip",
            action="store_false",
            help="skip the message that confirms all operations.",
        )

        return parser.parse_args(sys.argv[2:])

    def analysis(self):

        parser = argparse.ArgumentParser(
            description="Analyze a calculation output"
        )

        parser.add_argument(
            "-j",
            "--job",
            action="store_true",
            help=argparse.SUPPRESS,
        )

        parser.add_argument(
            "path",
            metavar="DIR",
            nargs="?",
            type=str,
            help="directory with the calculations' files.",
            default=Path().cwd()
        )

        parser.add_argument(
            "-f",
            "--factor",
            metavar="N",
            nargs="?",
            type=float,
            help="cutoff radius factor of the structure analysis.",
            default=1.25
        )

        parser.add_argument(
            "-n",
            "--nunits",
            metavar="N",
            nargs="?",
            type=float,
            help="nunits parameter.",
            default=1
        )

        parser.add_argument(
            "-o",
            "--ignore-ok",
            action="store_true",
            help="run analysis only if the folder does not contain an 'OK' in the name.",
        )

        parser.add_argument(
            "--no-pattern",
            action="store_false",
            help="run analysis for folders with no prefix and a number in their name.",
        )

        # customizing analysis
        parser.add_argument(
            "-s",
            action="store_true",
            help="make a structural analysis.",
        )

        parser.add_argument(
            "--singlepoint",
            action="store_true",
            help="analysis for singlepoint calculation.",
        )

        parser.add_argument(
            "-c",
            "--check-convergence",
            action="store_true",
            help="check if the calculation converged.",
        )

        parser.add_argument(
            "--set-name",
            metavar="NAME",
            nargs=1,
            type=str,
            help="define the file name to perform the structural analysis.",
            default=["vesta.xyz"]
        )

        parser.add_argument(
            "-y",
            "--skip",
            action="store_false",
            help="skip the message that confirms all operations.",
        )

        return parser.parse_args(sys.argv[2:])

    def plot(self):

        parser = argparse.ArgumentParser(
            description="Create plots from the output of the analysis module"
        )

        parser.add_argument(
            "-j",
            "--job",
            action="store_true",
            help=argparse.SUPPRESS,
        )

        parser.add_argument(
            "path",
            metavar="DIR",
            nargs="?",
            type=str,
            help="a directory with the calculations' files.",
            default=Path().cwd()
        )

        parser.add_argument(
            "-y",
            "--skip",
            action="store_false",
            help="skip the message that confirms all operations.",
        )

        return parser.parse_args(sys.argv[2:])


def query_task(question):
    """
    Print and ask to confirm the task to be done in the
    command line.

    Parameters
    ----------
    question: str
        The message to be print.

    Returns
    -------
    bool
    """

    while True:
        print("{} Do you want to continue [Y/n]?".format(question), end=" ")
        try:
            choice = raw_input().lower()
        except NameError:
            choice = input().lower()

        if choice in ['', "yes", "y"]:
            INACTIVITY = False
            return True
        elif choice in ["no", "n"]:
            sys.exit(0)
        else:
            INACTIVITY = False
            print("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")


def conversor(
    path,
    file_type,
    keep_name=False,
    print_message=True,
    exit=True
):
    """
    Converts a XYZ (or geometry.in) file to geometry.in (or XYZ) file.

    Parameters
    ----------
    path: str or Pathlib-like object
        Input file or directory path.
    file_type: str
        Input file format (e.g., xyz or geometry.in).
    keep_name: bool, default False
        Maintains the original file names.
    print_message: bool, default True
        If True, create a message to be printed in the query_task function.
    """

    formats = {
        "xyz": {
            "from": ".xyz",
            "to": ".in",
            "default": "geometry.in",
            "geometryIn": False
        },
        "geometry.in": {
            "from": ".in",
            "to": ".xyz",
            "default": "vesta.xyz",
            "geometryIn": True
        }
    }

    qcalc = IO(path, console=True)

    if print_message:
        qcalc._print_console(
            "[INFO] Qcalc conversor can only convert XYZ to geometry.in files, "
            "or vice-versa.",
            qcalc.mtype[100],
            exit=False
        )

    if qcalc.is_dir():
        ff = "*.xyz" if formats[file_type]["from"] == ".xyz" else "geometry.in"
        files_list = list(qcalc.path.rglob(ff))
        len_files_list = len(files_list)
        if len_files_list == 1:
            qcalc.path = files_list[0]
        elif len_files_list == 0:
            qcalc._print_console(
                " The source path ({}) has no '{}' files.".format(
                    qcalc.path,
                    formats[file_type]["from"]
                ),
                qcalc.mtype[404]
            )

    # Case 1: if the path is a file
    if qcalc.is_file():

        # Checking if the file corresponding to the right file format
        if qcalc.path.name.lower().endswith(file_type):
            # Generating output file name
            if keep_name:
                file_out = qcalc.path.stem + formats[file_type]["to"]
            else:
                file_out = formats[file_type]["default"]

            # Printing the message
            if print_message:
                qst = "[1 file] Conversion of '{}' to '{}'.".format(
                    qcalc.path.name,
                    file_out
                )
                query_task(qst)
            # Reading the file
            arr = qcalc.read(qcalc.path, formats[file_type]["geometryIn"])
            # Writing the file to the output file format
            qcalc.write(
                arr,
                file_out,
                qcalc.path.parent,
                not formats[file_type]["geometryIn"]
            )

            if exit:
                qcalc._print_console(
                    " One file was converted without an error.",
                    qcalc.mtype[202]
                )
        else:

            qcalc._print_console(
                " The source path ({}) has no '{}' files.".format(
                    qcalc.path,
                    formats[file_type]["from"]
                ),
                qcalc.mtype[404]
            )

    # Case 2: if the path is a dir
    elif qcalc.is_dir():

        # Printing the message
        if print_message:
            qst = "[{} files] The files in source path ({}) will be converted "\
                "to '***{}' format.".format(
                    len_files_list,
                    qcalc.path,
                    formats[file_type]["to"]
                )
            query_task(qst)

        for file_name in files_list:
            arr = qcalc.read(file_name, formats[file_type]["geometryIn"])
            if keep_name:
                file_out = qcalc.path.stem + formats[file_type]["to"]
            else:
                file_out = formats[file_type]["default"]

            qcalc.write(
                arr,
                file_out,
                file_name.parent,
                not formats[file_type]["geometryIn"]
            )

        if exit:
            qcalc._print_console(
                " {} files were converted without an error.".format(len_files_list),
                qcalc.mtype[202]
            )
    else:
        qcalc._print_console(
            qcalc.alert[405](
                "The source path ({}) is neither a file nor a directory. Try to"
                " check if it exists.".format(qcalc.path)
            ),
            qcalc.mtype[405]
        )


def timeout_handler(signal, frame):
    print("\n\033[91m\033[1mALERT:\033[0m\033[91m Qcalc operates at two minutes "
          "maximum without submitting a job. If you want to continue this oper"
          "ation, please, create a job file using the same command with a --jo"
          "b at the end.", end="\033[0m\n")
    print("\033[93m\033[1m[INFO]\033[0m\033[93m If you continue this operation"
          " without submitting it to the queue system, you may block your acco"
          "unt for 30 consecutive days.", end="\033[0m\n")
    sys.exit(0)


def cancell_handler(signal, frame):
    print("\nCancelled")
    sys.exit(0)


def main():

    signal.signal(signal.SIGINT, cancell_handler)

    # Getting the arguments
    parser = MakeArgparser()
    args = parser.get_arguments()
    command = parser.get_command()

    if command == "convert":

        print_message = args.skip
        if not args.job:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(MINUTES)
        else: # not print messages if the job arg is True
            print_message = False

        conversor(
            args.path,
            args.file_format,
            args.keep_name,
            print_message 
        )

        if not args.job:
            signal.alarm(0)

    elif command == "move":

        suffix = "_" + args.suffix[0].strip("_")
        utils = Utils(args.path, console=True)

        utils._print_console(
            "[INFO] Qcalc can only move two or more files.",
            utils.mtype[100],
            exit=False
        )

        if not args.job:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(MINUTES)

            if args.skip:
                qst = "The files from the source path ({}) will be moved (or copied)" \
                    " into '{}_num{}', where num is an integer associated with" \
                    " the order that the files were moved (or copied).".format(
                        utils.path,
                        args.prefix[0],
                        suffix
                    )
                query_task(qst)

        utils.move(
            args.prefix[0],
            suffix,
            args.copy,
            args.format[0],
            args.keep_name,
            args.set_name[0]
        )

        utils._print_console(" All files were moved.", utils.mtype[202])

        if not args.job:
            signal.alarm(0)

    elif command == "controlin":

        controlin = ControlIn(args.path, console=True)
        io = IO(args.path, console=True)

        controlin._print_console(
            "[INFO] Qcalc can only generate control.in file for XYZ inputs.",
            controlin.mtype[100],
            exit=False
        )

        if not args.job:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(MINUTES)

        if args.get_template:
            controlin.params_template()
            controlin._print_console(" 'params.txt' was generated without an error.", controlin.mtype[202])

        if controlin.is_dir():

            dir_list = list(controlin.path.rglob("*.xyz"))
            if len(dir_list) == 0:
                controlin._print_console(
                    " controlIn - The source path ({}) has no XYZ file(s).".format(controlin.path),
                    controlin.mtype[404]
                )
                raise ValueError("controlIn - The source path ({}) has no XYZ file(s).".format(controlin.path))
            elif len(dir_list) == 1:
                controlin.path = dir_list[0]
                io.path = dir_list[0]


        if controlin.is_file():

            if not controlin.path.suffix.lower().endswith(".xyz"):
                controlin._print_console(
                    " controlIn - Not a XYZ file: {}".format(args.path),
                    controlin.mtype[404]
                )
                raise ValueError("controlIn - Not a XYZ file: {}".format(controlin.path))

            if not args.job and args.skip:

                qst = "[1 file] Generation of the 'control.in' for the '{}'.".format(controlin.path)
                query_task(qst)

            controlin.path = controlin.path.parent
            controlin.generate_controlIn(io.read(io.path), args.tier, args.level, args.charge, args.singlepoint, args.set_template, args.from_path[0])

        else:

            if not args.job and args.skip:

                qst = "[{} files] Generation of the 'control.in' for the files in the source path ({}).".format(len(dir_list), controlin.path)
                query_task(qst)

            for d in dir_list:
                controlin.path = d.parent
                controlin.generate_controlIn(io.read(d), args.tier, args.level, args.charge, args.singlepoint, args.set_template, args.from_path[0])
        
        controlin._print_console(" Generation concluded without an error.", controlin.mtype[202])

        if not args.job:
            signal.alarm(0)

    elif command == "job":

        job = Job(args.num_cores[0], args.queue_sys[0], args.path, console=True)

        job._print_console(
            "[INFO] Qcalc will generate a job file only for folders with a 'geometry.in' and 'control.in' file.",
            job.mtype[100],
            exit=False
        )

        if not args.job:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(MINUTES)

            if args.skip:
                qst = "Creating job files for the source path ({}).".format(job.path)
                query_task(qst)

        job.generate(args.batch, args.ignore_ok, args.dir_name)
        job._print_console(" All job files were generated.", job.mtype[202])
        
        if not args.job:
            signal.alarm(0)

    elif command == "analysis":

        analysis = Analysis(args.path, console=True, singlepoint=args.singlepoint, 
            table_energy=args.no_pattern)
        analysis._print_console(
            "[INFO] Qcalc will perform analysis only for folders with a 'aims.out' file.",
            analysis.mtype[100],
            exit=False
        )

        if not args.job:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(MINUTES)

        if args.s:
            if analysis.is_file():
                filename = analysis.path
                analysis.path = analysis.path.parent
            elif analysis.is_dir():
                filename = Path(args.set_name[0])

            if not args.job and args.skip:
                qst = "[1 file] A structural analysis will be make for the following file: {}.".format(analysis.path)
                query_task(qst)

            analysis.structure_analysis(filename, args.factor)
            analysis._print_console(" Structural analysis concluded.", analysis.mtype[202])
        else:

            if not args.job and args.skip:
                # Perform energy order
                qst = "This operation will make several analysis of the calculation"\
                    " results in the source path ({}).".format(analysis.path)
                query_task(qst)

            analysis.energy_order(args.nunits, args.ignore_ok, check_convergence=args.check_convergence) ## add save option
            analysis._print_console(" Analysis concluded.", analysis.mtype[202])

        if not args.job:
            signal.alarm(0)

    elif command == "plot":

        plot = Plots(args.path, console=True)
        plot._print_console(
            "[INFO] Qcalc will plot all calculations analysis.",
            plot.mtype[100],
            exit=False
        )

        if not args.job:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(MINUTES)

            if args.skip:
                qst = "This command will plot for all calculations' analysis of the" \
                " following folder: {}".format(args.path)
                query_task(qst)

        plot.plot()
        plot._print_console(" All plots were generated.", plot.mtype[202])
 
        if not args.job:
            signal.alarm(0)

    else:

        if not args.job:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(MINUTES)

            if args.skip:

                qst = "The following processes will be executed in '{}' folder:" \
                    "\n\n".format(args.path)

                cont = 1
                if not args.ignore_move:
                    qst = qst + "{}) moves the directory's files into '{}_num{}" \
                        "' folder, where 'num' is a number associated with the " \
                        "order that the files were moved\n".format(
                            cont,
                            args.prefix[0],
                            "_" + args.suffix[0].strip("_")
                        )
                    cont = cont + 1
                if not args.ignore_conversion:
                    qst += "{}) conversion of the XYZ files to geometry.in\n".format(cont)
                    cont = cont + 1
                if not args.ignore_controlin:
                    qst += "{}) generation of the control.in file\n".format(cont)
                    cont = cont + 1
                if not args.ignore_job:
                    qst += "{}) creation of the job file\n".format(cont)
                    cont = cont + 1

                query_task(qst)

        if not args.ignore_move:

            utils = Utils(args.path, console=True)
            utils.move(args.prefix[0], "_" + args.suffix[0].strip("_"), fmt=".xyz")

        if not args.ignore_conversion:

            conversor(args.path, "xyz", print_message=False, exit=False)

        if not args.ignore_controlin:


            controlin = ControlIn(args.path, console=True)
            io = IO(args.path, console=True)

            if controlin.is_dir():

                dir_list = list(controlin.path.rglob("*.xyz"))
                if len(dir_list) == 0:
                    controlin._print_console(
                        " controlIn - The source path ({}) has no XYZ file(s).".format(controlin.path),
                        controlin.mtype[404]
                    )
                    raise ValueError("controlIn - The source path ({}) has no XYZ file(s).".format(controlin.path))
                elif len(dir_list) == 1:
                    controlin.path = dir_list[0]
                    io.path = dir_list[0]


            if controlin.is_file():

                if not controlin.path.suffix.lower().endswith(".xyz"):
                    controlin._print_console(
                        " controlIn - Not a XYZ file: {}".format(args.path),
                        controlin.mtype[404]
                    )
                    raise ValueError("controlIn - Not a XYZ file: {}".format(controlin.path))

                controlin.path = controlin.path.parent
                controlin.generate_controlIn(io.read(io.path), args.tier, args.level, args.charge, args.singlepoint, args.set_template, args.from_path[0])

            else:

                for d in dir_list:
                    controlin.path = d.parent
                    controlin.generate_controlIn(io.read(d), args.tier, args.level, args.charge, args.singlepoint, args.set_template, args.from_path[0])

        if not args.ignore_job:
            
            job = Job(args.num_cores[0], args.queue_sys[0], args.path, console=True)
            job.generate(args.batch, args.ignore_ok, args.dir_name)

        if not args.job:
            signal.alarm(0)