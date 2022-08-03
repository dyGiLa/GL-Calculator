from scipy.optimize import fsolve

import numpy  as np
import Module_SC_Beta_V06 as SCb


# def func(x):

#     return [4.*beta1*x[1]*x[2]**2 + 2.*(-3.*gz*h + 3.*alpha + 2.*(2.*beta1+beta2+beta3+beta5)*x[1]**2. + 2.*beta2*x[2]**2)*x[0] + 4.*(beta2+beta4)*x[0]**3,

#             6.*gz*h*x[1] + 6.*alpha*x[1] + 4.*((beta2+beta4)*x[1]**3 + beta2*x[1]*x[2]**2 + beta1*x[2]**2*x[1] + (2.*beta1+beta2+beta3+beta5)*x[1]*x[0]**2),

#             3.*gH*h**2 + 3.*alpha + 2.*((beta1+beta3+beta4+beta5)*x[2]**2 + 2.*beta1*x[1]*x[0] + beta2*(x[1]**2+x[2]**2+x[0]**2)) 
#            ]

# def func2(x):

#     return [3.*((kb*Tc)**2)*(-gzt*h+alphat)*x[0] + 2.*(beta1t*x[1]*x[2]*x[2] + ((2.*beta1t+beta2t+beta3t+beta5t)*x[1]*x[1]+beta2t*x[2]*x[2])*x[0] + (beta2t+beta4t)*x[0]*x[0]*x[0]),

#             x[1]*(3.*((kb*Tc)**2)*(gzt*h+alphat)+2.*(beta2t+beta4t)*x[1]*x[1]+2.*beta2t*x[2]*x[2]) + 2.*beta1t*x[2]*x[2]*x[0] + 2.*(2.*beta1t+beta2t+beta3t+beta5t)*x[1]*x[0]*x[0],

#             3.*gHt*h**2 + 3.*((kb*Tc)**2)*alphat + 2.*((beta1t+beta3t+beta4t+beta5t)*x[2]*x[2] + 2.*beta1t*x[1]*x[0] + beta2t*(x[1]*x[1]+x[0]*x[0]+x[2]*x[2]))
#            ]

def func3(x):

    return [3.*(-gzt*h+alphat)*x[0] + 2.*(beta1t*x[1]*x[2]*x[2] + ((2.*beta1t+beta2t+beta3t+beta5t)*x[1]*x[1]+beta2t*x[2]*x[2])*x[0] + (beta2t+beta4t)*x[0]*x[0]*x[0]),

            x[1]*(3.*(gzt*h+alphat)+2.*(beta2t+beta4t)*x[1]*x[1]+2.*beta2t*x[2]*x[2]) + 2.*beta1t*x[2]*x[2]*x[0] + 2.*(2.*beta1t+beta2t+beta3t+beta5t)*x[1]*x[0]*x[0],

            3.*(gHt*h**2)*((kb*Tc)**(-2)) + 3.*alphat + 2.*((beta1t+beta3t+beta4t+beta5t)*x[2]*x[2] + 2.*beta1t*x[1]*x[0] + beta2t*(x[1]*x[1]+x[0]*x[0]+x[2]*x[2]))
           ]


##########################################

# witch to Greywall temperature scale
SCb.turn_on_Greywall()


p = 32*SCb.bar

T = 0.88*SCb.Tcp(p)

# h = 22200*SCb.Gauss


pnoa, pnob = SCb.pno()

###########################################
###########################################

kb = SCb.kb
Tc = SCb.Tcp(p)

alphat = pnoa*SCb.alpha_td(p, T)
beta1t = pnob*SCb.beta1_td(p, T)
beta2t = pnob*SCb.beta2_td(p, T)
beta3t = pnob*SCb.beta3_td(p, T)
beta4t = pnob*SCb.beta4_td(p, T)
beta5t = pnob*SCb.beta5_td(p, T)

gzt = SCb.gz_td(p)
# gzt = 0.

gHList =  SCb.gH_td(p)
gHt = gHList[0]


###########################################

h_array = np.arange(0, 150000*SCb.Gauss, 50)

uuIni = SCb.GapB(p, T)/(kb*Tc)
ddIni = SCb.GapB(p, T)/(kb*Tc)
udIni = SCb.GapB(p, T)/(kb*Tc)

print(uuIni,ddIni,udIni)

for h in h_array:

    
      #root = fsolve(func, [uuIni, ddIni, udIni])
      root = fsolve(func3, [uuIni, ddIni, udIni])

      uuIni = root[0]
      ddIni = root[1]
      udIni = root[2]

      if (root[0]<0 or root[1]<0 or root[2]<0):
      #    print(" nagetive gaps appear, breaks")
          break

      else:
          
          print(p,',',T/Tc,',',h,',',root[0],',',root[1],',',root[2])

      
