import os
from time import sleep
from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
from usuarios.auxiliares.validadores_usuario import validaEmail
from caronas.auxiliares.data import data
from caronas.auxiliares.resumo_caronas import resumoCaronas

def detalhesCarona(caronas_cadastradas, usuarios_cadastrados):
    print(BANCO_DE_FRASES['titulo_detalhes'])
    while True:
        motorista_email = input(BANCO_DE_FRASES['email_motorista'])
        validaEmail(motorista_email)
        break

    dia_viagem, mes_viagem, ano_viagem = data()
    
    data_viagem = f"{dia_viagem if len(dia_viagem) == 2 or dia_viagem[0] == '0' else f'0{dia_viagem}'}/{mes_viagem if len(mes_viagem) == 2 or mes_viagem[0] == '0' else f'0{mes_viagem}'}/{ano_viagem}"

    encontrado_carona = False
    for carona in caronas_cadastradas:
            if motorista_email == usuarios_cadastrados[carona['usuario_atual']]['email'] and data_viagem == carona['data_viagem']:
                encontrado_carona = True
                resumoCaronas(caronas_cadastradas, usuarios_cadastrados)
    
    os.system("cls" if os.name == 'nt' else 'clear')
    if encontrado_carona == False:
        print(f"{BANCO_DE_FRASES['nenhuma_carona']} \n".center(70))
        sleep(3)
        os.system("cls" if os.name == 'nt' else 'clear')
