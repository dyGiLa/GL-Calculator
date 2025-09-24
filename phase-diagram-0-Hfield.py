import os
import numpy as np
import matplotlib.pyplot as plt
import Module_GLSCC_calculator as gl 

# line width
LineWidth=3.5

# plot marker sizes
s=[50, 70, 90, 110]

# PCP pressure & Tc
p_PCP = 21.248227 # bar
Tc_PCP = gl.Tcp_mK(p_PCP)

# pressure lists
p_arr1 = np.linspace(0, p_PCP, 700, endpoint=False)
p_arr2 = np.linspace(p_PCP, 34, 300)
# print(p_arr1[-1], p_arr2[0])
p_arr = np.concatenate((p_arr1, p_arr2))

# Evaluate TAB(p) and Tc(p)
TAB_arr = np.array([gl.TAB_mK(p) if p >= p_PCP else np.nan for p in p_arr])
Tc_arr = np.array([gl.Tcp_mK(p) for p in p_arr])

# phase diagram at 0 H-field
fig, ax = plt.subplots(1,1,figsize=(8, 6));
ax.plot(TAB_arr, p_arr, linewidth=LineWidth, label=fr'$T_{{AB}}$', color='blue')
ax.plot(Tc_arr, p_arr, linewidth=LineWidth, label=fr'$T_{{C}}$', color='red')
ax.scatter(Tc_PCP, p_PCP, marker='o', s=s[0], color='black', label=r'PCP', zorder=3)

ax.set_xlabel(r'$T/mK$',fontsize = 26.0)
ax.set_ylabel(r'$p/bar$',fontsize = 26.0)
ax.set_xlim(0.0, 3.0) # mK   
ax.set_ylim(0.0, 34) # bar
ax.tick_params(axis='both', which='both', labelsize=20)
ax.set_title(r'$p$-wave Superfluid $^3$He GL model Phase Diagram $H=0$')

# fill normal, A- and B- as ground state region
mask_p_less = p_arr < p_PCP
mask_p_larger = p_arr >= p_PCP

mask_TAB = mask_p_larger & ~np.isnan(TAB_arr) # element-wise and

mask_A_ground_state = (Tc_arr > TAB_arr) & mask_TAB
T_Bphase = np.concatenate((Tc_arr[mask_p_less], TAB_arr[mask_TAB]))

ax.fill_betweenx(p_arr, Tc_arr, TAB_arr,
    where=(mask_A_ground_state),
    facecolor='red', alpha=0.3, interpolate=True, label='A-phase'
)

ax.fill_betweenx(p_arr, 0, T_Bphase,
                  color='green', alpha=0.3, label='B-phase'
)

ax.fill_betweenx(p_arr, Tc_arr, 3.0,
                  color='orange', alpha=0.3, label='Normal-phase'
)


ax.legend(prop={'size': 12}, loc='lower right')
fig.subplots_adjust(left=0.15, bottom=0.15)  # space for labels

plt.show()

# save PD to local
plot_name = 'PD-0H-field.png'
output_path = os.path.join('./', plot_name)            
fig.savefig(output_path, dpi=300, pad_inches=0.01)

plt.close(fig)
