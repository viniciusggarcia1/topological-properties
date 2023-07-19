import numpy as np
import qsh_main as qsh
from matplotlib import pyplot as plt

sigma_z = np.array([[1, 0], [0, -1]])

#Vconj=np.zeros((2,len(qsh.kx_range)))
Vconj0=[]
Vconj1=[]
V0=[]
V1=[]
weight0=[]
weight1=[]
E0=[]
E1=[]

for kx in range (0, len(qsh.kx_range), 1):
    ky=kx
    E, V=qsh.diagonalize_hamiltonian(qsh.kx_range[kx], qsh.ky_range[kx], qsh.t, qsh.M)
    
    E0.append(E[0])
    E1.append(E[1])
    V0.append(V[0])
    V1.append(V[1])
    Vconj0.append(np.conj(V[0]))
    Vconj1.append(np.conj(V[1]))

    weight0.append(Vconj0[kx][0]*(sigma_z[0][0]*V0[kx][0] + sigma_z[0][1]*V0[kx][1]) + Vconj0[kx][1]*(sigma_z[1][0]*V0[kx][0] + sigma_z[1][1]*V0[kx][1]))

    weight1.append(Vconj1[kx][0]*(sigma_z[0][0]*V1[kx][0] + sigma_z[0][1]*V1[kx][1]) + Vconj1[kx][1]*(sigma_z[1][0]*V1[kx][0] + sigma_z[1][1]*V1[kx][1]))
  

plt.figure()

for i in range (0, len(E0), 1):
    weight0[i]=weight0[i].real
    weight1[i]=weight1[i].real
    
    # Plotting Graph of donor
    plt.scatter(qsh.kx_range[i], E0[i], s=10, c=5*weight0[i], vmin=-1, vmax=1, cmap='bwr')
    plt.scatter(qsh.kx_range[i], E1[i], s=10, c=5*weight1[i], vmin=-1, vmax=1, cmap='bwr')
    

plt.ylabel('Energy', fontsize=18)
plt.yticks(fontsize=14)
plt.xlabel('k$_x$', fontsize=16)

plt.tight_layout()
plt.savefig('proj.png', dpi=800)