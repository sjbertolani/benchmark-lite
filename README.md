# To go along with paper.

This is the "light" version of the benchmark dataset. This does not include fragments. You can either a) make your own using Robetta or b) remove the call for custom fragments

**crystaldock** Contains files needed to dock the ligand into the crystal structure. This is used to verify the ability of the enzyme constraint files to recover the binding mode consistent with the chemistry of the mechanism

**docking** Contains files that define the ligand for docking, including a template docking XML script, the param files needed for Rosetta to understand the ligand atoms, enzyme design constraint files that encode the enzyme mechanism chemistry, and conformation libraries for each ligand.

**homologoussequences** Contains the similar sequence searches used to identify the templates for modeling each target. Includes alignments of everything, as well as filtered alignments with the sequences closer than 80% removed

**ligandmaps** Contains the mappings from the Rosetta - params ligand atom numbering to the PDB structure ligand numbering. Used in analysis of ligand rmsd

**lowenergy** Contains all of the +CG and -CG low energy models shown in docking analysis

**models** contains all the files needed to run homology modeling and ligand docking, inlcuding the CG constraints, the XML files, the flags files, the input sequences, etc.

**pdbstructures** Contain the PDB structures, inlcuding version that are only 1 chain, waters remove, other ligands removed, renumbered, 

**sequences** Contain the original target sequences

**structuralinfo** Contain mappings for the catalytic residues from the PDB structure to the templates

**templates** Contain alignments, threaded models, and evolutionary constraints.


