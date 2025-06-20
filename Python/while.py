num = 1

while (num <= 10000):
    print(f'{num}')
    num += 1 
print('Laço Encerrado!')

nome = None

while True:
    print('Digite seu nome, ou x para parar....')
    nome = input('Digite o seu nome:')
    if(nome == 'x' or nome == 'X'):
        break
    print(f'Bem vindo, {nome}!')

print('Ate logo!')