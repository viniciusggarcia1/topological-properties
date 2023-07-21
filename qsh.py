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

# Plotar a fase de Berry em função de Kx e Ky 
def graph_berry(phases, kx_range, ky_range):
    plt.figure()
    plt.imshow(phases.T, origin='lower', extent=[kx_range[0], kx_range[-1], ky_range[0], ky_range[-1]], cmap='jet')
    plt.colorbar(label='Berry Phase')
    plt.xlabel('K$_x$', fontsize=18)
    plt.ylabel('K$_y$', fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.tight_layout()
    plt.savefig('berry.png', dpi=800)

# Plotar a estrutura de bandas
def graph_bands(kx_range, E0, E1, M, t):
    plt.figure()
    plt.plot(kx_range, E0, c='blue', label=f'M={M} and t={t}')
    plt.plot(kx_range, E1, c='blue')
    plt.xlabel('K$_x$', fontsize=18)
    plt.ylabel('Energy', fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.legend()
    plt.tight_layout()
    plt.savefig('bands.png', dpi=800)

# Plotar a fase de Berry para kx fixo
def graph_kx_fixed(ky_range, phases_fixed_kx, fixed_kx):
    plt.figure()
    plt.plot(ky_range, phases_fixed_kx, color='r', label=f'k$_x$={fixed_kx}')
    plt.xlabel('K$_y$', fontsize=18)
    plt.ylabel('Berry Phase', fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.legend()
    plt.tight_layout()
    plt.savefig('kx_fixed.png', dpi=800)

# Plotar a fase de Berry para ky fixo
def graph_ky_fixed(kx_range, phases_fixed_ky, fixed_ky):
    plt.figure()
    plt.plot(kx_range, phases_fixed_ky, color='r', label=f'k$_y$={fixed_ky}')
    plt.xlabel('K$_x$', fontsize=18)
    plt.ylabel('Berry Phase', fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.legend()
    plt.tight_layout()
    plt.savefig('ky_fixed.png', dpi=800)

#Função para calcular a projeção
def graph_proj(weight0, weight1, kx_range, E0, E1, M, t):
    plt.figure()
    for i in range (0, len(E0), 1):
        weight0[i]=weight0[i].real
        weight1[i]=weight1[i].real
        plt.scatter(kx_range[i], E0[i], s=10, c=5*weight0[i], vmin=-1, vmax=1, cmap='bwr')
        plt.scatter(kx_range[i], E1[i], s=10, c=5*weight1[i], vmin=-1, vmax=1, cmap='bwr')
    
    plt.ylabel('Energy', fontsize=18)
    plt.yticks(fontsize=14)
    plt.xlabel('k$_x$', fontsize=16)
    plt.text(-0.7, 7, f'M={M} and t={t}')
    plt.tight_layout()
    plt.savefig('proj.png', dpi=800)
