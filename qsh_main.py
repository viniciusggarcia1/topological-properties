import numpy as np
import matplotlib.pyplot as plt 

# Parâmetros da Hamiltoniana
t = 0.3
M = 1.0
fixed_kx = 1
fixed_ky = 1

# Definir a Hamiltoniana
def hamiltonian(kx, ky, t, M):
    sigma_x = np.array([[0, 1], [1, 0]])
    sigma_y = np.array([[0, -1j], [1j, 0]])
    sigma_z = np.array([[1, 0], [0, -1]])
    H = t * kx * sigma_x + t * ky * sigma_y + (M - kx**2) * sigma_z
    return H

# Calcular os autovalores e autovetores da Hamiltoniana
def diagonalize_hamiltonian(kx, ky, t, M):
    H = hamiltonian(kx, ky, t, M)
    eigenvalues, eigenvectors = np.linalg.eigh(H)
    return eigenvalues, eigenvectors

# Calcular a fase de Berry
def berry_phase(kx, ky, t, M):
    eigenvalues, eigenvectors = diagonalize_hamiltonian(kx, ky, t, M)
    phase = np.angle(np.prod(np.conj(eigenvectors[:, 0])))
    return phase

# Criar uma malha de pontos no espaço dos momentos
num_points = 100
kx_range = np.linspace(-np.pi, np.pi, num_points)
ky_range = np.linspace(-np.pi, np.pi, num_points)
phases = np.zeros((num_points, num_points))

# Calcular a fase de Berry para cada ponto da malha
for i, kx in enumerate(kx_range):
    for j, ky in enumerate(ky_range):
        phases[i, j] = berry_phase(kx, ky, t, M)

# Plotar a fase de Berry em função de Kx e Ky
plt.figure()
plt.imshow(phases.T, origin='lower', extent=[kx_range[0], kx_range[-1], ky_range[0], ky_range[-1]], cmap='jet')
plt.colorbar(label='Berry Phase')

plt.xlabel('K$_x$', fontsize=18)
plt.ylabel('K$_y$', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
#plt.title('Berry Phase in Momentum Space')
plt.tight_layout()
plt.savefig('berry.png', dpi=800)

# Plotar a estrutura de bandas
num_bands = 2
energies = np.zeros((num_points, num_bands))

# Calcular as energias para cada ponto da malha
for i, kx in enumerate(kx_range):
    eigenvalues, _ = diagonalize_hamiltonian(kx, 0, t, M)  # Fixar ky em 0
    energies[i, :] = eigenvalues

# Plotar a estrutura de bandas
plt.figure()
for band in range(num_bands):
    plt.plot(kx_range, energies[:, band], label='Band {}'.format(band + 1))
plt.xlabel('K$_x$', fontsize=18)
plt.ylabel('Energy', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
#plt.title('Energy Band Structure')
plt.legend()
plt.tight_layout()
plt.savefig('bands.png', dpi=800)


#Transição de Fase Kx fixo+++++++++++++++++++++++++++++++++++++++++++++++++

# Plotar a fase de Berry para kx fixo

phases_fixed_kx = np.zeros(num_points)

# Calcular a fase de Berry para kx fixo e ky variando
for i, ky in enumerate(ky_range):
    phases_fixed_kx[i] = berry_phase(fixed_kx, ky, t, M)

# Plotar a fase de Berry para kx fixo
plt.figure()
plt.plot(ky_range, phases_fixed_kx, color='r')
plt.xlabel('K$_y$', fontsize=18)
plt.ylabel('Berry Phase', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
#plt.title('Berry Phase for Fixed K$_x$')
plt.tight_layout()
plt.savefig('kx_fixed.png', dpi=800)

#Transição de Fase Ky fixo+++++++++++++++++++++++++++++++++++++++++++++++++

# Plotar a fase de Berry para ky fixo

phases_fixed_ky = np.zeros(num_points)

# Calcular a fase de Berry para kx fixo e ky variando
for i, kx in enumerate(kx_range):
    phases_fixed_ky[i] = berry_phase(kx, fixed_ky, t, M)

# Plotar a fase de Berry para ky fixo
plt.figure()
plt.plot(kx_range, phases_fixed_ky, color='r')
plt.xlabel('K$_x$', fontsize=18)
plt.ylabel('Berry Phase', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
#plt.title('Berry Phase for Fixed K$_x$')
plt.tight_layout()
plt.savefig('ky_fixed.png', dpi=800)