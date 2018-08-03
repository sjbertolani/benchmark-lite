import sys

numtoadd = int(sys.argv[1])
filetoadd = sys.argv[2]

with open(filetoadd,'r') as fh, open(filetoadd+'.renum','w') as gh:
    for line in fh:
        if line.startswith('ATOM'):

            resnum = line[22:26]
            mylen = len(resnum)
            new = int(resnum) + numtoadd

            newline = line[:22] + '{:>4}'.format(new) + line[26:]
#            print newline
            gh.write(newline)
            
        if line.startswith('HETATM'):
            gh.write(line)
