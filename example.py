# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pickle
import pyCEA
import numpy as np
import subprocess,os

############################################################################
only_consider_these =  '\n e- H He Ti V O C N S Na K Fe\n'+\
                       '  H+ H- Na+ K+\n'+\
                       '  Fe(L) H2O(L)\n'

prefix = 'example'
input_pt_filename = 'input.pt'
input_mr_filename = 'input.mr'

############################################################################

# Load mixing ratios of elements:
fin = open(input_mr_filename,'r')
nameo = []
No = []
while True:
    line = fin.readline()
    if line != '':
        n,m = line.split()
        nameo.append(n)
        No.append(np.double(m))
    else:
        break

# Chech which elements we are actually going to use:
idx = pyCEA.check_elements(nameo,only_consider_these)
name = np.array(nameo)[idx]
N = np.array(No)[idx]

# Load PT profile:
P,T = np.loadtxt(input_pt_filename,unpack=True)

# Calculate chemical equilibrium:
results = {}
results['T'] = np.array([])
results['P'] = np.array([])
for i in range(len(P)):
  results['T'] = np.append(results['T'],T[i])
  results['P'] = np.append(results['P'],P[i])
  # Calculate equilibrium chemistry for each T-P point:
  only_consider_these_now = only_consider_these
  pyCEA.calcCEA(T[i],P[i],name,N,only_consider_these_now,prefix=prefix,ions=True)
  c_species,c_moles = pyCEA.readCEA(T[i],P[i],prefix=prefix)
  if i == 0:
      for j in range(len(c_species)):
          results[c_species[j]] = np.zeros(len(P))
          results[c_species[j]][i] = c_moles[j]
  else:
      for j in range(len(c_species)):
          if c_species[j] in results.keys():
              results[c_species[j]][i] = c_moles[j]
          else:
              results[c_species[j]] = np.zeros(len(P))
              results[c_species[j]][i] = c_moles[j]

# Save results to python dict:
FILE = open(prefix+'_results.pkl','w')
pickle.dump(results, FILE)
FILE.close()
