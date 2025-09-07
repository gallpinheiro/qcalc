from .qcalc import Qcalc
from pathlib import Path
from numpy import array_split, ceil


class Job(Qcalc):

    def __init__(self, n_cores, queue_sys, path=Path.cwd(), console=False):
        super(Job, self).__init__(path, console=console)
        self.n_cores = n_cores  # Number of cores
        self.queue_sys = queue_sys  # Queue system type. Possible arguments are "longq", "workq", and "shortq"

        self.process = {
            "longq": {20: "120:00:00", 40: "120:00:00"},
            "workq": {10: "48:00:00", 20: "48:00:00"},
            "shortq": {8: "1:00:00"}
        }

        if not isinstance(self.n_cores, int):
            msg = "job - required field 'n_cores' is not an int."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        if not isinstance(self.queue_sys, str):
            msg = "job - required field 'queue_sys' is not a str."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise TypeError(msg)

        if self.queue_sys not in self.process.keys():
            msg = "job - required field 'queue_sys' received an invalid queue system."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise ValueError(msg)

        if self.n_cores not in self.process[self.queue_sys].keys():
            msg = "job - required field 'n_cores' received an invalid value for the selected queue system."
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise ValueError(msg)

        if self.is_file():
            msg = "job - required field 'path' is a file: {}".format(self.path)
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise ValueError(msg)

        self.n_hours = self.process[self.queue_sys][self.n_cores]  # Number of hours

    def update(self, qcalc_obj):
        self.__dict__.update(qcalc_obj.__dict__)

    def job_to_file(self, folder_name):
        """
        Generate the job file.
        """

        pbs = ""
        if folder_name:
            pbs = "#PBS -N {}".format(self.path.name) 
 
        bash_file = """#!/bin/bash

#PBS -S /bin/bash
#PBS -l nodes=1:ppn={},walltime={}
#PBS -V
#PBS -j oe
#PBS -q {}
{}

# Number of cores (should be the same as (nodes * ppn))
NNODES={}

# Setup environment so that FHI-aims works correctly.
ulimit -s unlimited
source /opt/intel/bin/compilervars.sh intel64
source /opt/intel/bin/iccvars.sh intel64
source /opt/intel/bin/ifortvars.sh intel64
source /opt/intel/compilers_and_libraries/linux/mkl/bin/mklvars.sh intel64
source /opt/intel/impi/2019.6.166/intel64/bin/mpivars.sh
export I_MPI_PIN_DOMAIN=auto
export I_MPI_PIN_PROCS=all
export I_MPI_PERHOST=all
export I_MPI_DEBUG=10
export OMPI_FC=ifort
export I_MPI_F77=ifort
export I_MPI_F90=ifort
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export MKL_DYNAMIC=FALSE
export I_MPI_FABRICS=shm
cd $PBS_O_WORKDIR

# FHI-aims executable
AIMSBIN=/dados/softwares/fhi-aims/aims.071914_7.scalapack.mpi.x

# Name of output file -- stdout data written by FHI-aims will be here
OUTFILE=aims.out

printf "################################################\\n";
printf "Current time is: `date`\\n";
printf "Current PBS work directory is: $PBS_O_WORKDIR\\n";
printf "Current PBS queue is: $PBS_O_QUEUE\\n";
printf "Current PBS job ID is: $PBS_JOBID\\n";
printf "Current PBS job name is: $PBS_JOBNAME\\n";
printf "This jobs will run on the following ($NNODES) processors:\\n";
printf "MPI Fabric: $I_MPI_FABRICS:\\n";
#echo `cat $PBS_NODEFILE`

TBEGIN=`echo "print time();" | perl`

# Command to run
mpirun -machinefile $PBS_NODEFILE -np $NNODES $AIMSBIN > $OUTFILE
TEND=`echo "print time();" | perl`

printf "#################################################\\n";
printf "+++ Job finished: `date`\\n"
printf "+++ Job walltime: `expr $TEND - $TBEGIN`\\n"
printf "#################################################\\n";""".format(
        self.n_cores, self.n_hours, self.queue_sys, pbs, self.n_cores)

        with open(str(self.path / "job"), "w") as file:
            file.write(bash_file)


    def job_to_files(self, folders_list, counter, folder_name):
        """
        Generate the job all file.

        Parameters
        ----------
        folders: str
            String with all calculation folders name.
        counter: int
            suffix for the job file name.
        """

        pbs = ""
        if folder_name:
            if counter > 0:
                pbs = "#PBS -N {}_{}".format(self.path.name, counter)
            else:
                pbs = "#PBS -N {}".format(self.path.name) 

        bash_file = """#!/bin/bash
#PBS -S /bin/bash
#PBS -l nodes=1:ppn={},walltime={}
#PBS -V
#PBS -m e
#PBS -j oe
{}

# Number of cores (should be the same as (nodes * ppn))
export NNODES={}

# Setup environment so that FHI-aims works correctly.
source /opt/intel/bin/compilervars.sh intel64
source /opt/intel/bin/iccvars.sh intel64
source /opt/intel/bin/ifortvars.sh intel64
source /opt/intel/compilers_and_libraries/linux/mkl/bin/mklvars.sh intel64
source /opt/intel/impi/2019.6.166/intel64/bin/mpivars.sh
export OMPI_FC=ifort
export I_MPI_F77=ifort
export I_MPI_F90=ifort
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export MKL_DYNAMIC=FALSE
export I_MPI_FABRICS=shm
cd $PBS_O_WORKDIR

# FHI-aims executable
export AIMSBIN=aims.071914_7.scalapack.mpi.x

# Name of output file -- stdout data written by FHI-aims will be here
export OUTFILE=aims.out

printf "################################################\\n";
printf "Current time is: `date`\\n";
printf "Current PBS work directory is: $PBS_O_WORKDIR\\n";
printf "Current PBS queue is: $PBS_O_QUEUE\\n";
printf "Current PBS job ID is: $PBS_JOBID\\n";
printf "Current PBS job name is: $PBS_JOBNAME\\n";
printf "This jobs will run on the following ($NNODES) processors:\\n";

export TBEGIN=`echo "print time();" | perl`

namepath=({})
dirbegin=()
dirend=()

for dir in "${{namepath[@]}}"; do
  if [ -d $dir ]
  then
     echo found $dir
     cd $dir
     [ -f HERE ] && rm -rf HERE
     [ -f aims.out ] &&  rm -rf aims.out
     echo "I am HERE" > HERE
     dirbegin+=(`echo "print time();" | perl`)
     mpirun -machinefile $PBS_NODEFILE -np $NNODES /dados/softwares/fhi-aims/$AIMSBIN > $OUTFILE
     dirend+=(`echo "print time();" | perl`)
     [ -f HERE ] && rm -rf HERE
     cd ..
  fi
done

export TEND=`echo "print time();" | perl`

printf "#################################################\\n";
for ((i=0; i<${{#namepath[@]}}; ++i)); do
    printf "+++ Job walltime of ${{namepath[i]}}: `expr ${{dirend[i]}} - ${{dirbegin[i]}}` seconds\\n"
done
printf "+++ General Information\\n"
printf "+++ Job finished: `date`\\n"
printf "+++ Job walltime: `expr $TEND - $TBEGIN`\\n"
printf "#################################################\\n";""".format(
            self.n_cores, self.n_hours, pbs, self.n_cores, folders_list)
        
        if counter > 0:
            output = "job_all_{}".format(counter)
        else:
            output = "job_all"

        with open(str(self.path / output), "w") as file:
            file.write(bash_file)

    def generate(self, batch=-1, ignore_ok=False, folder_name=False):
        """
        Generate the job file.
        
        batch: int, default -1
            create job files with a maximum of calculations equal to the batch.
        ignore_ok: bool, default False
            If True, a job will be create for the folders with 'OK' at its name.
        folder_name: bool, default False
            Set the folder name in the name of the job file.
        """
        aux = []
        for elem in self.retrv(constraints=["geometry.in", "control.in"], relative=False):
            if not ignore_ok and elem.name.lower().endswith("_ok"):
                msg = " job - '{}' contains '_OK' at the end. Try to use the " \
                "--ignore-ok argument to create a job file for this folder.".format(elem)
                self._print_console(msg, self.mtype[406], exit=False)
            else:
                aux.append(elem)

        aux = sorted(aux)

        if len(aux) == 0:
            msg = "job - The source path ({}) has no folder(s) to create the job file(s).".format(self.path)
            self._print_console(self.alert[405](msg), self.mtype[405])
            raise ValueError(msg)
        elif len(aux) == 1:
            self.path = aux[0]
            self.job_to_file(folder_name)
        else:
            # Batch
            batch = float(len(aux)) / float(batch)
            batch = int(ceil(batch)) if (batch - int(batch)) >= 0.5 else int(batch)

            if batch > 0:
                start=0
                arr_splited = array_split(aux, batch)
            else:
                start = -2  # this will generate a counter = -1 for the job_to_files
                arr_splited = [aux]

            for counter, b in enumerate(arr_splited, start=start): 
                arr = ""
                for filename in b:
                    arr += "\"{}\"\n".format(filename)

                counter += 1
                self.job_to_files(arr, counter, folder_name)