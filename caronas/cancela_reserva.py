from time import sleep
import os
from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
from usuarios.auxiliares.validadores_usuario import validaEmail
from caronas.auxiliares.data import data

def cancelaReserva(caronas_cadastradas,saldo, usuarios_cadastrados, caronas_reservadas, usuario_atual):
    while True:
        motorista_email = input(BANCO_DE_FRASES['email_motorista'])
        validaEmail(motorista_email)
        break

    dia_viagem, mes_viagem, ano_viagem = data()

    data_viagem = f"{dia_viagem if len(dia_viagem) == 2 or dia_viagem[0] == '0' else f'0{dia_viagem}'}/{mes_viagem if len(mes_viagem) == 2 or mes_viagem[0] == '0' else f'0{mes_viagem}'}/{ano_viagem}"

    removida = False
    for carona in caronas_cadastradas:
        if motorista_email == usuarios_cadastrados[carona['usuario_atual']]['email'] and data_viagem == carona['data_viagem']:
            if (motorista_email, data_viagem) in caronas_reservadas:
                carona['vagas'] += 1
                lista_de_reservas = caronas_reservadas[(motorista_email, data_viagem)]
                if usuario_atual in lista_de_reservas:
                    lista_de_reservas.remove(usuario_atual)
                    saldo[usuario_atual] += float(carona['valor'])
                    saldo[carona['usuario_atual']] -= float(carona['valor'])
                    removida = True
                    print(BANCO_DE_FRASES['reserva_cancelada'])
                else:
                    print(BANCO_DE_FRASES['sem_reserva'])
        else:
            print(BANCO_DE_FRASES['nenhuma_reserva'])

        sleep(3)
        os.system("cls" if os.name == 'nt' else 'clear')
        break

    if(removida == False):
        print("Falha ao remover reserva!")
        sleep(3)
        os.system("cls" if os.name == 'nt' else 'clear')
    
    return saldo, caronas_reservadas