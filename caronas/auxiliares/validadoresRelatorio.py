from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
def validaOpcaoRelatorio(opcao_relatorio: str):
    if opcao_relatorio.strip() == "":
        print(BANCO_DE_FRASES["digite_algo"])
        return False
    if opcao_relatorio not in ["1", "2"]:
        print(BANCO_DE_FRASES["opcao_invalida"])
        return False
    return True