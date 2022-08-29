""" dunestyle.py (matplotlib edition): DUNE plot style tools for use with matplotlib.

This module simply imports the style defined in the C++ header version of the style.
By default it will be enabled immediately on import.

If you do not want it enabled on import, set the global:
```
import builtins  #  this only works with Python3...
builtins.__dict__["DUNESTYLE_ENABLE_AUTOMATICALLY"] = False
import dunestyle
```
Then you can call dunestyle.enable() to turn it on.

:author: J. Wolcott <jwolcott@fnal.gov>
:date:   March 2022
"""

import os
from matplotlib import pyplot as plt

def enable():
    #assert "dune" in plt.style.available, "Can't locate DUNE matplotlib style sheet file!"

    #plt.style.use("dune")

    plt.style.use('{:s}/matplotlib/stylelib/dune.mplstyle'.format(os.environ['DUNEPLOTSTYLE_DIR']))

    print("DUNE plot style enabled")


import builtins
_IMPORT_FLAG_NAME = "DUNESTYLE_ENABLE_AUTOMATICALLY"
if _IMPORT_FLAG_NAME not in builtins.__dict__ or builtins.__dict__[_IMPORT_FLAG_NAME]:
    enable()


##########   Utility functions below  ################

def WIP(transform=None):
    plt.text(0, 1.05, r"DUNE Work In Progress",
	     fontdict={"fontsize": 24, "color": "blue"},
	     transform=transform if transform is not None else plt.gca().transAxes)

def Simulation(transform=None):
    plt.text(1.0, 1.05, r"DUNE Simulation", horizontalalignment='right',
	     fontdict={"fontsize": 18, "color": "gray"},
	     transform=transform if transform is not None else plt.gca().transAxes)

def SimulationSide(transform=None):
    plt.text(1.05, 0.5, r"DUNE Simulation", rotation=270, verticalalignment='center',
	     fontdict={"fontsize": 18, "color": "gray"},
	     transform=transform if transform is not None else plt.gca().transAxes)
