import random

valor = random.randint(1,20)

print(valor,'\n')

print('Gerar números aleatórios entre 1 e 50: \n')

for i in range(5):
    n = random.randint(1,50)
    print(f'Número gerado: {n}')

#Exemplo de número aleatório do tipo flutuante
#A multiplicação por * 10 gera numeros aleatórios de ponto flutuante até 10
valor2 = random.random()
print(f'Número gerado: {valor2 * 10}')    

print(f'Número gerado: {round(valor2 * 10, 2)}')    

valor3 = random.uniform(1,100)
print(f'Número: {valor3}')
print(f'Número gerado: {round(valor3, 3)}')   

L = [2,6,14,25,3,75,9,72,26,8,43,50,37]
n = random.choice(L)
print(f'Número escolhido: {n}')

n = random.sample(L,3)
print(f'Números escolhido: {n}')

