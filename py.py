#!/usr/bin/env python

import os, sys

filepath = sys.argv[1]

path = filepath.split('/')
if path[-1].endswith('.py'):
	path[-1] = path[-1][:-3]

cmd = 'python -m {}'.format('.'.join(path))
print (cmd)
os.system(cmd)
