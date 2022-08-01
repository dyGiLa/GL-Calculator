from scipy.optimize import fsolve

import numpy  as np
import Module_SC_Beta_V06 as SCb

import matplotlib.pyplot as plt
import Module_B2Gaps_PHA as B2gaps


##########################################

# witch to Greywall temperature scale
SCb.turn_on_Greywall()


p = 32*SCb.bar

T = 0.88*SCb.Tcp(p)


###########################################

h_array = np.arange(0,500000*SCb.Gauss, 50)
# print(np.shape(h_array))

fA2_array = np.array([])
fB2_array = np.array([])
fPlanar_array = np.array([])
fA1_array = np.array([])

Duu2A1_B2Like_array = np.array([])
Duu2A1_A2Like_array = np.array([])

Duu2A2_array = np.array([])
Ddd2A2_array = np.array([])


Duu2Planar_array = np.array([])
Ddd2Planar_array = np.array([])


Duu2B2_array = np.array([])
Ddd2B2_array = np.array([])
Dud2B2_array = np.array([])



for h in h_array:

    gaps2A1_all = SCb.GapA1(p, T, h)

    gaps2A2 = SCb.GapA2(p, T, h)

    gaps2Planar = SCb.GapPlanar(p, T, h)

    gaps2B2_noPHA = SCb.GapB2_noPHA(p, T, h)


    fA1 = SCb.fA1(p, T, h)
    
    fA2 = SCb.fA2(p, T, h)

    fPlanar = SCb.fPlanar(p, T, h)

    fB2_noPHA = SCb.fB2_noPHA(p, T, h)

    

    Duu2A1_B2Like_array = np.append(Duu2A1_B2Like_array, gaps2A1_all[0])
    Duu2A1_A2Like_array = np.append(Duu2A1_A2Like_array, gaps2A1_all[1])

    fA1_array = np.append(fA1_array, fA1)

    if (gaps2A2[0]<0 or gaps2A2[1]<0):

      Duu2A2_array = np.append(Duu2A2_array, np.nan)
      Ddd2A2_array = np.append(Ddd2A2_array, np.nan)

      fA2_array = np.append(fA2_array, np.nan)
    else:
      Duu2A2_array = np.append(Duu2A2_array, gaps2A2[0])
      Ddd2A2_array = np.append(Ddd2A2_array, gaps2A2[1])

      fA2_array = np.append(fA2_array, fA2)
      

    if (gaps2Planar[0]<0 or gaps2Planar[1]<0):
      Duu2Planar_array = np.append(Duu2Planar_array, np.nan)
      Ddd2Planar_array = np.append(Ddd2Planar_array, np.nan)

      fPlanar_array = np.append(fPlanar_array, np.nan)
      
    else:
      Duu2Planar_array = np.append(Duu2Planar_array, gaps2Planar[0])
      Ddd2Planar_array = np.append(Ddd2Planar_array, gaps2Planar[1])

      fPlanar_array = np.append(fPlanar_array, fPlanar)
        
      
    if (gaps2B2_noPHA[0]<0 or gaps2B2_noPHA[1] or gaps2B2_noPHA[2]):

        Duu2B2_array = np.append(Duu2B2_array, np.nan)
        Ddd2B2_array = np.append(Ddd2B2_array, np.nan)
        Dud2B2_array = np.append(Dud2B2_array, np.nan)

        fB2_array = np.append(fB2_array, np.nan)
    else:
        Duu2B2_array = np.append(Duu2B2_array, gaps2B2_noPHA[0])
        Ddd2B2_array = np.append(Ddd2B2_array, gaps2B2_noPHA[1])
        Dud2B2_array = np.append(Dud2B2_array, gaps2B2_noPHA[2])

        fB2_array = np.append(fB2_array, fB2_noPHA)



Duu2A1_B2Like_array = Duu2A1_B2Like_array*((SCb.kb*SCb.Tcp(p))**(-2))
Duu2A1_A2Like_array = Duu2A1_A2Like_array*((SCb.kb*SCb.Tcp(p))**(-2))

Duu2A2_array = Duu2A2_array*((SCb.kb*SCb.Tcp(p))**(-2))
Ddd2A2_array = Ddd2A2_array*((SCb.kb*SCb.Tcp(p))**(-2))

Duu2Planar_array = Duu2Planar_array*((SCb.kb*SCb.Tcp(p))**(-2))
Ddd2Planar_array = Ddd2Planar_array*((SCb.kb*SCb.Tcp(p))**(-2))

Duu2B2_array = Duu2B2_array*((SCb.kb*SCb.Tcp(p))**(-2))
Ddd2B2_array = Ddd2B2_array*((SCb.kb*SCb.Tcp(p))**(-2))
Dud2B2_array = Dud2B2_array*((SCb.kb*SCb.Tcp(p))**(-2))


################################################################

fB2_PHA = SCb.fB2_PHA(p, T, B2gaps.hArray, B2gaps.DuuArray, B2gaps.DddArray, B2gaps.DudArray)
# print(" got fB2_PHA array!! ")

################################################################


fig1, ax1 = plt.subplots(1,1)

# print(np.shape(Duu2A2_array))

# ax1.plot(h_array,np.sqrt(Duu2A2_array),'b-', h_array,np.sqrt(Ddd2A2_array),'r-',h_array,np.sqrt(Duu2Planar_array),'g-.',h_array,np.sqrt(Ddd2Planar_array),'c-.',h_array,np.sqrt(Duu2B2_array),'m--',h_array,np.sqrt(Ddd2B2_array),'k--',h_array,np.sqrt(Dud2B2_array),'y--')

ax1.plot(h_array,np.sqrt(Duu2A1_B2Like_array),'b:',h_array,np.sqrt(Duu2A1_A2Like_array),'r:',h_array,np.sqrt(Duu2A2_array),'b-', h_array,np.sqrt(Ddd2A2_array),'r-',h_array,np.sqrt(Duu2Planar_array),'g-.',h_array,np.sqrt(Ddd2Planar_array),'c-.',B2gaps.hList,B2gaps.DuuArray,'m--',B2gaps.hList,B2gaps.DddArray,'k--',B2gaps.hList,B2gaps.DudArray,'y--')

ax1.grid()


fig2, ax2 = plt.subplots(1,1)

# ax2.plot(h_array,fA2_array,'b-', h_array,fPlanar_array,'r-.',h_array,fB2_array,'g--', )
ax2.plot(h_array,fA1_array,'m:',h_array,fA2_array,'b-', h_array,fPlanar_array,'r-.',B2gaps.hList,fB2_PHA,'g--')

ax2.grid()


fig3, ax3 = plt.subplots(1,1)

ax3.plot(h_array,fA1_array,'m:',h_array,fA2_array,'b-', h_array,fPlanar_array,'r-.')

ax3.grid()



plt.show()
