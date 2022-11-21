# -*- coding: utf-8 
def risos():
    risada = input()
    risada = risada.lower()
    return risada

def sequencia(risada) -> str:
    vogais = ['a', 'e', 'i', 'o', 'u']
    seq = ''
    for i in risada:
        if i in (vogais):
            seq = seq+i
    return seq

def intensidade(vogais):
    correta = vogais
    reversa = vogais[::-1] 
    if correta == reversa:
        print('S') 
    else:
        print('N')
        

if __name__ == "__main__":
    risada = risos()
    vogais = sequencia(risada)
    intensidade(vogais) 
