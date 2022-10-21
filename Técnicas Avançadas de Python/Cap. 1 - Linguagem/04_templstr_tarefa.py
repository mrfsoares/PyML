# -*- coding: latin-1 -*-
# Demonstração das funções de string templates
from string import Template


def main():
    # Formatação tradicional usando o método format()
    frase = "Você está assistindo {0} com {1}".format(
        "Python Avançado", "Jessica Temporal")
    print(frase)

    # TODO: Crie um template com placeholders
    templ = Template("Você está assistindo ${curso} com ${professor}")

    # TODO: Use o método substitute passando argumentos nomeados
    frase_2 = templ.substitute(curso="Python Avançado",
                               professor="Jessica Temporal")
    print(frase_2)
    # TODO: Use  o método substitute com um dicionário
    info = {
        "curso": "Python Avançado",
        "professor": "Jessica Temporal"
    }
    frase_3 = templ.substitute(info)
    print(frase_3)
    print(type(frase_3))


if __name__ == "__main__":
    main()
