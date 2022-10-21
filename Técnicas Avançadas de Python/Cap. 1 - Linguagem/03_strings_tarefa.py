# strings e bytes não são diretamente intercambiáveis
# strings contém unicode, bytes são valores de 8 bits

def main():
    # definindo alguns valores iniciais
    a = 'ABCD'
    b = bytes([0x41, 0x42, 0x43, 0x44])

    # TODO: Tente juntar os dois.
    # print(a + b, '\n')

    # TODO: Bytes e strings precisam ser apropriadamente encoded
    c = b.decode('utf-8')
    print(a + c, '\n')

    d = a.encode('utf-8')
    print(d + b, '\n')

    # TODO: Faça o encode da string como UTF-32
    e = a.encode('utf-32')
    print(e)


if __name__ == "__main__":
    main()
