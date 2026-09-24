from __future__ import division
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import filtro_func_FIR
#Filtro de médias
# Polinomio numerador
Hn=[1/2 , 1/2.]
#Hn=[1/4. , 1/4.,1/4. , 1/4.]
#Hn=[1/6. , 1/6.,1/6. , 1/6.,1/6. , 1/6.]
# Polinomio denominador
Hd=[1.]

# Projeto Filtros FIR
Hd=[1.]
n =20

#Hn = signal.firwin(n, cutoff = 0.1, window = "boxcar") #janela retangular ate q bom
#Hn = signal.firwin(n, cutoff = 0.2, window = "triang") #janela triangular
Hn = signal.firwin(n, cutoff = 0.1, window = "hamming") #janela hamming
#Hn = signal.firwin(n, cutoff = 0.1, window = "blackman") # bom tbm
print("Numerador :",Hn)
#filtro_func_FIR.plot_impulso(Hn,Hd,n)
filtro_func_FIR.plot_bode(Hn,Hd)
#filtro_func_FIR.plot_filtro(Hn,Hd,1000)
plt.show()