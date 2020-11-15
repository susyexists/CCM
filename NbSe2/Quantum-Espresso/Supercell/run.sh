#!/bin/bash
source ~/intel/parallel_studio_xe_2020.2.108/bin/psxevars.sh 

mpirun -np 44 ~/Downloads/q-e/bin/pw.x -inp 1-scf.in > 1-scf.out 
echo "scf is done"
#mpirun -np 44 ~/Downloads/q-e/bin/pw.x -inp 1-nscf.in > 1-nscf.out 
#echo "nscf is done"
mpirun -np 44 ~/Downloads/q-e/bin/pw.x -inp 2-bands.in > 2-bands.out
echo "band is done"
mpirun -np 44 ~/Downloads/q-e/bin/bands.x -inp 3-bands_pp.in > 3-bands_pp.out 
echo "post processing is done"
