"""
executable python script for starting a train3dunet session on UZH's ScienceCluster
creation date (dd.mm.yyyy): 30.01.2024
Daniel Walther
"""

import sys
import os

print(f"input arguments: {sys.argv[:]}")  # element 0 is the script's file path relative to the terminal session's working directory

train_config = sys.argv[1]
if not os.path.exists(train_config):
	print(f"Could not find {train_config}")
	sys.exit(1)

