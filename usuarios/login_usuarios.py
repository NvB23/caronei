from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
from usuarios.auxiliares.validadores_usuario import validaEmail, validaSenha
from pwinput import pwinput
import os

def loginUsuarios(logado, usuarios_cadastrados, usuario_atual):
    while True:
        print(BANCO_DE_FRASES['titulo_login'])

        # Pega email
        while True:
            login_email = input(BANCO_DE_FRASES['digite_email'])
            if validaEmail(login_email) == False:
                continue
            break
        
        # Pega senha
        while True:
            login_senha = pwinput(prompt=f"\n{BANCO_DE_FRASES['digite_senha']}", mask="•")
            if validaSenha(login_senha) == False:
                continue
            break

        for i in range(len(usuarios_cadastrados)):
            if (login_email == usuarios_cadastrados[i]['email']):
                usuario_atual = i
        for usuario in usuarios_cadastrados:
            if((login_email == usuario['email']) and (login_senha == usuario['senha'])):
                logado = True
        os.system("cls" if os.name == 'nt' else 'clear')

        if(logado == False):
            print(BANCO_DE_FRASES['login_falhou'])
        return logado, usuario_atual