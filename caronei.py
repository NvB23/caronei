import importlib.util
import os
import subprocess
import sys

# Instala a biblioteca externa pwinput e deepl se elas ainda não estiverem instaladas
if(importlib.util.find_spec("pwinput") is None):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pwinput"])
    os.system("cls" if os.name == "nt" else "clear")
if(importlib.util.find_spec("deepl") is None):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "deepl"])
    os.system("cls" if os.name == "nt" else "clear")


import pwinput
from time import sleep
from datetime import date, datetime
import time

import re
import deepl

linhas = "-" * 25

banco_frases = {
    "titulo_cadastro": f"\033[1;36m{linhas} Cadastro {linhas}",
    "titulo_usuario": "Usuário",
    "titulo_login": f"\033[1;36m{linhas} Login {linhas}",
    "titulo_reservar": f"\033[1;36m{linhas} Reservar Carona {linhas}",
    "titulo_caronas_disponiveis": f"\033[1;36m{linhas} Caronas Disponíveis {linhas}",
    "titulo_busca": f"\033[1;36m{linhas} Busca de Caronas {linhas}",
    "titulo_detalhes": f"\033[1;36m{linhas} Detalhes de uma Carona {linhas}",
    "titulo_suas_caronas": f"\033[1;36m{linhas} Suas Caronas {linhas}",
    
    "opcao_invalida": "\033[1;31mOpção Inválida!",
    "digite_algo": "\033[1;31mDigite algo!",
    "apenas_letras": "\033[1;31mApenas letras!",
    "email_invalido": "\033[1;31mEmail inválido!",
    "email_cadastrado": "\033[1;31mEmail já cadastrado!",
    "senha_invalida": "\033[1;31mA senha precisa ter no mínimo 8 caracteres e no máximo 15 caracteres!",
    "diverge_campo": "\033[1;31mDiverge do campo anterior!",
    "cadastro_sucesso": "\n\033[1;32mCadastro realizado com sucesso!",
    "login_falhou": "\033[1;31mFalha ao logar! Tente novamente!",
    "carona_criada": "\033[1;32mCarona criada com sucesso!",
    "carona_reservada": "\033[1;32mCarona reservada!",
    "sem_caronas": "\033[1;31mSem caronas cadastradas!",
    "nenhuma_carona": "\033[1;31mNenhuma carona para essa busca!",
    "reserva_cancelada": "\033[1;32mReserva cancelada!",
    "sem_reserva": "\033[1;31mVocê não tinha reserva nessa carona!",
    "carona_removida": "\033[1;32mCarona removida!",
    "nao_permissao": "\033[1;31mEsta carona não te pertence!",
    "saindo_conta": "\033[1;33mSaindo da conta...",
    "conta_saiu": "\033[1;32mConcluído!",
    
    "bem_vindo": "Bem vido ao ",
    "opcoes": "Opções",
    "menu_deslogado": "     [1] Cadastrar Usuário\n     [2] Fazer Login",
    "oferer_pegar_carona": "     [1] Oferecer Carona\n     [2] Pegar Carona",
    "menu_logado": "     [3] Listar Todas as Caronas Disponíveis\n     [4] Buscar Carona\n     [5] Mostrar Detalhes da Carona\n     [6] Mostrar Todas as Suas Caronas\n     [7] Cancelar Reserva\n     [8] Remover Carona\n     [9] Logout",
    "opcao_sair": "     [0] Fechar\n",
    "selecione_opcao": "\033[1;34mSelecione uma opção >>> \033[m",
    
    "digite_nome": "\033[1;36mDigite seu nome: ",
    "digite_email": "\n\033[1;36mDigite seu email: ",
    "digite_senha": "\033[1;36mDigite sua senha: ",
    "confirme_senha": "\033[1;36mDigite sua senha novamente: ",
    "digite_origem": "\033[1;36mDe onde você vai partir: ",
    "digite_destino": "\033[1;36mPara onde você vai: ",
    "digite_vagas": "\033[1;36mQuantas vagas disponíveis: ",
    "digite_valor": "\033[1;36mQual o valor de cada vaga? R$",
    "email_motorista": "\033[1;36mDigite o email do motorista: ",
    "origem_busca": "\033[1;36mDigite a origem buscada: ",
    "destino_busca": "\033[1;36mDigite o destino buscado: ",
    
    "hoje_viagem": "\033[1;36mVai ser hoje? \n  [1] Sim \n  [2] Não\n>>> ",
    "agora_viagem": "\033[1;36mVai ser agora? \n  [1] Sim \n  [2] Não\n>>> ",
    
    "quando_viagem": "\033[1;36mQuando vai ser a viagem: ",
    "dia_viagem": "    Dia: ",
    "mes_viagem": "    Mês: ",
    "ano_viagem": "    Ano: ",
    "hora_viagem": "    Hora: ",
    "minuto_viagem": "    Minuto: ",
    
    "apenas_numeros": "\033[1;31mApenas números!",
    "apenas_inteiros": "\033[1;31mApenas números inteiros!",
    "valor_positivo": "\033[1;31mApenas valor positivo!",
    "data_passada": "\033[1;31mSomente data atual ou futura!",
    "hora_passada": "\033[1;31mHora já passada!",
    "ano_invalido": "\033[1;31mSomente anos atuais ou futuros!",
    "mes_invalido": "\033[1;31mApenas valores entre 1 e 12!",
    "dia_invalido": "\033[1;31mApenas valores entre 1 e 31!",
    "hora_invalida": "\033[1;31mApenas números entre 1 e 24!",
    "minuto_invalido": "\033[1;31mApenas números entre 1 e 59!",
    "vagas_invalidas": "\033[1;31mApenas uma ou mais vagas!",
    
    "sem_vagas": "\033[1;31mNão há mais vagas!",
    "nao_pegar_propria": "\033[1;31mNão é permitido pegar uma carona que você criou!",
    "carona_nao_encontrada": "\033[1;31mCarona não encontrada!",
    "nenhuma_reserva": "\033[1;31mNenhuma reserva encontrada para essa carona.",

    "label_motorista": "\033[1;36mMotorista",
    "label_email_motorista": "Email do Motorista",
    "label_origem": "Origem",
    "label_destino": "Destino",
    "label_data_carona": "Data da Carona",
    "label_horario": "Horário",
    "label_vagas": "Vagas",
    "label_valor": "Valor por Vagas"
}

