#!/bin/bash
#SBATCH --job-name=dock4real
#SBATCH --output=logs
#SBATCH --mem 4G
#SBATCH --nodes 1
#SBATCH --time 1-0

/home/bertolan/rosetta_new/Rosetta/main/source/bin/rosetta_scripts.default.linuxgccrelease @flags -overwrite -parser:protocol docking.xml -s 1eh5.dock.pdb -nstruct 20

#$ROSETTA_BIN/rosetta_scripts.default.linuxgccdebug @flags -overwrite -parser:protocol docking.xml -s 1eh5.dock.pdb -database $ROSETTA_DB -nstruct 100
