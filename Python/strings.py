# nome = 'Diego '
# sobrenome = 'Coelho Lessa'
# letra = nome[2]
# print(letra)
# print(len(nome))
# print(nome + sobrenome)

# frase = 'Vamos aprender Python hoje'
# palavras = frase.split()
# print(palavras[1])

# for palavra in palavras:
#     print(palavra)

# for letra in frase:
#     print(letra)
    
# print(frase[0:5],'\n')


email = input('Digite seu email: ')
arroba = email.find('@')
print(arroba)
usuario = email[0:arroba]
dominio = email[arroba+1:]
print(usuario)
print(dominio)

#Docstring

"""""
Docstring é uma documentação de uma função, classe ou módulo
"""""

texto = """""
Docstring é uma documentação de uma função, classe ou módulo
"""""

print(texto)