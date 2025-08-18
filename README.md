## GL Calculator

Python interfaces for quantities of strong coupling corrected p-wave Ginzburg-Landau model.

---
### Using Examples
Import `GL Calculator` module 
```shell
~$ python3
...
>>> import Module_GLSCC_calculator as gl
>>> dir(gl) # checkout APIs & attributes
```

Computing `gap A-phase` and `gap B-phase` at `p=25 bar`, `T/T_c= 0.7`:
```shell
>>> gl.gapA(25, 0.7)
>>> gl.gapB(25, 0.7)
```

Checkout `T_c` and `T_AB` at `25 bar`:
```shell
>>> gl.Tcp_mK(25)
>>> gl.TAB_mK(25)
```