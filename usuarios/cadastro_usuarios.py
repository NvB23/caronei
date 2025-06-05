from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
from usuarios.auxiliares.validadores_usuario import validaNome, validaEmail, validaSenha, validaSenhaNovamente
from pwinput import pwinput
import os
from time import sleep
from usuarios.auxiliares.usuarios import paraArquivo

def cadastraUsuario(usuarios_cadastrados, saldo):
    print(BANCO_DE_FRASES['titulo_cadastro'])

    # Pega nome
    while True:
        nome = input(BANCO_DE_FRASES['digite_nome']).title()
        if validaNome(nome) == False:
            continue
        break
    
    # Pega email
    while True:
        email = input(BANCO_DE_FRASES['digite_email'])
        if validaEmail(email) == False:
            continue
        ja_cadastrado = False
        for usu in usuarios_cadastrados:
            if(email == usu['email']):
                print(BANCO_DE_FRASES['email_cadastrado'])
                ja_cadastrado = True
                break
        if(ja_cadastrado == True):
            continue
        break

    # Pega senha
    while True:
        str_senha = BANCO_DE_FRASES['digite_senha']
        senha = pwinput(prompt=f"\n{str_senha}", mask="•")
        if validaSenha(senha) == False:
            continue
        break

    # Pega confrimação de senha
    while True:
        str_senha_novamente = BANCO_DE_FRASES['confirme_senha']
        confirmar_senha = pwinput(prompt=f"\n{str_senha_novamente}", mask="•")
        if validaSenhaNovamente(confirmar_senha, senha) == False:
            continue
        break

    dicionario = {'nome': nome, 'email': email, 'senha': senha}
    usuarios_cadastrados.append(dicionario)
    paraArquivo(dicionario)
    
    for i in range(len(usuarios_cadastrados)):
        usuario_atual = i
    saldo[usuario_atual] = 0.0

    print(BANCO_DE_FRASES['cadastro_sucesso'])
    sleep(1)
    os.system("cls" if os.name == 'nt' else 'clear')
    return usuarios_cadastrados, saldo