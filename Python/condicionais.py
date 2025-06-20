n1 = n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))

media = (n1 + n2) / 2

if (media >= 7):
    print('Resultado: Aprovado!')
    print('Parabens!')
elif(media >= 5):
    print('Aluno em recuperação.')
else:
    print('Aluno reprovado...')

print('Media: {}'.format(media) )
