#!/usr/bin/env python
import os, sys

if len(sys.argv) == 1:
    print 'gpp: No input file'
    exit()

filename = sys.argv[1]

input_from_file = False

input_file = '~/Documents/CompetitiveProgramming/input.txt'

if len(sys.argv) >= 3:
    filename, flag = sys.argv[1:3]
    if len(sys.argv) >= 4:
        input_file = sys.argv[3]
    if flag == '-i':
        input_from_file = True

if '.' in filename:
    i = filename.rindex('.')
    name, ext = filename[:i], filename[i:]
else:
    name, ext = filename, '.cpp'

filename = name + ext

if ext == '.cpp':
    exec_file = name + '.out'

    if input_from_file:
        cmd = "g++ {0} -o {1} && ./{1} < {2}".format(filename, exec_file, input_file)
    else:
        cmd = "g++ {0} -o {1} && ./{1}".format(filename, exec_file)

elif ext == '.py':
    if input_from_file:
        cmd = "python {0} < {1}".format(filename, input_file)
    else:
        cmd = "python {0}".format(filename)

else :
    print 'gpp: {}: Invalid source file extention'.format(ext)
    exit()



# print cmd
os.system(cmd)
