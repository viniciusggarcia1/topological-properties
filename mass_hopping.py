import qshin as qsh
import numpy as np
from matplotlib import pyplot as plt

M=np.linspace(-2, 2, 1000)
t=np.linspace(-2, 2, 1000)

#Vamos analizar como o Bandgap varia de acordo com a mudança de M e com t fixo

E0=[]
E1=[]
gap=[]

for i in range (0, len(M), 1):
        for j in range (0, len(qsh.kx_range), 1):
            E, V = qsh.diagonalize_hamiltonian(qsh.kx_range[j], 0, qsh.t, M[i])
            E0.append(E[0])
            E1.append(E[1])
        
        gr0=max(E0)
        gr1=min(E1)
        gap.append(gr1-gr0)


plt.figure()

plt.plot(M, gap, color='r')
plt.xlabel('M', fontsize=18)
plt.ylabel('Bandgap Energy', fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.tight_layout()
plt.savefig('bandgap_M.png', dpi=800)

#Fazendo o mesmo cálculo, mas com M fixo e t variando

E2=[]
E3=[]
gap2=[]

for i in range (0, len(M), 1):
        for j in range (0, len(qsh.kx_range), 1):
            E, V = qsh.diagonalize_hamiltonian(qsh.kx_range[j], 0, t[i], qsh.M)
            E2.append(E[0])
            E3.append(E[1])
        
        gr2=max(E2)
        gr3=min(E3)
        gap2.append(gr3-gr2)


plt.figure()

plt.plot(t, gap2, color='r')
plt.xlabel('t', fontsize=18)
plt.ylabel('Bandgap Energy', fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.tight_layout()
plt.savefig('bandgap_t.png', dpi=800)
