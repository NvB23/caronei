from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES

def validaNome(nome):
    if nome.strip() == "":
        print(BANCO_DE_FRASES['digite_algo'])
        return False
    elif nome.isnumeric() or nome.isdecimal():
        print(BANCO_DE_FRASES['apenas_letras'])
        return False
    elif not all(palavra.isalpha() for palavra in nome.split()):
        print(BANCO_DE_FRASES['apenas_letras'])
        return False
    return True

def validaEmail(email):
    if email.strip() == "":
        print(BANCO_DE_FRASES['digite_algo'])
        return False
    elif email.find("@") == -1 or email.find(".") == -1:
        print(BANCO_DE_FRASES['email_invalido'])
        return False
    elif email.isnumeric() or email.isdecimal():
        print(BANCO_DE_FRASES['apenas_letras'])
        return False
    return True

def validaSenha(senha):
    if senha.strip() == "":
        print(BANCO_DE_FRASES['digite_algo'])
        return False
    elif len(senha) < 8 or len(senha) > 15:
        print(BANCO_DE_FRASES['senha_invalida'])
        return False
    return True

def validaSenhaNovamente(confirmar_senha, senha):
    if senha.strip() == "":
        print(BANCO_DE_FRASES['digite_algo'])
        return False
    elif(confirmar_senha != senha):
        print(BANCO_DE_FRASES['diverge_campo'])
        return False
    return True
