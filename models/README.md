For each target, these folders contain the files need to run homology modeling.

This includes

a folder called **model"** which contains the target sequence (trimmed), the evolutionary constraints (alignmnet.grishin.dist_csts.BB_SC.CA)
a submission script (SLURM), Rosetta flags files, Rosetta scripts xml protocol file, and weights for the Hybridize mover

a folder called **cgaddmodel** which contains the same, with the change of alignment.grishin.dist_csts.CA for upweighted.alignment.grishin.trim.ist_csts
You can easily see the CG constraints by diffing this file with the one in the ./model folder.

a folder called **dockingfile** which contain a docking submission script, a flags file, a header file that must be included for the enzyme design constraints
and a docking xml protocol. In this protocol, the startfrom coords must be replaced with the average XYZ position of the catalytic residues for taht model being used as input
