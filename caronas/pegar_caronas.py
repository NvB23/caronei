from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
from time import sleep
import os
from usuarios.auxiliares.validadores_usuario import validaEmail
from caronas.auxiliares.data import data

def pegarCaronas(saldo, usuario_atual, caronas_cadastradas, usuarios_cadastrados, caronas_reservadas):
    print(BANCO_DE_FRASES['titulo_reservar'])
    while True:
        motorista_email = input(BANCO_DE_FRASES['email_motorista'])
        if validaEmail(motorista_email) == False:
            continue
        break

    dia_viagem, mes_viagem, ano_viagem = data()
    
    data_viagem = f"{dia_viagem if len(dia_viagem) == 2 or dia_viagem[0] == '0' else f'0{dia_viagem}'}/{mes_viagem if len(mes_viagem) == 2 or mes_viagem[0] == '0' else f'0{mes_viagem}'}/{ano_viagem}"

    informações_validadas = False
    for carona in caronas_cadastradas:
        if (not usuarios_cadastrados[usuario_atual]['email'] == motorista_email) and (data_viagem == carona['data_viagem']) and (motorista_email == usuarios_cadastrados[carona['usuario_atual']]['email']) and saldo[usuario_atual] >= float(carona['valor']) :
            informações_validadas = True
            carona['vagas'] -= 1
            if(motorista_email, data_viagem) not in caronas_reservadas:
                caronas_reservadas[(motorista_email, data_viagem)] = []
            caronas_reservadas[(motorista_email, data_viagem)].append(usuario_atual)
            valor = float(carona['valor'])
            saldo[usuario_atual] -= valor
            saldo[carona['usuario_atual']] += valor
            print(f"\n{BANCO_DE_FRASES['carona_reservada']}")
            sleep(3)
            os.system("cls" if os.name == 'nt' else 'clear')
            break
        elif saldo[usuario_atual] < float(carona['valor']):
            print(BANCO_DE_FRASES['sem_saldo'])
        elif carona['vagas'] == 0:
            print(BANCO_DE_FRASES['sem_vagas'])
            informações_validadas = False
        elif usuarios_cadastrados[usuario_atual]['email'] == motorista_email:
            print(BANCO_DE_FRASES['nao_pegar_propria'])
            informações_validadas = False
        else:
            informações_validadas = False
            print(BANCO_DE_FRASES['carona_nao_encontrada'])
    
    if informações_validadas == False:
        sleep(3)
        os.system("cls" if os.name == 'nt' else 'clear')
    return saldo, caronas_reservadas