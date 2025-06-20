idade = 15
altura = 1.80

resultado = (idade >= 18) and (altura >= 1.80)
msg = 'Pode participar do evento?' + str(resultado)

print(msg)

porta = 'a'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
msg2 = 'Alarme disparado? ' + str(alarme)
print(msg2)
