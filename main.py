# Code to calculate topological properties using a Hamiltonian 07/20/2023
# Vinícius G. Garcia
# Graduate Program in Physics - PPGFis
# Federal University of Espírito Santo - UFES
# viniciusggarcia1@hotmail.com

import numpy as np
import qsh
from tqdm import tqdm
import time

print()
print("========================TOPOLOGICAL PROPERTIES========================")
print()

# Hamiltonian parameters
t = float(input('Enter the hopping parameter (t): '))
M = float(input('Enter the topological mass (M): '))
fixed_kx = 1
fixed_ky = 1
print()

# Create a mesh of points in the space of moments
num_points = 100
kx_range = np.linspace(-np.pi, np.pi, num_points)
ky_range = np.linspace(-np.pi, np.pi, num_points)
phases = np.zeros((num_points, num_points))

# Calculate the Berry phase for each point of the mesh
for i, kx in enumerate(kx_range):
    for j, ky in enumerate(ky_range):
        phases[i, j] = qsh.berry_phase(kx, ky, t, M)

# Plot the structure of bands
num_bands = 2
energies = np.zeros((num_points, num_bands))
E0=[]
E1=[]

# Calculate the energies for each point of the mesh
for i, kx in enumerate(kx_range):
    eigenvalues, _ = qsh.diagonalize_hamiltonian(kx, 0, t, M)  # Fixar ky em 0
    #energies[i, :] = eigenvalues
    E0.append(eigenvalues[0])
    E1.append(eigenvalues[1])

# Fixed Kx Phase Transition
# Plot the Berry phase to fixed kx
phases_fixed_kx = np.zeros(num_points)

# Calcular a fase de Berry para kx fixo e ky variando
for i, ky in enumerate(ky_range):
    phases_fixed_kx[i] = qsh.berry_phase(fixed_kx, ky, t, M)

# Fixed Ky Phase Transition
# Plot the Berry phase to fixed ky
phases_fixed_ky = np.zeros(num_points)

# Calculate the Berry phase for fixed kx and ky varying
for i, kx in enumerate(kx_range):
    phases_fixed_ky[i] = qsh.berry_phase(kx, fixed_ky, t, M)

# Calculating the projection in spin up and turn down
sigma_z = np.array([[1, 0], [0, -1]])
Vconj0=[]
Vconj1=[]
V0=[]
V1=[]
weight0=[]
weight1=[]
E0=[]
E1=[]

for kx in range (0, len(kx_range), 1):
    ky=kx
    E, V=qsh.diagonalize_hamiltonian(kx_range[kx], ky_range[kx], t, M)
    E0.append(E[0])
    E1.append(E[1])
    V0.append(V[0])
    V1.append(V[1])
    Vconj0.append(np.conj(V[0]))
    Vconj1.append(np.conj(V[1]))

    weight0.append(Vconj0[kx][0]*(sigma_z[0][0]*V0[kx][0] + sigma_z[0][1]*V0[kx][1]) + 
                   Vconj0[kx][1]*(sigma_z[1][0]*V0[kx][0] + sigma_z[1][1]*V0[kx][1]))


    weight1.append(Vconj1[kx][0]*(sigma_z[0][0]*V1[kx][0] + sigma_z[0][1]*V1[kx][1]) +
                    Vconj1[kx][1]*(sigma_z[1][0]*V1[kx][0] + sigma_z[1][1]*V1[kx][1]))


# We will call all Plot functions to save the graphics
with tqdm(total=5) as prog:
    qsh.graph_berry(phases, kx_range, ky_range)
    prog.update(1)

    qsh.graph_bands(kx_range, E0, E1, M, t)
    prog.update(1)

    qsh.graph_kx_fixed(ky_range, phases_fixed_kx, fixed_kx)
    prog.update(1)

    qsh.graph_ky_fixed(kx_range, phases_fixed_ky, fixed_ky)
    prog.update(1)

    qsh.graph_proj(weight0, weight1, kx_range, E0, E1, M, t)
    prog.update(1)

print()
print("=========================by Vinícius G. Garcia========================")
print()