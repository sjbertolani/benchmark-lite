## Template files

Each of these folders contain the template PDB files, as well as "cleaned up" version which have alternate chains remove for ease of alignmnet algorithms

For each template, the fasta file is included, as well as an alignment file of all of the templates to the target sequences ( alignment.grishin)

Each target sequence is "trimmed" in this folder, based on removing portions of the target sequence that have 0 coverage at either the N or C termini (alignmnet.grishin.trim)

Each folder contains a files call "alignmnet.grishin.dist_csts" and "alignment.grishin.dist_csts.bb_sc" which are Robetta's program called "predict_distances_multi.pl" written by James Thompson. All of these lines are created by overlaying the template pdbs, measuring the distances between equivalent pairs of residues (equivalence is determined by the alignment file) and making a gaussian mixture model to estimate a contraint for a specific interaction. This is essentially putting rubber bands all over the structure to make sure that the structure looks like the templates.
This files is created by running
```
$ROBETTA/cm_scripts/bin/predict_distances_multi.pl alignment.grishin 1wy6.fasta  -outfile alignment.grishin.dist_csts -min_seqsep 5 -max_dist 10 -aln_format grishin -max_e_value 10000 -pdb_dir PATHTHATCONTAINSPDBS
```

Each folder contains a file called "upweighted.alignment.grishin.dist_cst" which is identical to the file above.... which the addition of 
the very last lines are the catalytic constraints. These can be created by taking a list of "catalytic residues" and a pdb structure and calculating the distances between all of the atoms. 
Each folder contains a files call "alignmnet.grishin.dist_csts" and "alignment.grishin.dist_csts.bb_sc" which are Robetta's program called "predict_distances_multi.pl" written by James Thompson. All of these lines are created by overlaying the template pdbs, measuring the distances between equivalent pairs of residues (equivalence is determined by the alignment file) and making a gaussian mixture model to estimate a contraint for a specific interaction. This is essentially putting rubber bands all over the structure to make sure that the structure looks like the templates.
The lines at the bottom of this file contain "HARMONIC" and are the *CG* constraints.
These are also "rubber bands" but with a much stronger weight and conceptual difference in that they are required for an enzyme to catalyze it's chemical reaction
