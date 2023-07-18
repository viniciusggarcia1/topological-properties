import numpy as np
import matplotlib.pyplot as plt

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
   # eigenvectors[0]=np.conj(eigenvectors[0])
   # prod = (eigenvectors[0][0] * eigenvectors[1][0]) + (eigenvectors[0][1] * eigenvectors[1][1])
   # phase[i][j]=(-np.angle(prod))
    return phase

# Criar uma malha de pontos no espaço dos momentos
num_points = 200
kx_range = np.linspace(-np.pi, np.pi, num_points)
ky_range = np.linspace(-np.pi, np.pi, num_points)
phases = np.zeros((num_points, num_points))
energies = np.zeros((num_points, num_points, 2))

# Parâmetros da Hamiltoniana
t = 0.5
M = 1

# Calcular a fase de Berry e os autovalores para cada ponto da malha
for i, kx in enumerate(kx_range):
    for j, ky in enumerate(ky_range):
        phases[i, j] = berry_phase(kx, ky, t, M)
        eigenvalues, _ = diagonalize_hamiltonian(kx, ky, t, M)
        energies[i, j, :] = eigenvalues

# Plotar a fase de Berry
plt.figure(figsize=(8, 6))
plt.imshow(phases.T, origin='lower', extent=[kx_range[0], kx_range[-1], ky_range[0], ky_range[-1]], cmap='jet')
plt.colorbar(label='Fase de Berry')
plt.xlabel('Kx', fontsize=16)
plt.ylabel('Ky', fontsize=16)
plt.title('Berry Phase in Momentum Space', fontsize=16)
plt.savefig('range.png', dpi=800)

# Plotar a estrutura de bandas
fig, ax = plt.subplots(2, 1, figsize=(8, 10))
ax[0].set_xlabel('K$_x$', fontsize=16)
ax[0].set_ylabel('Energia', fontsize=16)
ax[0].set_title('Estrutura de Bandas', fontsize=16)

# Plotar as bandas de energia
for band in range(2):
    color = 'b' if energies[0, 0, band] > 0 else 'r'
    ax[0].plot(kx_range, energies[:, :, band], color=color)

# Fixar kx e variar ky
fixed_ky = np.pi / 4
ky_fixed = np.linspace(-np.pi, np.pi, num_points)
phases_fixed_ky = np.zeros(num_points)

# Calcular a fase de Berry para kx fixo e ky variando
for i, ky in enumerate(ky_fixed):
    phases_fixed_ky[i] = berry_phase(kx, fixed_ky, t, M)

# Plotar a fase de Berry para kx fixo
ax[1].plot(phases_fixed_ky, ky_fixed, color='black', label='Fase de Berry para K$_x$ fixado')
ax[1].set_xlabel('K$_y$', fontsize=16)
ax[1].set_ylabel('Fase de Berry', fontsize=16)
#ax[1].set_title('Fase de Berry para K$_x$ fixado', fontsize=16)

plt.legend()
plt.tight_layout()
plt.savefig('bands.png', dpi=800)

