numeros=[]
for i in range(0,4):
    numero= float(input(f"digite o numero {i+1}: "))
    numeros.append(numero*numero)
print(f"quadrado do numero 1 = {numeros[0]}")
print(f"quadrado do numero 2 = {numeros[1]}")
print(f"quadrado do numero 3 = {numeros[2]}")
print(f"quadrado do numero 4 = {numeros[3]}")
soma_quadrados= numeros[0]+numeros[1]+numeros[2]+numeros[3]
print(f"a soma dos quadrados é = 2{soma_quadrados}")