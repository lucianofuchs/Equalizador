# Usando python + numpy + signal como ferramenta de projeto
# funções auxiliares - diagrama de bode / resposta impulsiva / filtragem
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi, angle


class _Signal:
    @staticmethod
    def freqz(num, den=(1,), worN=512):
        """Return the digital filter frequency response using NumPy."""
        w = np.linspace(0, pi, worN, endpoint=False)
        num = np.asarray(num, dtype=float)
        den = np.asarray(den, dtype=float)
        k_num = np.arange(num.size)
        k_den = np.arange(den.size)
        h_num = np.exp(-1j * np.outer(w, k_num)) @ num
        h_den = np.exp(-1j * np.outer(w, k_den)) @ den
        return w, h_num / h_den

    @staticmethod
    def lfilter(num, den, x):
        """Apply a causal digital filter using the difference equation."""
        num = np.asarray(num, dtype=float)
        den = np.asarray(den, dtype=float)
        x = np.asarray(x, dtype=float)
        if den.size == 0 or den[0] == 0:
            raise ValueError("den must have a non-zero first coefficient")
        y = np.zeros_like(x, dtype=float)
        for n in range(x.size):
            for k in range(min(num.size, n + 1)):
                y[n] += num[k] * x[n - k]
            for k in range(1, min(den.size, n + 1)):
                y[n] -= den[k] * y[n - k]
            y[n] /= den[0]
        return y


signal = _Signal()
# Criando função para exibir diagrama resposta em frequencia
def plot_bode(num,den):
    w,h=signal.freqz(num,den) # Compute impulse response
    fig, axs = plt.subplots(2,1,sharex=True)
    plt.subplots_adjust( hspace = .2 )
    fig.set_size_inches((6,4))
    ax=axs[0]
    ax.plot(w,20*np.log10(abs(h)))
    ax.set_ylabel(r"$20 \log_{10} |H(\omega)| $",fontsize=14)
    ax.set_title("Resposta em frequencia",fontsize=18)
    ax.grid()
    ax=axs[1]
    ax.plot(w,angle(h)/pi*180)
    ax.set_xlabel(r'$\omega$ (radians/s)',fontsize=14)
    ax.set_ylabel(r"$\phi $ (deg)",fontsize=14)
    ax.set_xlim(xmax = pi)
    ax.grid()
    return
def plot_sinais(x,y,n,titulo):
    fig,ax = plt.subplots(1,1)
    fig.set_size_inches(10,4)
    ax.stem(n,x,markerfmt='b.',linefmt='b-',label='entrada',basefmt='b-')
    ax.plot(n,x,':')
    #ax.stem(n[1:],y[:-1],markerfmt='ro',linefmt='r-',label='output')
    #ax.plot(n[1:],y[:-1],'r:')
    ax.stem(n,y,markerfmt='r.',linefmt='r-',label='saida')
    ax.plot(n,y,'r:')
    ax.set_xlim(xmin=-1.1)
    ax.set_ylim(ymin=-1.1,ymax=1.1)
    ax.set_xlabel("n",fontsize=14)
    ax.legend(loc='upper right')
    ax.set_xticks(n)
    ax.set_ylabel("amplitude",fontsize=14);
    ax.set_title(titulo,fontsize=18)
    ax.set_axis_on()
    return
def plot_filtro(num,den,Ns):
    n= np.arange(Ns) # eixo n
    #criando a senoidal
    x = np.sin(np.arange(Ns)*pi/4.)
    y= signal.lfilter(num,den,x)
    plot_sinais(x,y,n,"Filtragem sinal")
    return
def plot_impulso(num,den,Ns):
    n= np.arange(Ns) # eixo n
    #criando o impulso
    x=np.zeros(Ns)
    x[0]=1
    y= signal.lfilter(num,den,x)
    plot_sinais(x,y,n,'Resposta ao impulso')
    return