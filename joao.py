import numpy as np

a=1
t1=1
t2=1
M=1
num_points=10



ka1=[]
ka2=[]
ka3=[]
kb1=[]
kb2=[]
kb3=[]



a1=a*[1,0]
a2=[-a/2,(3*a/2)**(1/2)]
a3=[-a/2,-(3*a/2)**(1/2)]


b1=[3*a/2,(3*a/2)**(1/2)]
b2=[-3*a/2,(3*a/2)**(1/2)]
b3=[-(3*a)**(1/2),0]

#kx=np.linspace(-np.pi, np.pi, num_points)
#ky=np.linspace(-np.pi, np.pi, num_points)
kx=np.linspace(0, 2*np.pi, num_points)
ky=np.linspace(0,2* np.pi, num_points)

for i in range (0,num_points,1):           #kx
	for j in range (0,num_points,1):   #ky	
		ka1.append(kx[i]*a1[0]  + ky[j]*a1[1])
		ka2.append(kx[i]*a2[0]  + ky[j]*a2[1])
		ka3.append(kx[i]*a3[0]  + ky[j]*a3[1])
		kb1.append(kx[i]*b1[0]  + ky[j]*b1[1])
		kb2.append(kx[i]*b2[0]  + ky[j]*b2[1])
		kb3.append(kx[i]*b3[0]  + ky[j]*b3[1])

result_a=(np.cos((ka1)) + np.cos((ka2)) + np.cos((ka3))) #multiplicado por sigma x
result_b=(np.sin((ka1)) + np.sin((ka2)) + np.sin((ka3))) #multiplicado por sigma y
result_c=(np.cos((kb1)) + np.cos((kb2)) + np.cos((kb3))) #multiplicado por sigma z

sx = np.array([[0,1],[1,0]])
sy = np.array([[0,-1j],[1j,0]])
sz = np.array([[1,0],[0,-1]])

H=np.zeros((2,2))

for i in range (0, len(result_a), 1):
	H[i]=t1*sx*result_a[i] - t1*sy*result_b[i] + 2*t2*sz*result_c[i] + M*sz

print(H[0])


