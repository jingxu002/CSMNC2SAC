# CSMNC2SAC
transfer CSMNC format data files to SAC files
## Code
sac.py -- define the class of SAC file

readCSMNC.py -- read China Strong Motion Network Center data files,
create head and data segment of SAC file

## Data files
ua0001.dat --  a CSMNC file as an example

tmpOut.dat --  an ascii SAC file, 
to read in SAC, use the command 'r alpha tmpOut.dat' 

## Example
"file transfer procedure commands in IPython"

from sac import SAC

import numpy as np

from readCSMNC import readCSMNC

head, data = readCSMNC('ua0001.dat')

head.writeOut('tmpOut.dat', data)


## Acknowledgements
Data for this study are provided by China Strong Motion Network Centre at Institute of Engineering Mechanics, China Earthquake Administration
