#!/bin/bash
#SBATCH --job-name=dock4real
#SBATCH --output=logs
#SBATCH --mem 25G
#SBATCH --nodes 1
#SBATCH --time 4-0

$ROSETTA_BIN/rosetta_scripts.default.linuxgccrelease @flags -overwrite -parser:protocol docking.xml -s S_0001_1.dock.pdb -database $ROSETTA_DB -nstruct 100