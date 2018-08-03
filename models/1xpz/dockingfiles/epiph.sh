#!/bin/bash
#SBATCH --job-name=dock4real
#SBATCH --output=logs
#SBATCH --mem 4G
#SBATCH --nodes 1
#SBATCH --time 1-0

$ROSETTA_BIN/rosetta_scripts.default.linuxgccrelease @flags -overwrite -parser:protocol docking.xml -s S_0001_36.dock.pdb -database $ROSETTA_DB -nstruct 100