para_traduzir = ""

for chave, frase in banco_frases.items():
    frase_descolorida = re.sub(r"\033\[[0-9;]*m", "", frase)

    frase_descolorida = frase_descolorida.replace("\n", "##")

    para_traduzir += f"{frase_descolorida}||||"

print("""\033[1;33m
        [1] Portuguese 
        [2] English 
        [3] Spanish 
        [4] Japanese 
        [5] Arabic 
""")

sigla_lingua = ""

nao_traduz = False

while True:
    lingua_opcao = input("\033[1;33mSelect your language: ")
    if lingua_opcao.strip() == "":
        print("\033[1;31mType something!\033[1;m")
        continue
    elif(lingua_opcao == '1'):
        nao_traduz = True
        break
    elif(lingua_opcao == '2'):
        sigla_lingua = "EN-US"
        break
    elif(lingua_opcao == '3'):
        sigla_lingua = "ES"
        break
    elif(lingua_opcao == '4'):
        sigla_lingua = "JA"
        break
    elif(lingua_opcao == '5'):
        sigla_lingua = "AR"
        break
    else:
        print("\033[1;31mInvalid option!\033[1;m")
        continue
    

if nao_traduz != True:
    key = "3696baba-20cf-4935-b424-ac0653d5a413:fx"
    tradutor = deepl.Translator(key)

    traduzido = tradutor.translate_text(para_traduzir, target_lang=sigla_lingua).text
    traduzido = traduzido.split("||||")
    
    for chave, frases_traduzidas in zip(banco_frases.keys(), traduzido):
        frases_traduzidas = frases_traduzidas.replace("##", "\n")
        banco_frases[chave] = frases_traduzidas



caronei = """
   ______   ___       ____     ____     _   __   ______   ____   __
  / ____/  /   |     / __ \   / __ \   / | / /  / ____/  /  _/  / /
 / /      / /| |    / /_/ /  / / / /  /  |/ /  / __/     / /   / / 
/ /___   / ___ |   / _, _/  / /_/ /  / /|  /  / /___   _/ /   /_/  
\____/  /_/  |_|  /_/ |_|   \____/  /_/ |_/  /_____/  /___/  (_)  
"""

usuarios_cadastrados = []
caronas_cadastradas = []
caronas_reservadas = {}
usuario_atual = -1
logado = False
logout_opcao = ""
cad_log_opcao = ""
invalida_opcao = banco_frases["opcao_invalida"]

