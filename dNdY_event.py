import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import sys

#import sympy as sym

#load the particle list
#particle_list = pd.read_csv(sys.argv[1], sep='\t')
particle_list = np.loadtxt('results/samples_-2212.dat', skiprows=0)
#mcid = particle_list[:,0]

#spacetime info
#tau = particle_list[:,1]
#x   = particle_list[:,2]
#eta = particle_list[:,3]
#momentum info

px = particle_list[:,0]
py = particle_list[:,1]
pz = particle_list[:,2]
E  = particle_list[:,3]

#mcid = particle_list['mcid']

#spacetime info 
#tau = particle_list['tau']
#x   = particle_list['x']
#eta = particle_list['eta']
#momentum info 
#E  = particle_list['E']
#px = particle_list['px']
#py = particle_list['py']
#pz = particle_list['pz']

######################################
######################################

#def dNchdeta(fname):
    #dat = np.loadtxt( 'build/pmag_for_pion.dat', skiprows=1)
    #    dat = pd.read_csv(fname, skiprows=1, header=None, \
#                     sep=' ', dtype = float).values
                      #                      E = dat[:,0]
                      #                      px = dat[:,1]
                      #                      py = dat[:,2]
                      #                      pz = dat[:,3]
                      #                      Yi = dat[:,4]
p = []
eta = []

for i in range(1, len(px)):
    pp = np.sqrt(px[i]*px[i] + py[i]*py[i] + pz[i]*pz[i])
    p.append(pp)
    YY = 0.5*np.log((pp+pz[i])/(pp-pz[i]))
    eta.append(YY)

dNch, Y = np.histogram(eta, bins=60)
dY = (Y[1:]-Y[:-1])
Y = 0.5*(Y[:-1]+Y[1:])
nev = 100000
dNchdY = dNch/(dY*float(nev))

#Y2, dNdY_23decay = get_dNdY(fname='~/data/auau200_results/ideal/cent20_25_etas0p00/cent20_25_event0/mc_particle_list.dat')

plt.plot(Y, dNchdY)
    
#fig, ax = plt.subplots(1,1)
    #dndy_smooth_R = np.loadtxt('event_ideal/dNdEta_Charged.dat')
    #sm0, = ax.plot(dndy_smooth_R[:, 0], dndy_smooth_R[:,1], 'm-', label='smooth 234body')
    
#mc0, = ax.plot(Y2, dNdY_23decay, 'rd', label='mc 23-body')
    
#ax.set_xlabel('Y')
#ax.set_ylabel(r'$dN/dY\ for\ charged$')
    
#smash_style.set()
#ax.legend(loc='best')
    
#plt.subplots_adjust(left=0.1, bottom=0.15, top=0.96, right=0.96)
plt.show()

