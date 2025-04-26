from sys import path
import os

# Adds the absolute location of context.py to sys.path list, for importing myshell modules
path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mycommands, myprograms, myutils
