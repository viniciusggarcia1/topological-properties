matriz = [
    [1, 2, 3, 3],
    [4, 17, 6, 10],
    [7, 10, 19, 10]
]

#soma_total = sum(sum(linha) for linha in matriz)
#print(soma_total)  # Saída: 45

#print (len(matriz[0]))

soma1=[]
for i in range (0, len(matriz), 1):
	soma1.append(sum(matriz[i]))
soma=sum(soma1)
print(soma)
