from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
def validaQuantia(quantia):
    if quantia <= 0:
        print(BANCO_DE_FRASES['quantia_positiva'])
        return False
    return True