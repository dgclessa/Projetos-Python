def mensagem():
    print('Curso completo python.')
    
mensagem()    

# Funçaõ com argumentos

def soma(a, b):
    print(a+b)
    
#soma(10,5)    

def mult(x, y):
    return x * y
    
#soma(mult(3,7),5)    

if __name__ == '__main__':
    
    soma(mult(3,7),5)    
    soma(10,5)    

