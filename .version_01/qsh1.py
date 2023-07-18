import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit

M=1
t=0.5
#kx=np.pi/4
#ky=np.pi/4
#kx=0
#ky=0

kx_fixed=0

kx=np.linspace(-np.pi, np.pi, 200)
ky=np.linspace(-np.pi, np.pi, 200)

berry=np.zeros((len(kx), len(kx)))

#for i in range (0, len(kx), 1):
#	if kx[i]>=-2 and kx[i]<= -1.9:
#		print(i)

#print(kx)



# Definindo a hamiltoniana
sx = np.array([[0,1],[1,0]])
sy = np.array([[0,-1j],[1j,0]])
sz = np.array([[1,0],[0,-1]])

def hamilt(kx, ky, M, t):
    H2 = t*kx*sx + t*ky*sy + (M - kx**2)*sz
    return H2
#print(hamilt[0][1])

E=[]
E1=[]
E2=[]

for i in range (0, len(kx), 1):
	for j in range (0, len(kx), 1):
		autoval, autovec = np.linalg.eig(hamilt(kx[i], ky[j], M, t))
		autovec[0]=np.conj(autovec[0])
		prod = (autovec[0][0] * autovec[1][0]) + (autovec[0][1] * autovec[1][1])
		berry[i][j]=(-np.angle(prod))
		
		if i==kx_fixed:
			#E.append(autoval)
			E1.append(autoval[0])
			E2.append(autoval[1])


#print(berry)			
#print(-autoval[0])
print(autovec[0])
print(np.conj(autovec[0]))
#############################################################################

# Fazendo a soma de todas as fases de Berry calculadas na matriz 'berry':
soma1=[]
for i in range (0, len(berry), 1):
        soma1.append(sum(berry[i]))
soma=sum(soma1)

print("A soma de todas as fases é: ", soma)
'''
# Soma apenas no limite de k:
soma1=[]
for i in range (0, len(berry), 1):
        soma1.append(berry[99][i])
soma=sum(soma1)

print("A soma de todas as fases é: ", soma)

'''









##############################################################################

#print(E)
#print(E[1][0])

#print(berry)


levels = np.linspace(-np.pi, np.pi, 300)

# Code to plot the first graph
plt.rcParams.update({'font.size': 14})
plt.contourf(kx, ky, berry, levels = levels,  cmap='jet')

#plt.plot(E_gd, deltaE_c, marker='o', markersize = 8, markerfacecolor = 'black', markeredgecolor = 'black')
#plt.text(E_gd+0.02, deltaE_c+0.03, f"{value_pce:.2f}%")
#plt.text(E_gd+0.02, deltaE_c+0.03, "Sb$_2$S$_3$@Sb$_2$Se$_3$")

plt.xlabel('k$_x$', labelpad = 10)
plt.ylabel('k$_y$', labelpad = 10)

colorbar = plt.colorbar(ticks = [-3, -2, -1, 0, 1, 2, 3])
colorbar.set_label('$\phi$', labelpad = 12)

plt.tight_layout()

plt.savefig("graph_berry_kx-ky.png", dpi=800)

#print(np.min(berry))

# Create new figure to plot the second graph
plt.figure()

############################

#kx fico em -2
plt.plot(ky, berry[kx_fixed], color='black', lw=1, zorder=2, label='Dados Brutos')
#plt.plot(x, z, color='red', lw=1, zorder=2, label='Global tilt')
#plt.plot(x, w, color='green', lw=1, zorder=2, label='Direct+Circumsolar')
plt.axhline(0, color='#cccccc', zorder=-10)


###parenteses#################################################################

'''

def serie_trigonometrica(ky, *coeficientes):
	n = len(coeficientes) // 2  # Divisão inteira para obter o número de termos da série
	resultado = coeficientes[0]  # Termo constante
	for i in range(1, n+1):
		resultado += coeficientes[i] * np.cos(i * ky) + coeficientes[i+n] * np.sin(i * ky)
	return resultado

# Ajuste por série trigonométrica
grau = 1  # Grau da série trigonométrica
coeficientes_iniciais = [1] * (2 * grau + 1)  # Valores iniciais dos coeficientes
coeficientes_otimizados, _ = curve_fit(serie_trigonometrica, ky, berry[38], p0=coeficientes_iniciais)

# Valores previstos pelo ajuste
x_fit = np.linspace(min(ky), max(ky), 100)  # Valores de x para plotagem suave
y_fit = serie_trigonometrica(x_fit, *coeficientes_otimizados)

# Plotar os dados brutos e o ajuste
plt.scatter(ky, berry[kx_fixed], label='Dados brutos')
plt.plot(x_fit, y_fit, color='red', label='Ajuste')
plt.xlabel('ky')
plt.ylabel('fase')
#plt.legend()
#plt.show()

'''

# Ajuste polinomial
grau = 3  # Grau do polinômio
coeficientes = np.polyfit(ky, berry[kx_fixed], grau)

# Valores previstos pelo ajuste
x_fit = np.linspace(min(ky), max(ky), 100)  # Valores de x para plotagem suave
y_fit = np.polyval(coeficientes, x_fit)

# Plotar os dados brutos e o ajuste
plt.scatter(ky, berry[kx_fixed], label='Pontos calculados')
plt.plot(x_fit, y_fit, color='red', label='Ajuste')


#############parenteses###########################################################

# Add legend
plt.legend()

# Add labels and title
plt.xlabel('k$_y$')
plt.ylabel('$\phi$')
#plt.title('Solar Radiation Spectrum')

plt.tight_layout()
plt.savefig('kx_fixed.png', dpi=800)


###########################################################################################

plt.figure()
#Estrutura de bandas

plt.plot(ky, E1, color='black', lw=1, zorder=2)
plt.plot(ky, E2, color='black', lw=1, zorder=2)


plt.axhline(0, color='#cccccc', zorder=-10)
plt.axvline(0, color='#cccccc', zorder=-10)

plt.xlabel('k$_y$', fontsize=18)
plt.ylabel('E', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)


plt.tight_layout()
plt.savefig('bands.png', dpi=800)
#plt.show()

#############################################################################

