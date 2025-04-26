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
from datetime import date, datetime
import time

caronei = """
   ______   ___       ____     ____     _   __   ______   ____   __
  / ____/  /   |     / __ \   / __ \   / | / /  / ____/  /  _/  / /
 / /      / /| |    / /_/ /  / / / /  /  |/ /  / __/     / /   / / 
/ /___   / ___ |   / _, _/  / /_/ /  / /|  /  / /___   _/ /   /_/  
\____/  /_/  |_|  /_/ |_|   \____/  /_/ |_/  /_____/  /___/  (_)  
"""

usuarios_cadastrados = [['Naum', 'naum', '123']]
caronas_cadastradas = {}

usuario_atual = -1
logado = False
logout_opcao = ""
cad_log_opcao = ""
invalida_opcao = "Opção Inválida!"

while True:
    linhas = "-" * 25

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
        print("     [3] Listar Todas as Caronas Disponíveis")
        print("     [4] Logout")
    print("     [0] Fechar\n")

    opcao = input("\033[1;34mSelecione uma opção >>> \033[m")
    print("\n")

    # Valida se o usuário não digitar nada
    if(opcao.strip() == ""):
        print("Digite algo!")
        sleep(1)
        os.system("cls" if os.name == 'nt' else 'clear')
        continue

    # Valida se não vai digitar nada fora do padrão
    elif(opcao not in ["1", "2", "3", "4", "0"]):
        print(invalida_opcao)
        sleep(1)
        os.system("cls" if os.name == 'nt' else 'clear')
        continue

    # Cadastro de usuários e validações
    elif(opcao == '1' and logado == False):
        print(f"{linhas} Cadastro {linhas}")

        while True:
            nome = input("\nDigite seu nome: ").title()
            if nome.strip() == "":
                print("Digite algo!")
                continue
            elif nome.isnumeric() or nome.isdecimal():
                print("Apenas letras!")
                continue
            elif not all(palavra.isalpha() for palavra in nome.split()):
                print("Apenas letras!")
                continue
            break
        
        while True:
            email = input("\nDigite seu email: ")
            if email.strip() == "":
                print("Digite algo!")
                continue
            elif email.find("@") == -1 or email.find(".") == -1:
                print("Email inválido!")
                continue
            elif email.isnumeric() or email.isdecimal():
                print("Apenas letras!")
                continue
            cadastrado = False
            for usu in usuarios_cadastrados:
                if(email == usu[1]):
                    print("Email já cadastrado!")
                    cadastrado = True
                    break

            if(cadastrado == True):
                continue

            break

        while True:
            senha = pwinput.pwinput(prompt="\nDigite sua senha: ", mask="•")
            if senha.strip() == "":
                print("Digite algo!")
                continue
            elif len(senha) < 8 or len(senha) > 15:
                print("A senha precisa ter no mínimo 8 caracteres e no máximo 15 caracteres!")
                continue
            break

        while True:
            confirmar_senha = pwinput.pwinput(prompt="\nDigite sua senha novamente: ", mask="•")
            if(confirmar_senha != senha):
                print("Diverge do campo anterior!")
                continue
            break

        print("\nCadastro realizado com sucesso!")
        sleep(1)

        usuarios_cadastrados.append([nome, email, senha])
        os.system("cls" if os.name == 'nt' else 'clear')
            

    # Oferecer Carona e validações
    elif(opcao == '1' and logado == True):  
        while True:      
            origem = input("De onde você vai partir: ").title()
            if origem.strip() == "":
                print("Digite algo!")
                continue
            elif origem.isnumeric() or origem.isdecimal():
                print("Apenas letras!")
                continue
            break
        while True:
            destino = input("\nPara onde você vai: ").title()
            if destino.strip() == "":
                print("Digite algo!")
                continue
            elif destino.isnumeric() or destino.isdecimal():
                print("Apenas letras!")
                continue
            break
        
        data_viagem = ""
        horario = ""

        dia_viagem = ""
        mes_viagem = ""
        ano_viagem = ""

        data_atual = str(date.today())
        ano_atual = data_atual[0:4]
        mes_atual = data_atual[5:7]
        dia_atual = data_atual[8:10]

        # Bloco de data e tratamentos
        while True:
            hoje = input("\nVai ser hoje? \n  [1] Sim \n  [2] Não\n>>> ")
            if(hoje == '1'):
                ano_viagem = data_atual[0:4]
                mes_viagem = data_atual[5:7]
                dia_viagem = data_atual[8:10]
                break
            elif(hoje == '2'):
                print("Quando vai ser a viagem: ")

                # Valida dia
                while True:
                    dia_viagem = input("    Dia: ")
                    if dia_viagem.strip() == "":
                        print("Digite algo!")
                        continue
                    elif(not dia_viagem.isdigit()):
                        print("Apenas números inteiros!")
                        continue
                    elif int(dia_viagem) < 1 or int(dia_viagem) > 31:
                        print("Apenas valores entre 1 e 31!")
                        continue
                    else:
                        break

                # Valida mês
                while True:
                    mes_viagem = input("    Mês: ")
                    if mes_viagem.strip() == "":
                        print("Digite algo!")
                        continue
                    elif(not mes_viagem.isdigit()):
                        print("Apenas números inteiros!")
                        continue
                    elif int(mes_viagem) < 1 or int(mes_viagem) > 12:
                        print("Apenas valores entre 1 e 12!")
                        continue
                    else:
                        break
                
                # Valida ano
                while True:
                    ano_viagem = input("    Ano: ")
                    if ano_viagem.strip() == "":
                        print("Digite algo!")
                        continue
                    elif(not ano_viagem.isdigit()):
                        print("Apenas números inteiros!")
                        continue
                    elif int(ano_viagem) < int(ano_atual):
                        print("Somente anos atuais ou futuros!")
                        continue
                    else:
                        break
                
                # Verifica se a data já passou
                data_informada = date(int(ano_viagem), int(mes_viagem), int(dia_viagem))
                if data_informada < date.today():
                    print("Somente data atual ou futura!")
                    continue

                break
            else:
                print(f"{invalida_opcao}\n")
                continue
       
        data_viagem = f"{dia_viagem if len(dia_viagem) == 2 or dia_viagem[0] == '0' else f'0{dia_viagem}'}/{mes_viagem if len(mes_viagem) == 2 or mes_viagem[0] == '0' else f'0{mes_viagem}'}/{ano_viagem}"

        while True:
            hoje = input("\nVai ser agora? \n  [1] Sim \n  [2] Não\n>>> ")

            hora = ""
            minutos = ""

            if (hoje == '1'):
                hora_atual = time.strftime("%H:%M", time.localtime())
                hora = hora_atual[0:2]
                minutos = hora_atual[3:5]
                break
            elif (hoje == '2'):
                print("\nQual o horário:")

                # Valida hora
                while True:
                    hora = input("    Hora: ")
                    if hora.strip() == "":
                        print("Digite algo!")
                        continue
                    elif(not hora.isdigit()):
                        print("Apenas números inteiros!")
                        continue
                    elif int(hora) < 0 or int(hora) > 24:
                        print("Apenas números entre 1 e 24!")
                        continue
                    else:
                        break
                
                # Valida minutos
                while True:
                    minutos = input("    Minuto: ")
                    if minutos.strip() == "":
                        print("Digite algo!")
                        continue
                    elif(not minutos.isdigit()):
                        print("Apenas números inteiros!")
                        continue
                    elif (int(minutos) < 0 or int(minutos) > 59):
                        print("Apenas números entre 1 e 59!")
                        continue
                    else:
                        break

                # Verifica se o minuto já passou
                if date(int(ano_viagem), int(mes_viagem), int(dia_viagem)) == date.today():
                    h_atual = datetime.now().hour
                    m_atual = datetime.now().minute
                    if int(hora) < h_atual or (int(hora) == h_atual and int(minutos) <= m_atual):
                        print("Hora já passada!")
                        continue
                break

        horario = f"{hora if len(hora) == 2 or hora[0] == '0' else f'0{hora}'}:{minutos if len(minutos) == 2 or minutos[0] == '0' else f'0{minutos}'}"

        # Validando vagas
        while True:
            vagas = input("Quantas vagas disponíveis: ")
            if vagas.strip() == "":
                print("Digite algo!")
                continue
            elif(vagas.isalpha()):
                print("Apenas números!")
                continue
            elif(int(vagas) < 1):
                 print("Apenas uma ou mais vagas!")
                 continue
            elif(not vagas.isdecimal()):
                 print("Apenas números inteiros!")
                 continue
            else:
                 break
        

        # Validando preço por vagas
        while True:
            valor_por_vagas = input("Qual o valor de cada vaga? R$")

            if valor_por_vagas.strip() == "":
                print("Digite algo!")
                continue
            elif(valor_por_vagas.isalpha()):
                print("Apenas números!")
                continue
            elif(float(valor_por_vagas) < 0):
                print("Apenas valor positivo!")
            else:
                break
        
        caronas_cadastradas[usuario_atual] = {'origem': origem, 'destino': destino, 'data_carona': data_viagem, 'horario': horario, 'vagas': vagas, 'valor_vaga': f"{float(valor_por_vagas):.2f}"}

        print("\nCarona criada com sucesso!")
        sleep(1)
        os.system("cls" if os.name == 'nt' else 'clear')


    # Login de usuários
    if(opcao == '2' and logado == False):
        while True:
            print(f"{linhas} Login {linhas}")
            while True:
                login_email = input("Digite o seu email: ")
                if login_email.strip() == "":
                    print("Digite algo!")
                    continue
                elif login_email.find("@") == -1 or login_email.find(".") == -1:
                    print("Email inválido!")
                    continue
                elif login_email.isnumeric() or login_email.isdecimal():
                    print("Apenas letras!")
                    continue
                break

            while True:
                login_senha = pwinput.pwinput(prompt="\nDigite o sua senha: ", mask="•")
                if login_senha.strip() == "":
                    print("Digite algo!")
                    continue
                elif len(login_senha) < 8 or len(login_senha) > 15:
                    print("A senha precisa ter no mínimo 8 caracteres e no máximo 15 caracteres!")
                    continue
                break

            for i in range(len(usuarios_cadastrados)):
                if (login_email == usuarios_cadastrados[i][1]):
                    usuario_atual = i
            for usuario in usuarios_cadastrados:
                if((login_email in usuario[1]) and (login_senha in usuario[2])):
                    logado = True
            os.system("cls" if os.name == 'nt' else 'clear')

            break

        if(logado == False):
            print("Falha ao logar! Tente novamente!")
            continue

    # Pegar Carona
    elif(opcao == '2' and logado == True):
        pass

    # Listar todas as caronas
    elif (opcao == '3' and logado == True):
        print(f"{linhas} Caronas Disponíveis {linhas}\n")
        if(len(caronas_cadastradas) == 0):
            print("Sem caronas cadastradas! \n".center(70))
            sleep(3)
            os.system("cls" if os.name == 'nt' else 'clear')
        else:
            for usuario, carona in caronas_cadastradas.items():
                print(f"    Motorista: {usuarios_cadastrados[usuario][0]}".center(70))
                print(f"    Origem: {carona['origem']}".center(70))
                print(f"    Destino: {carona['destino']}".center(70))
                print(f"    Data da Carona: {carona['data_carona']}".center(70))
                print(f"    Horario: {carona['horario']}".center(70))
                print(f"    Vagas: {carona['vagas']}".center(70))
                print(f"    Valor por Vagas: R${carona['valor_vaga']}".center(70))
                print(f"{'_' * 70}\n")

        tempo = len(caronas_cadastradas * 2)
        sleep(tempo)
        os.system("cls" if os.name == 'nt' else 'clear')

    # Sair da conta
    elif(opcao == '4' and logado == True):
        logado = False
        print("Saindo da conta...")
        sleep(3)
        print("Concluido!")
        sleep(2)
        os.system("cls" if os.name == 'nt' else 'clear')


    # Fecha o programa
    elif(opcao == '0'):
        break