while True:
    # Mostra sessão de usuário com nome
    if(logado == True and usuario_atual != -1):
        print(f"\n\n\033[1;34m{linhas*2}\n") 

        str_usuario = banco_frases['titulo_usuario']

        nome_estilizado = f"{str_usuario}: {usuarios_cadastrados[usuario_atual][0]}".center(50).upper()
        print(f"\033[3;34m{nome_estilizado}\033[m")
        print(f"\n\033[1;34m{linhas*2}")
    
    str_bem_vindo = banco_frases['bem_vindo']
    str_opcoes = banco_frases['opcoes']

    # Painel de boas vindas e opções
    print(f"\n\033[1;34m{str_bem_vindo}\n\n{caronei}\n\n\033[1;34m{str_opcoes}:\n")
    if(logado == False):
        print(banco_frases['menu_deslogado'])
    else:
        print(banco_frases['oferer_pegar_carona'])
    if(logado == True):
        print(banco_frases['menu_logado'])
    print(banco_frases['opcao_sair'])

    opcao = input(banco_frases['selecione_opcao'])
    print("\n")

    # Valida se o usuário não digitar nada
    if(opcao.strip() == ""):
        print(banco_frases['digite_algo'])
        sleep(1)
        os.system("cls" if os.name == 'nt' else 'clear')
        continue

    # Valida se não vai digitar nada fora do padrão
    elif(opcao not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]):
        print(invalida_opcao)
        sleep(1)
        os.system("cls" if os.name == 'nt' else 'clear')
        continue

    # Cadastro de usuários e validações
    elif(opcao == '1' and logado == False):
        print(banco_frases['titulo_cadastro'])

        while True:
            nome = input(banco_frases['digite_nome']).title()
            if nome.strip() == "":
                print(banco_frases['digite_algo'])
                continue
            elif nome.isnumeric() or nome.isdecimal():
                print(banco_frases['apenas_letras'])
                continue
            elif not all(palavra.isalpha() for palavra in nome.split()):
                print(banco_frases['apenas_letras'])
                continue
            break
        
        while True:
            email = input(banco_frases['digite_email'])
            if email.strip() == "":
                print(banco_frases['digite_algo'])
                continue
            elif email.find("@") == -1 or email.find(".") == -1:
                print(banco_frases['email_invalido'])
                continue
            elif email.isnumeric() or email.isdecimal():
                print(banco_frases['apenas_letras'])
                continue
            cadastrado = False
            for usu in usuarios_cadastrados:
                if(email == usu[1]):
                    print(banco_frases['email_cadastrado'])
                    cadastrado = True
                    break

            if(cadastrado == True):
                continue

            break

        while True:
            str_senha = banco_frases['digite_senha']

            senha = pwinput.pwinput(prompt=f"\n{str_senha}", mask="•")
            if senha.strip() == "":
                print(banco_frases['digite_algo'])
                continue
            elif len(senha) < 8 or len(senha) > 15:
                print(banco_frases['senha_invalida'])
                continue
            break

        while True:
            str_senha_novamente = banco_frases['confirme_senha']
            confirmar_senha = pwinput.pwinput(prompt=f"\n{str_senha_novamente}", mask="•")
            if(confirmar_senha != senha):
                print(banco_frases['diverge_campo'])
                continue
            break

        print(banco_frases['cadastro_sucesso'])
        sleep(1)

        usuarios_cadastrados.append([nome, email, senha])
        os.system("cls" if os.name == 'nt' else 'clear')
            

    # Oferecer Carona e validações
    elif(opcao == '1' and logado == True):
        while True:      
            origem = input(banco_frases['digite_origem']).title()
            if origem.strip() == "":
                print(banco_frases['digite_algo'])
                continue
            elif origem.isnumeric() or origem.isdecimal():
                print(banco_frases['apenas_letras'])
                continue
            break
        while True:
            destino = input(banco_frases['digite_destino']).title()
            if destino.strip() == "":
                print(banco_frases['digite_algo'])
                continue
            elif destino.isnumeric() or destino.isdecimal():
                print(banco_frases['apenas_letras'])
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
            hoje = input(banco_frases['hoje_viagem'])
            if(hoje == '1'):
                ano_viagem = data_atual[0:4]
                mes_viagem = data_atual[5:7]
                dia_viagem = data_atual[8:10]
                break
            elif(hoje == '2'):
                print(banco_frases['quando_viagem'])

                # Valida dia
                while True:
                    dia_viagem = input(banco_frases['dia_viagem'])
                    if dia_viagem.strip() == "":
                        print(banco_frases['digite_algo'])
                        continue
                    elif(not dia_viagem.isdigit()):
                        print(banco_frases['apenas_inteiros'])
                        continue
                    elif int(dia_viagem) < 1 or int(dia_viagem) > 31:
                        print(banco_frases['dia_invalido'])
                        continue
                    else:
                        break

                # Valida mês
                while True:
                    mes_viagem = input(banco_frases['mes_viagem'])
                    if mes_viagem.strip() == "":
                        print(banco_frases['digite_algo'])
                        continue
                    elif(not mes_viagem.isdigit()):
                        print(banco_frases['apenas_inteiros'])
                        continue
                    elif int(mes_viagem) < 1 or int(mes_viagem) > 12:
                        print(banco_frases['mes_invalido'])
                        continue
                    else:
                        break
                
                # Valida ano
                while True:
                    ano_viagem = input(banco_frases['ano_viagem'])
                    if ano_viagem.strip() == "":
                        print(banco_frases['digite_algo'])
                        continue
                    elif(not ano_viagem.isdigit()):
                        print(banco_frases['apenas_inteiros'])
                        continue
                    elif int(ano_viagem) < int(ano_atual):
                        print(banco_frases['ano_invalido'])
                        continue
                    else:
                        break
                
                # Verifica se a data já passou
                data_informada = date(int(ano_viagem), int(mes_viagem), int(dia_viagem))
                if data_informada < date.today():
                    print(banco_frases['data_passada'])
                    continue

                break
            else:
                print(f"{invalida_opcao}\n")
                continue
       
        data_viagem = f"{dia_viagem if len(dia_viagem) == 2 or dia_viagem[0] == '0' else f'0{dia_viagem}'}/{mes_viagem if len(mes_viagem) == 2 or mes_viagem[0] == '0' else f'0{mes_viagem}'}/{ano_viagem}"

        # Bloco hora e validações
        while True:
            hoje = input(banco_frases['agora_viagem'])

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
                    hora = input(banco_frases['hora_viagem'])
                    if hora.strip() == "":
                        print(banco_frases['digite_algo'])
                        continue
                    elif(not hora.isdigit()):
                        print(banco_frases['apenas_inteiros'])
                        continue
                    elif int(hora) < 0 or int(hora) > 24:
                        print(banco_frases['hora_invalida'])
                        continue
                    else:
                        break
                
                # Valida minutos
                while True:
                    minutos = input(banco_frases['minuto_viagem'])
                    if minutos.strip() == "":
                        print(banco_frases['digite_algo'])
                        continue
                    elif(not minutos.isdigit()):
                        print(banco_frases['apenas_inteiros'])
                        continue
                    elif (int(minutos) < 0 or int(minutos) > 59):
                        print(banco_frases['minuto_invalido'])
                        continue
                    else:
                        break

                # Verifica se o minuto já passou
                if date(int(ano_viagem), int(mes_viagem), int(dia_viagem)) == date.today():
                    h_atual = datetime.now().hour
                    m_atual = datetime.now().minute
                    if int(hora) < h_atual or (int(hora) == h_atual and int(minutos) <= m_atual):
                        print(banco_frases['hora_passada'])
                        continue
                break

        horario = f"{hora if len(hora) == 2 or hora[0] == '0' else f'0{hora}'}:{minutos if len(minutos) == 2 or minutos[0] == '0' else f'0{minutos}'}"

        # Validando vagas
        while True:
            vagas = input(banco_frases['digite_vagas'])
            if vagas.strip() == "":
                print(banco_frases['digite_algo'])
                continue
            elif(vagas.isalpha()):
                print(banco_frases['apenas_numeros'])
                continue
            elif(int(vagas) < 1):
                 print(banco_frases['vagas_invalidas'])
                 continue
            elif(not vagas.isdecimal()):
                 print(banco_frases['apenas_inteiros'])
                 continue
            else:
                 break
        

        # Validando preço por vagas
        while True:
            valor_por_vagas = input(banco_frases['digite_valor'])

            if valor_por_vagas.strip() == "":
                print(banco_frases['digite_algo'])
                continue
            elif(valor_por_vagas.isalpha()):
                print(banco_frases['apenas_numeros'])
                continue
            elif(float(valor_por_vagas) < 0):
                print(banco_frases['valor_positivo'])
            else:
                break
        
        caronas_cadastradas.append([usuario_atual, origem, destino, data_viagem, horario, int(vagas), f"{float(valor_por_vagas):.2f}"])

        print(f"\n{banco_frases['carona_criada']}")
        sleep(1)
        os.system("cls" if os.name == 'nt' else 'clear')


    # Login de usuários
    if(opcao == '2' and logado == False):
        while True:
            login_email = ""
            print(banco_frases['titulo_login'])
            while True:
                login_email = input(banco_frases['digite_email'])
                if login_email.strip() == "":
                    print(banco_frases['digite_algo'])
                    continue
                elif login_email.find("@") == -1 or login_email.find(".") == -1:
                    print(banco_frases['email_invalido'])
                    continue
                elif login_email.isnumeric() or login_email.isdecimal():
                    print(banco_frases['apenas_letras'])
                    continue
                break

            while True:
                login_senha = pwinput.pwinput(prompt=f"\n{banco_frases['digite_senha']}", mask="•")
                if login_senha.strip() == "":
                    print(banco_frases['digite_algo'])
                    continue
                elif len(login_senha) < 8 or len(login_senha) > 15:
                    print(banco_frases['senha_invalida'])
                    continue
                break

            for i in range(len(usuarios_cadastrados)):
                if (login_email == usuarios_cadastrados[i][1]):
                    usuario_atual = i
            for usuario in usuarios_cadastrados:
                if((login_email == usuario[1]) and (login_senha == usuario[2])):
                    logado = True
            os.system("cls" if os.name == 'nt' else 'clear')

            break

        if(logado == False):
            print(banco_frases['login_falhou'])
            continue

    # Pegar Carona
    elif(opcao == '2' and logado == True):
        print(banco_frases['titulo_reservar'])
        while True:
            motorista_email = input(banco_frases['email_motorista'])
            if motorista_email.strip() == "":
                print(banco_frases['digite_algo'])
                continue
            elif motorista_email.find("@") == -1 or motorista_email.find(".") == -1:
                print(banco_frases['email_invalido'])
                continue
            elif motorista_email.isnumeric() or motorista_email.isdecimal():
                print(banco_frases['apenas_letras'])
                continue
            break

        while True:
            hoje = input(banco_frases['hoje_viagem'])
            if(hoje == '1'):
                data_atual = str(date.today())
                ano_viagem = data_atual[0:4]
                mes_viagem = data_atual[5:7]
                dia_viagem = data_atual[8:10]
                break
            elif(hoje == '2'):
                print(banco_frases['quando_viagem'])

                # Valida dia
                while True:
                    dia_viagem = input(banco_frases['dia_viagem'])
                    if dia_viagem.strip() == "":
                        print(banco_frases['digite_algo'])
                        continue
                    elif(not dia_viagem.isdigit()):
                        print(banco_frases['apenas_inteiros'])
                        continue
                    elif int(dia_viagem) < 1 or int(dia_viagem) > 31:
                        print(banco_frases['dia_invalido'])
                        continue
                    else:
                        break

                # Valida mês
                while True:
                    mes_viagem = input(banco_frases['mes_viagem'])
                    if mes_viagem.strip() == "":
                        print(banco_frases['digite_algo'])
                        continue
                    elif(not mes_viagem.isdigit()):
                        print(banco_frases['apenas_inteiros'])
                        continue
                    elif int(mes_viagem) < 1 or int(mes_viagem) > 12:
                        print(banco_frases['mes_invalido'])
                        continue
                    else:
                        break
                
                # Valida ano
                while True:
                    ano_viagem = input(banco_frases['ano_viagem'])
                    if ano_viagem.strip() == "":
                        print(banco_frases['digite_algo'])
                        continue
                    elif(not ano_viagem.isdigit()):
                        print(banco_frases['apenas_inteiros'])
                        continue
                    elif int(ano_viagem) < int(ano_atual):
                        print(banco_frases['ano_invalido'])
                        continue
                    else:
                        break
                
                # Verifica se a data já passou
                data_informada = date(int(ano_viagem), int(mes_viagem), int(dia_viagem))
                if data_informada < date.today():
                    print(banco_frases['data_passada'])
                    continue
                break
            else:
                print(f"{invalida_opcao}\n")
                continue
       
        data_viagem = f"{dia_viagem if len(dia_viagem) == 2 or dia_viagem[0] == '0' else f'0{dia_viagem}'}/{mes_viagem if len(mes_viagem) == 2 or mes_viagem[0] == '0' else f'0{mes_viagem}'}/{ano_viagem}"

        informações_validadas = False
        for carona in caronas_cadastradas:
            if (not usuarios_cadastrados[usuario_atual][1] == motorista_email) and (data_viagem == carona[3]) and (motorista_email == usuarios_cadastrados[carona[0]][1]):
                informações_validadas = True
                carona[5] -= 1
                if(motorista_email, data_viagem) not in caronas_reservadas:
                    caronas_reservadas[(motorista_email, data_viagem)] = []
                caronas_reservadas[(motorista_email, data_viagem)].append(usuario_atual)
                print(f"\n{banco_frases['carona_reservada']}")
                sleep(3)
                os.system("cls" if os.name == 'nt' else 'clear')
                break
            elif carona[5] == 0:
                print(banco_frases['sem_vagas'])
                informações_validadas = False
            elif usuarios_cadastrados[usuario_atual][1] == motorista_email:
                print(banco_frases['nao_pegar_propria'])
                informações_validadas = False
            else:
                informações_validadas = False
                print(banco_frases['carona_nao_encontrada'])
        
        if informações_validadas == False:
            sleep(3)
            os.system("cls" if os.name == 'nt' else 'clear')
            continue
        

    # Listar todas as caronas
    elif (opcao == '3' and logado == True):
        print(banco_frases['titulo_caronas_disponiveis'] + "\n")
        if(len(caronas_cadastradas) == 0):
            print(f"{banco_frases['sem_caronas']} \n".center(70))
            sleep(3)
            os.system("cls" if os.name == 'nt' else 'clear')

        else:
            str_motorista = banco_frases['label_motorista']
            str_email_motorista = banco_frases['label_email_motorista']
            str_origem = banco_frases['label_origem']
            str_destino = banco_frases['label_destino']
            str_data_carona = banco_frases['label_data_carona']
            str_horario = banco_frases['label_horario']
            str_vagas = banco_frases['label_vagas']
            str_valor = banco_frases['label_valor']

            for carona in caronas_cadastradas:
                print(f"    {str_motorista}: {carona[0]}".center(70))
                print(f"    {str_email_motorista}: {usuarios_cadastrados[carona[0]][1]}".center(70))
                print(f"    {str_origem}: {carona[1]}".center(70))
                print(f"    {str_destino}: {carona[2]}".center(70))
                print(f"    {str_data_carona}: {carona[3]}".center(70))
                print(f"    {str_horario}: {carona[4]}".center(70))
                print(f"    {str_vagas}: {carona[5]}".center(70))
                print(f"    {str_valor}: R${carona[6]}".center(70))
                print(f"{'_' * 70}\n")

            tempo = len(caronas_cadastradas) * 4
            sleep(tempo)
            os.system("cls" if os.name == 'nt' else 'clear')
    
    # Busca todas a caronas
    elif(opcao == '4' and logado == True):
        print(banco_frases['titulo_busca'])
        while True:      
            origem_busca = input(f"\n{banco_frases['origem_busca']}").title()
            if origem_busca.strip() == "":
                print(banco_frases['digite_algo'])
                continue
            elif origem_busca.isnumeric() or origem_busca.isdecimal():
                print(banco_frases['apenas_letras'])
                continue
            break
        while True:
            destino_busca = input(f"\n{banco_frases['destino_busca']}").title()
            if destino_busca.strip() == "":
                print(banco_frases['digite_algo'])
                continue
            elif destino_busca.isnumeric() or destino_busca.isdecimal():
                print(banco_frases['apenas_letras'])
                continue
            break
        print("\n")
        encontrado_carona = False
        cont = 0
        str_motorista = banco_frases['label_motorista']
        str_email_motorista = banco_frases['label_email_motorista']
        str_origem = banco_frases['label_origem']
        str_destino = banco_frases['label_destino']
        str_data_carona = banco_frases['label_data_carona']
        str_horario = banco_frases['label_horario']
        str_vagas = banco_frases['label_vagas']
        str_valor = banco_frases['label_valor']

        for carona in caronas_cadastradas:
            if origem_busca == carona[1] and destino_busca == carona[2]:
                encontrado_carona = True
                print(f"    {str_motorista}: {carona[0]}".center(70))
                print(f"    {str_email_motorista}: {usuarios_cadastrados[carona[0]][1]}".center(70))
                print(f"    {str_origem}: {carona[1]}".center(70))
                print(f"    {str_destino}: {carona[2]}".center(70))
                print(f"    {str_data_carona}: {carona[3]}".center(70))
                print(f"    {str_horario}: {carona[4]}".center(70))
                print(f"    {str_vagas}: {carona[5]}".center(70))
                print(f"    {str_valor}: R${carona[6]}".center(70))
                print(f"{'_' * 70}\n")

                cont += 1

        sleep(cont * 3)
        os.system("cls" if os.name == 'nt' else 'clear')

        if encontrado_carona == False:
            print(f"{banco_frases['nenhuma_carona']} \n".center(70))
            sleep(3)
            os.system("cls" if os.name == 'nt' else 'clear')
            continue

    # Mostrar Detalhes de uma Carona
    elif(opcao == '5' and logado == True):
        print(banco_frases['titulo_detalhes'])
        while True:
            motorista_email = input(banco_frases['email_motorista'])
            if motorista_email.strip() == "":
                print(banco_frases['digite_algo'])
                continue
            elif motorista_email.find("@") == -1 or motorista_email.find(".") == -1:
                print(banco_frases['email_invalido'])
                continue
            elif motorista_email.isnumeric() or motorista_email.isdecimal():
                print(banco_frases['apenas_letras'])
                continue
            break

        while True:
            hoje = input(banco_frases['hoje_viagem'])
            if(hoje == '1'):
                data_atual = str(date.today())
                ano_viagem = data_atual[0:4]
                mes_viagem = data_atual[5:7]
                dia_viagem = data_atual[8:10]
                break
            elif(hoje == '2'):
                print(banco_frases['quando_viagem'])

                # Valida dia
                while True:
                    dia_viagem = input(banco_frases['dia_viagem'])
                    if dia_viagem.strip() == "":
                        print(banco_frases['digite_algo'])
                        continue
                    elif(not dia_viagem.isdigit()):
                        print(banco_frases['apenas_inteiros'])
                        continue
                    elif int(dia_viagem) < 1 or int(dia_viagem) > 31:
                        print(banco_frases['dia_invalido'])
                        continue
                    else:
                        break

                # Valida mês
                while True:
                    mes_viagem = input(banco_frases['mes_viagem'])
                    if mes_viagem.strip() == "":
                        print(banco_frases['digite_algo'])
                        continue
                    elif(not mes_viagem.isdigit()):
                        print(banco_frases['apenas_inteiros'])
                        continue
                    elif int(mes_viagem) < 1 or int(mes_viagem) > 12:
                        print(banco_frases['mes_invalido'])
                        continue
                    else:
                        break
                
                # Valida ano
                while True:
                    ano_viagem = input(banco_frases['ano_viagem'])
                    if ano_viagem.strip() == "":
                        print(banco_frases['digite_algo'])
                        continue
                    elif(not ano_viagem.isdigit()):
                        print(banco_frases['apenas_inteiros'])
                        continue
                    elif int(ano_viagem) < int(ano_atual):
                        print(banco_frases['ano_invalido'])
                        continue
                    else:
                        break
                
                # Verifica se a data já passou
                data_informada = date(int(ano_viagem), int(mes_viagem), int(dia_viagem))
                if data_informada < date.today():
                    print(banco_frases['data_passada'])
                    continue
                break
            else:
                print(f"{invalida_opcao}\n")
                continue
       
        data_viagem = f"{dia_viagem if len(dia_viagem) == 2 or dia_viagem[0] == '0' else f'0{dia_viagem}'}/{mes_viagem if len(mes_viagem) == 2 or mes_viagem[0] == '0' else f'0{mes_viagem}'}/{ano_viagem}"

        encontrado_carona = False
        cont = 0
        str_motorista = banco_frases['label_motorista']
        str_email_motorista = banco_frases['label_email_motorista']
        str_origem = banco_frases['label_origem']
        str_destino = banco_frases['label_destino']
        str_data_carona = banco_frases['label_data_carona']
        str_horario = banco_frases['label_horario']
        str_vagas = banco_frases['label_vagas']
        str_valor = banco_frases['label_valor']
        for carona in caronas_cadastradas:
            if motorista_email == usuarios_cadastrados[carona[0]][1] and data_viagem == carona[3]:
                encontrado_carona = True
                print(f"    {str_motorista}: {carona[0]}".center(70))
                print(f"    {str_email_motorista}: {usuarios_cadastrados[carona[0]][1]}".center(70))
                print(f"    {str_origem}: {carona[1]}".center(70))
                print(f"    {str_destino}: {carona[2]}".center(70))
                print(f"    {str_data_carona}: {carona[3]}".center(70))
                print(f"    {str_horario}: {carona[4]}".center(70))
                print(f"    {str_vagas}: {carona[5]}".center(70))
                print(f"    {str_valor}: R${carona[6]}".center(70))
                print(f"{'_' * 70}\n")

                cont += 1

        sleep(cont * 3)
        os.system("cls" if os.name == 'nt' else 'clear')
        if encontrado_carona == False:
            print(f"{banco_frases['nenhuma_carona']} \n".center(70))
            sleep(3)
            os.system("cls" if os.name == 'nt' else 'clear')
            continue

    # Exibe caronas criadas pelo usuario
    elif(opcao == '6' and logado == True):
        print(banco_frases['titulo_suas_caronas'])
        encontrado_carona = False
        cont = 0

        str_motorista = banco_frases['label_motorista']
        str_email_motorista = banco_frases['label_email_motorista']
        str_origem = banco_frases['label_origem']
        str_destino = banco_frases['label_destino']
        str_data_carona = banco_frases['label_data_carona']
        str_horario = banco_frases['label_horario']
        str_vagas = banco_frases['label_vagas']
        str_valor = banco_frases['label_valor']

        for carona in caronas_cadastradas:
            if carona[0] == usuario_atual:
                encontrado_carona = True
                str_motorista = banco_frases['label_motorista']
                str_email_motorista = banco_frases['label_email_motorista']
                str_origem = banco_frases['label_origem']
                str_destino = banco_frases['label_destino']
                str_data_carona = banco_frases['label_data_carona']
                str_horario = banco_frases['label_horario']
                str_vagas = banco_frases['label_vagas']
                str_valor = banco_frases['label_valor']
                print(f"{'_' * 70}\n")

                cont += 1

        sleep(cont * 3)
        os.system("cls" if os.name == 'nt' else 'clear')
        if encontrado_carona == False:
            print(f"{banco_frases['nenhuma_carona']} \n".center(70))
            sleep(3)
            os.system("cls" if os.name == 'nt' else 'clear')
            continue
    
    elif(opcao == '7' and logado == True):
        while True:
            motorista_email = input(banco_frases['email_motorista'])
            if motorista_email.strip() == "":
                print(banco_frases['digite_algo'])
                continue
            elif motorista_email.find("@") == -1 or motorista_email.find(".") == -1:
                print(banco_frases['email_invalido'])
                continue
            elif motorista_email.isnumeric() or motorista_email.isdecimal():
                print(banco_frases['apenas_letras'])
                continue
            break

        while True:
            hoje = input(banco_frases['hoje_viagem'])
            if(hoje == '1'):
                data_atual = str(date.today())
                ano_viagem = data_atual[0:4]
                mes_viagem = data_atual[5:7]
                dia_viagem = data_atual[8:10]
                break
            elif(hoje == '2'):
                print(banco_frases['quando_viagem'])

                # Valida dia
                while True:
                    dia_viagem = input(banco_frases['dia_viagem'])
                    if dia_viagem.strip() == "":
                        print(banco_frases['digite_algo'])
                        continue
                    elif(not dia_viagem.isdigit()):
                        print(banco_frases['apenas_inteiros'])
                        continue
                    elif int(dia_viagem) < 1 or int(dia_viagem) > 31:
                        print(banco_frases['dia_invalido'])
                        continue
                    else:
                        break

                # Valida mês
                while True:
                    mes_viagem = input(banco_frases['mes_viagem'])
                    if mes_viagem.strip() == "":
                        print(banco_frases['digite_algo'])
                        continue
                    elif(not mes_viagem.isdigit()):
                        print(banco_frases['apenas_inteiros'])
                        continue
                    elif int(mes_viagem) < 1 or int(mes_viagem) > 12:
                        print(banco_frases['mes_invalido'])
                        continue
                    else:
                        break
                
                # Valida ano
                while True:
                    ano_viagem = input(banco_frases['ano_viagem'])
                    if ano_viagem.strip() == "":
                        print(banco_frases['digite_algo'])
                        continue
                    elif(not ano_viagem.isdigit()):
                        print(banco_frases['apenas_inteiros'])
                        continue
                    elif int(ano_viagem) < int(ano_atual):
                        print(banco_frases['ano_invalido'])
                        continue
                    else:
                        break
                
                # Verifica se a data já passou
                data_informada = date(int(ano_viagem), int(mes_viagem), int(dia_viagem))
                if data_informada < date.today():
                    print(banco_frases['data_passada'])
                    continue
                break
            else:
                print(f"{invalida_opcao}\n")
                continue
       
        data_viagem = f"{dia_viagem if len(dia_viagem) == 2 or dia_viagem[0] == '0' else f'0{dia_viagem}'}/{mes_viagem if len(mes_viagem) == 2 or mes_viagem[0] == '0' else f'0{mes_viagem}'}/{ano_viagem}"

        removida = False
        for carona in caronas_cadastradas:
            if motorista_email == usuarios_cadastrados[carona[0]][1] and data_viagem == carona[3]:
                if (motorista_email, data_viagem) in caronas_reservadas:
                    carona[5] += 1
                    lista_de_reservas = caronas_reservadas[(motorista_email, data_viagem)]
                    if usuario_atual in lista_de_reservas:
                        lista_de_reservas.remove(usuario_atual)
                        removida = True
                        print(banco_frases['reserva_cancelada'])
                    else:
                        print(banco_frases['sem_reserva'])
            else:
                print(banco_frases['nenhuma_reserva'])

            sleep(3)
            os.system("cls" if os.name == 'nt' else 'clear')
            break

        if(removida == False):
            print("Falha ao remover reserva!")
            sleep(3)
            os.system("cls" if os.name == 'nt' else 'clear')

    # Remover carona
    elif(opcao == '8' and logado == True):
        for carona in caronas_cadastradas:
            if(usuario_atual == carona[0]):
                while True:
                    hoje = input(banco_frases['hoje_viagem'])
                    if(hoje == '1'):
                        data_atual = str(date.today())
                        ano_viagem = data_atual[0:4]
                        mes_viagem = data_atual[5:7]
                        dia_viagem = data_atual[8:10]
                        break
                    elif(hoje == '2'):
                        print(banco_frases['quando_viagem'])

                        # Valida dia
                        while True:
                            dia_viagem = input(banco_frases['dia_viagem'])
                            if dia_viagem.strip() == "":
                                print(banco_frases['digite_algo'])
                                continue
                            elif(not dia_viagem.isdigit()):
                                print(banco_frases['apenas_inteiros'])
                                continue
                            elif int(dia_viagem) < 1 or int(dia_viagem) > 31:
                                print(banco_frases['dia_invalido'])
                                continue
                            else:
                                break

                        # Valida mês
                        while True:
                            mes_viagem = input(banco_frases['mes_viagem'])
                            if mes_viagem.strip() == "":
                                print(banco_frases['digite_algo'])
                                continue
                            elif(not mes_viagem.isdigit()):
                                print(banco_frases['apenas_inteiros'])
                                continue
                            elif int(mes_viagem) < 1 or int(mes_viagem) > 12:
                                print(banco_frases['mes_invalido'])
                                continue
                            else:
                                break
                        
                        # Valida ano
                        while True:
                            ano_viagem = input(banco_frases['ano_viagem'])
                            if ano_viagem.strip() == "":
                                print(banco_frases['digite_algo'])
                                continue
                            elif(not ano_viagem.isdigit()):
                                print(banco_frases['apenas_inteiros'])
                                continue
                            elif int(ano_viagem) < int(ano_atual):
                                print(banco_frases['ano_invalido'])
                                continue
                            else:
                                break
                        
                        # Verifica se a data já passou
                        data_informada = date(int(ano_viagem), int(mes_viagem), int(dia_viagem))
                        if data_informada < date.today():
                            print(banco_frases['data_passada'])
                            continue
                        break
                    else:
                        print(f"{invalida_opcao}\n")
                        continue
            
                data_viagem = f"{dia_viagem if len(dia_viagem) == 2 or dia_viagem[0] == '0' else f'0{dia_viagem}'}/{mes_viagem if len(mes_viagem) == 2 or mes_viagem[0] == '0' else f'0{mes_viagem}'}/{ano_viagem}"

                for car in caronas_cadastradas:
                    if car[3] == data_viagem:
                        caronas_cadastradas.remove(car)
                        print(banco_frases['carona_removida'])
                sleep(3)
                os.system("cls" if os.name == 'nt' else 'clear')

            else:
                print(banco_frases['nao_permissao'])
                sleep(3)
                os.system("cls" if os.name == 'nt' else 'clear')
                continue

    # Sair da conta
    elif(opcao == '9' and logado == True):
        logado = False
        print(banco_frases['saindo_conta'])
        sleep(2)
        print(banco_frases['conta_saiu'])
        sleep(1)
        os.system("cls" if os.name == 'nt' else 'clear')


    # Fecha o programa
    elif(opcao == '0'):
        os.system("cls" if os.name == 'nt' else 'clear')
        break