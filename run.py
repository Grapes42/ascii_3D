#!/usr/bin/python3

"""
File: run.py

Usage: To ensure all dependencies are installed, 
and that the program is run correctly 
"""

import os
from os import name

os.system("pip install -r code/requirements.txt")

in_vs_code = 'TERM_PROGRAM' in os.environ.keys() and os.environ['TERM_PROGRAM'] == 'vscode'

if name == 'nt' or in_vs_code: # If run in windows or VS Code
    python = "python"
else: # If linux or mac
    python = "python3"

os.system(f"{python} code/main.py")