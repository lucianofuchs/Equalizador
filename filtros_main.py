from __future__ import division
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import filtros_funcoes

"""
20 - 20k hz
4 bandas

20 - 260 hz baixos

240 - 2,1k hz baixos medios

1,9k - 6,1k hz altos medios

5,9k - 20k hz agudos

slider de atenuação para cada banda

"""

# Projeto Filtros IIR
#[Hn,Hd]=iirdesign(wp, ws, gpass, gstop, analog=False, ftype='ellip', output='ba', fs=None)[source]
# frequecia normalizada 1 -> fN (frequencia de Nyquist)
# wp - banda passagem
# wp - banda rejeição
# gpass - ganh banda passagem
# ganho banda rejeição
# ftype - filter type
# Butterworth : ‘butter’
# Chebyshev I : ‘cheby1’
# Chebyshev II : ‘cheby2’
# Cauer/elliptic: ‘ellip’
# output - formato da saida
# second-order sections (recommended): ‘sos’
# numerator/denominator (default) : ‘ba’
# pole-zero : ‘zpk’
#
#Filtro Passa-banda
#wp=[0.4,0.6]
#ws=[0.3, 0.8]
wp=.3
ws=.5
#[Hn,Hd]=signal.iirdesign(wp,ws, 1, 60, ftype='ellip')
#[Hn,Hd]=signal.iirdesign(wp,ws, 1, 60, ftype='cheby2')
[Hn,Hd]=signal.iirdesign(wp,ws, 1, 60, ftype='cheby1')
#[Hn,Hd]=signal.iirdesign(wp,ws, 1, 60, ftype='butter')
print("Numerador:",Hn)
print("Denominador:",Hd)
#Resposta ao impulso
filtros_funcoes.plot_impulso(Hn,Hd,80)
filtros_funcoes.plot_bode(Hn,Hd)
#Resposta ao impulso
#filtros_funcoes.plot_impulso(Hn,Hd,100)
plt.show()