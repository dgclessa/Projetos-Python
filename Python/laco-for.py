lista = [2,6,9,4,0,12,3,7]
palavra = 'Boson'

for item in lista:
    print(item)

for letra in palavra:
    print(letra)

for numero in range(1,101):
    print(numero)


for numero in range(100):
    print(numero)    

pedras = ('Rubi','Esmeralda','Quartzo','Safira','Diamante','Turmalina')    

for pedra in pedras:
    if (pedra == 'Quartzo'):
        continue
    print(pedra)