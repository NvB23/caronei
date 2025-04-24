import importlib.util
import os
import subprocess
import sys

# Instala a biblioteca externa pwinput se ela ainda não estiver instalada
if(importlib.util.find_spec("pwinput") is None):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pwinput"])
    os.system("cls" if os.name == "nt" else "clear")


import pwinput
from time import sleep

caronei = """
   ______   ___       ____     ____     _   __   ______   ____   __
  / ____/  /   |     / __ \   / __ \   / | / /  / ____/  /  _/  / /
 / /      / /| |    / /_/ /  / / / /  /  |/ /  / __/     / /   / / 
/ /___   / ___ |   / _, _/  / /_/ /  / /|  /  / /___   _/ /   /_/  
\____/  /_/  |_|  /_/ |_|   \____/  /_/ |_/  /_____/  /___/  (_)  
"""

usuarios_cadastrados = []
usuario_atual = -1
logado = False
logout_opcao = ""
cad_log_opcao = ""

while True:
    linhas = "-" * 25
    apagar_terminal = os.system("cls" if os.name == 'nt' else 'clear')

    # Mostra sessão de usuário com nome
    if(logado == True and usuario_atual != -1):
        print(f"\n\n\033[1;34m{linhas*2}\n") 
        nome_estilizado = f"Usuário: {usuarios_cadastrados[usuario_atual][0]}".center(50).upper()
        print(f"\033[3;35m{nome_estilizado}\033[m")
        print(f"\n\033[1;34m{linhas*2}")
    

    # Painel de boas vindas e opções
    print(f"\n\033[1;34mBem vindo ao\n\n{caronei}\n\n\033[1;34mOpções:\n")
    if(logado == False):
        print("     [1] Cadastrar Usuário\n     [2] Fazer Login")
    else:
        print("     [1] Oferecer Carona\n     [2] Pegar Carona")
    if(logado == True):
        print("     [3] Logout")
    print("     [0] Fechar\n")

    opcao = input("\033[1;34mSelecione uma opção >>> \033[m")
    print("\n")

    # Cadastro de usuários
    if(opcao == '1'):
        if(logado == False):
            print(f"{linhas} Cadastro {linhas}")
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            senha = pwinput.pwinput(prompt="Digite sua senha: ", mask="•")
            confirmar_senha = pwinput.pwinput(prompt="Digite sua senha novamente: ", mask="•")
            usuarios_cadastrados.append([nome, email, senha])
            apagar_terminal

    # Login de usuários
    if(opcao == '2'):
        if(logado == False):
            print(f"{linhas} Login {linhas}")
            login_email = input("Digite o seu email: ")
            login_senha = pwinput.pwinput(prompt="Digite o sua senha: ", mask="•")
            for i in range(len(usuarios_cadastrados)):
                if (login_email == usuarios_cadastrados[i][1]):
                    usuario_atual = i
            for usuario in usuarios_cadastrados:
                if((login_email in usuario[1]) and (login_senha in usuario[2])):
                    logado = True
            apagar_terminal

    # Sair da conta
    if(opcao == '3'):
        if (logado == True):
            logado = False
            print("Saindo da conta...")
            sleep(3)
            print("Concluido")
            sleep(2)
            apagar_terminal
        else:
            print("Opção Inválida")


    # Fecha o programa
    if(opcao == '0'):
        break