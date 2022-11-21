# -*- coding: utf-8 
def cartas():
    casos = int(input())
    casos = list(range(0, casos))
    
    pares = []
    for caso in casos:
        valor = list(map(int, input().split(' ')))
        pares.append(valor)

    return pares

def MDC(a, b):
    while(b != 0):
        resto = a % b
        a = b
        b = resto
  
    return a
    
def saida():
    '''Deve ser o máximo divisor comum do total de cartas de ambos os envolvidos'''
    ref = cartas()
    for caso in ref:
        maximo = MDC(int(caso[0]), int(caso[1]))
        print(maximo)


if __name__ == "__main__":
    saida()    
