pyCEA
-----

In order to use this, please download the original Fortran code from the NASA 
webpage: http://www.grc.nasa.gov/WWW/CEAWeb/ceaguiDownload-unix.htm. Untar the 
content of the file into a folder here and that's it! 

It is assumed the resulting folder name containing all the files is CEA+FORTRAN.

USAGE
-----

Follow the example.py code to check the usage. In there you can change the chemical 
network via the `only_consider_these` string; you can add different compounds to follow. 
In addition, a prefix for the calculation can be defined (i.e., just a name for personal use). 
Finally, you need to provide the code with two inputs:

- A file called `input.mr`, which has the mixing ratios of the elements that form the expected 
  compounds. The input.mr in this library has the solar system nebula abundances from Lodders (2003).

- A file called `input.pt`, which is a pressure-temperature profile. In this case, it is made up in order 
  for you to be able to test the code. This will calculate the equilibrium composition at 
  each P-T pair in the file.

The code makes sure everything is in order before compiling. 

OUTPUT
------

The output is a python dictionary that has the mixing ratios of the resulting compounds at 
each P-T point. At the same point, the folder CEAoutput is created which saves the actual 
outputs from CEA which are read by this program.

ACKNOWLEDGMENTS
---------------

I would like to thank Mike Line who got me started with the basics of CEA, Jonathan Fortney 
for suggesting using this for my equilibrium calculations and the Kavli Summer Program in 
Astrophysics which was the initiative that got the three of us together in order to pull this 
project forward!
