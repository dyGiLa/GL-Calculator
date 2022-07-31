from scipy.optimize import fsolve

import numpy  as np
import Module_SC_Beta_V06 as SCb

import matplotlib.pyplot as plt


##########################################

# witch to Greywall temperature scale
SCb.turn_on_Greywall()


p = 32*SCb.bar

T = 0.88*SCb.Tcp(p)


###########################################

h_array = np.arange(0, 50000*SCb.Gauss, 5)
print(np.shape(h_array))

fA2_array = np.zeros(np.shape(h_array))
fB2_array = np.zeros(np.shape(h_array))
fplanar_array = np.zeros(np.shape(h_array))

Duu2A2_array = np.array([])
Ddd2A2_array = np.array([])


Duu2Planar_array = np.array([])
Ddd2Planar_array = np.array([])


Duu2B2_array = np.array([])
Ddd2B2_array = np.array([])
Dud2B2_array = np.array([])

for h in h_array:

    gaps2A2 = SCb.GapA2(p, T, h)

    gaps2Planar = SCb.GapPlanar(p, T, h)

    gaps2B2_noPHA = SCb.GapB2_noPHA(p, T, h)


    Duu2A2_array = np.append(Duu2A2_array, gaps2A2[0])
    Ddd2A2_array = np.append(Ddd2A2_array, gaps2A2[1])

    Duu2Planar_array = np.append(Duu2Planar_array, gaps2Planar[0])
    Ddd2Planar_array = np.append(Ddd2Planar_array, gaps2Planar[1])

    Duu2B2_array = np.append(Duu2B2_array, gaps2B2_noPHA[0])
    Ddd2B2_array = np.append(Ddd2B2_array, gaps2B2_noPHA[1])
    Dud2B2_array = np.append(Dud2B2_array, gaps2B2_noPHA[2])

    

Duu2A2_array = Duu2A2_array*((SCb.kb*SCb.Tcp(p))**(-2))
Ddd2A2_array = Ddd2A2_array*((SCb.kb*SCb.Tcp(p))**(-2))

Duu2Planar_array = Duu2Planar_array*((SCb.kb*SCb.Tcp(p))**(-2))
Ddd2Planar_array = Ddd2Planar_array*((SCb.kb*SCb.Tcp(p))**(-2))

Duu2B2_array = Duu2B2_array*((SCb.kb*SCb.Tcp(p))**(-2))
Ddd2B2_array = Ddd2B2_array*((SCb.kb*SCb.Tcp(p))**(-2))
Dud2B2_array = Dud2B2_array*((SCb.kb*SCb.Tcp(p))**(-2))


################################################################


fig, ax = plt.subplots(1,1)

print(np.shape(Duu2A2_array))

ax.plot(h_array,Duu2A2_array,'b-', h_array,Ddd2A2_array,'r-',h_array,Duu2Planar_array,'g-.',h_array,Ddd2Planar_array,'c-.',h_array,Duu2B2_array,'m--',h_array,Ddd2B2_array,'k--',h_array,Dud2B2_array,'y--')

ax.grid()
plt.show()
