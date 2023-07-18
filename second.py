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
    return phase

# Criar uma malha de pontos no espaço dos momentos
num_points = 100
kx_range = np.linspace(-np.pi, np.pi, num_points)
ky_range = np.linspace(-np.pi, np.pi, num_points)
phases = np.zeros((num_points, num_points))

# Parâmetros da Hamiltoniana
t = 0.5
M = 1

# Calcular a fase de Berry para cada ponto da malha
for i, kx in enumerate(kx_range):
    for j, ky in enumerate(ky_range):
        phases[i, j] = berry_phase(kx, ky, t, M)

# Plotar a fase de Berry em função de Kx e Ky
plt.figure(figsize=(8, 6))
plt.imshow(phases.T, origin='lower', extent=[kx_range[0], kx_range[-1], ky_range[0], ky_range[-1]], cmap='jet')
plt.colorbar(label='Berry Phase')
plt.xlabel('Kx')
plt.ylabel('Ky')
plt.title('Berry Phase in Momentum Space')
plt.savefig('berry.png', dpi=800)

# Plotar a estrutura de bandas
num_bands = 2
energies = np.zeros((num_points, num_bands))

# Calcular as energias para cada ponto da malha
for i, kx in enumerate(kx_range):
    eigenvalues, _ = diagonalize_hamiltonian(kx, 0, t, M)  # Fixar ky em 0
    energies[i, :] = eigenvalues

# Plotar a estrutura de bandas
plt.figure(figsize=(8, 6))
for band in range(num_bands):
    plt.plot(kx_range, energies[:, band], label='Band {}'.format(band + 1))
plt.xlabel('Kx')
plt.ylabel('Energy')
plt.title('Energy Band Structure')
plt.legend()
plt.savefig('bands.png', dpi=800)

# Plotar a fase de Berry para kx fixo
fixed_ky = np.pi / 4
phases_fixed_ky = np.zeros(num_points)

# Calcular a fase de Berry para kx fixo e ky variando
for i, ky in enumerate(ky_range):
    phases_fixed_ky[i] = berry_phase(kx, fixed_ky, t, M)

# Plotar a fase de Berry para kx fixo
plt.figure(figsize=(8, 6))
plt.plot(ky_range, phases_fixed_ky, color='r')
plt.xlabel('Ky')
plt.ylabel('Berry Phase')
plt.title('Berry Phase for Fixed Ky')
plt.savefig('just_k.png', dpi=800)
