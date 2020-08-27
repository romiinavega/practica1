import sys
sys.path.insert(1, 'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate
from thinkdsp import CosSignal

#crear señal senoidal
seno = SinSignal (freq=400, amp=0.7, offset=0)
coseno = CosSignal (freq=800, amp=1.1, offset=0)

#modulo para mostrar grafiicas
import matplotlib.pyplot as plt

#crear grafica en memoria
seno.plot()
decorate(xlabel='tiempo (s)')
decorate(ylabel='amplitud')

coseno.plot()
plt.show()