# -*- coding: utf-8 -*-
def pega_formulas():
    formulas = input()
    return formulas

def pega_ocorrencias(formula):
    ocorrencias = []
    for valor in formula:
        if valor in ('(', ')'):
            ocorrencias.append(valor)
    return ocorrencias

def avalia_resultado(ocorrencias):
    if (ocorrencias[0] == '(') and (len(ocorrencias)%2 == 0) and (ocorrencias[-1] == ')'):
        fecha = []
        abre = []
        for val in ocorrencias:
            if val == ')':
                fecha.append(val)
            else:
                abre.append(val)
        if (len(abre) == len(fecha)):
            print('correct')
        else: 
            print('incorrect')   
    else: 
        print('incorrect')
        
                
if __name__ == "__main__":
    while True:
        try:
            formulas = pega_formulas()
            pega_ocorrencias(formulas)
            ocorrencias = pega_ocorrencias(formulas)
            avalia_resultado(ocorrencias)
        except EOFError:
            break
