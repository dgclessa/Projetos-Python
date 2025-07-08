var_global = 'Curso completo de Python'

def escreve_texto():
    global var_global
    var_global ='Bancos de dados com SQL'
    var_local = 'Lucas Caio Lessa'
    print(f'Variável Global: {var_global}')
    print(f'Variável Local: {var_local}')
    
if __name__ == '__main__':
        print(f'Executar a função escreve_texto()')
        escreve_texto()
        
        print('Tentar acessar as variáveis diretamente')
        print(f'Variável Global: {var_global}')
        