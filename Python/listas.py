# Lista: representa uma sequência de valores

notas = [5,7,8,6,9]
print(notas)

n1= [1,3,8,4,9]
n2 =[13,20,35,28]
valores = n1 + n2
print(valores)

print(valores[3])
print(valores[0:4])
print(len(valores))

valores.append(98)
print(valores)

planetas = ['Mercurio','Venus','Terra','Marte','Jupter','Saturno','Urano','Netuno']

for planeta in planetas:
    print(planeta)

bebidas = []

for i in range(5):
    bebidas.append(input('Digite uma bebida: '))

print(bebidas)    