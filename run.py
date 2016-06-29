import numpy as np
import subprocess,os

def checkCEA(compiler='gfortran'):
    """
    Check that all the fortran CEA codes have their 
    corresponding executables:
    """
    cwd = os.getcwd()
    os.chdir('CEA+FORTRAN')
    if not os.path.exists('FCEA2'):
        subprocess.Popen(compiler+' cea2.f -o FCEA2',shell = True).wait()
    if not os.path.exists('b1b2b3'):
        subprocess.Popen(compiler+' b1b2b3.f -o b1b2b3',shell = True).wait()
    if not os.path.exists('syntax'):
        subprocess.Popen(compiler+' syntax.f -o syntax',shell = True).wait()
    if not os.path.exists('thermo.lib'):
        p = subprocess.Popen(['./FCEA2'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_data = p.communicate(input='thermo')[0]
    if not os.path.exists('trans.lib'):
        p = subprocess.Popen(['./FCEA2'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_data = p.communicate(input='trans')[0]

    os.chdir(cwd)
    print '\t CEA up and running!'

def runCEA(filename):
    filename_no_extension = filename.split('.inp')[0]
    subprocess.Popen('cp '+filename+' CEA+FORTRAN/.',shell = True).wait()
    cwd = os.getcwd()
    os.chdir('CEA+FORTRAN')
    p = subprocess.Popen(['./FCEA2'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_data = p.communicate(input=filename_no_extension)[0]
    subprocess.Popen('mv '+filename_no_extension+'.out ../.',shell = True).wait() 
    subprocess.Popen('rm '+filename,shell = True).wait()
    os.chdir(cwd)
  
checkCEA()
runCEA('example1.inp')
