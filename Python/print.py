#Sintaxe
#print(objetos, argumentos)

mensagem = 'Função Print()'
print(mensagem)
print('Aula de Python')

nome = 'João das coves'
print('Treinamento ministrado por ', nome)

#concatenação

nome2 = input('Digite o seu nome:')

print('Olá ' + nome2 + ' Bem vindo!')

print('Imprime a mensagem e muda de linha')
print('Impreme a mensagem e permaneça nessa linha.',end='')
print(' Contunuamos na mesma linha')

nome3 = 'Lucas Caio'
idade = 5

msg_formatada = 'O nome dele é {0}, ele tem {1} anos de idade'.format(nome3,idade)

print(msg_formatada)

nome4 = 'Diego'
peso = 74.5
msg = f'olá meu nome é {nome4} e eu peso {peso} quilos.'
print(msg)
print(f'olá meu nome é {nome4} e eu peso {peso} quilos.')

a = 10
b= 25.8

print(f'A soma de {a} + {b} é {a + b}')

valor = 125.579637
print(f'O Valor é {valor:.2f}')
print('Como utilizar aspas \'\'')
print(f'Nome: {nome3}\tIdade: {idade}')