#!/usr/bin/python

#usage python script <mol2 file of conformers> <file of structure onto which to align>
import sys, os
from pymol import cmd
import re

def pair_fit_command(rot_name, min_name):
    ### This is the line you have to currently edit. Edit the atoms (the first atom is in the movable confs, the second is to the pdb template name)
    ## Note, if you want more or less than 4, edit the rot_name,min_name to match
    ## This should eventually take the conf and template, allow you to select in pymol the atoms to overlay and just simple loop over all states, for another time
    cmd.do("pair_fit %s and name C2, %s and name C2,  %s and name C3, %s and name C3,  %s and name C4, %s and name C4,  %s and name C5, %s and name C5"  %(rot_name,min_name,rot_name,min_name,rot_name,min_name,rot_name,min_name))


#this loads the conf mol, splits into states, saves as pdbs and clears everything that was loaded.

def load_file_conformers(file):
    print "Reading File and splitting \n"
    mobileStructurePath = os.path.abspath(file)
    mobileStructureName = mobileStructurePath.split('/')[-1].split('.')[0]
    cmd.load(file)
    cmd.do("split_states %s" %mobileStructureName)
    cmd.delete("mobileStructureName")
    list=cmd.get_names("all")
    for x in list:
        cmd.save("%s.pdb" %x,x)
    cmd.do("reinitialize")
    try:
        list.remove(mobileStructureName)
        print "Successfully remove the conf object from pymol "
    except:
        print "Oops, couldn't remove the conf object, blame your programmer ;) or buy him beer to fix it  "
    for x in list:
        cmd.load("%s.pdb" %x)
    return list

def pair_fit_and_save(min,rot_file_name,rot_name):
    minStructurePath = os.path.abspath(min)
    min_name = minStructurePath.split('/')[-1].split('.')[0]
    cmd.load(min)
    cmd.load(rot_file_name)
    print "Working on %s" %rot_name

    pair_fit_command(rot_name,min_name)

    new_name= "%s_overlayed.pdb" %rot_name
    cmd.save(new_name,rot_name,state=-1)
    print "Saving overlayed structure %s" % new_name
    cmd.delete(rot_name)
    cmd.delete(min_name)

def align_overlay( confs, template_pdb ):
    file = confs
    min = template_pdb
    print "Setting {} as the template file and using {} to get the different conformations ".format(min,file)

    name_list=load_file_conformers(file)
    for i in name_list:
        print "\n\n Working on pairfitting %s to the template \n" %i
        rot_file_name = "%s.pdb" %i
        pair_fit_and_save(min,rot_file_name,i)

cmd.extend("align_overlay",align_overlay)
align_overlay( sys.argv[1], sys.argv[2] )
