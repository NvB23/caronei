from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
from datetime import date, datetime
import time
from caronas.auxiliares.validadores_caronas import validaHoras, validaMinutos

def hora(dia_viagem, mes_viagem, ano_viagem):
    while True:
        hora_opcao = input(BANCO_DE_FRASES['agora_viagem'])

        if (hora_opcao == '1'):
            hora_atual = time.strftime("%H:%M", time.localtime())
            horas = hora_atual[0:2]
            minutos = hora_atual[3:5]
            break
        elif (hora_opcao == '2'):
            print("\nQual o horário:")

            # Pega hora
            while True:
                horas = input(BANCO_DE_FRASES['hora_viagem'])
                if validaHoras(horas) == False:
                    continue
                break
            
            # Pega minutos
            while True:
                minutos = input(BANCO_DE_FRASES['minuto_viagem'])
                if validaMinutos(minutos) == False:
                    continue
                break

            # Verifica se o minuto já passou
            if date(int(ano_viagem), int(mes_viagem), int(dia_viagem)) == date.today():
                h_atual = datetime.now().hour
                m_atual = datetime.now().minute
                if int(horas) < h_atual or (int(horas) == h_atual and int(minutos) < m_atual):
                    print(BANCO_DE_FRASES['hora_passada'])
                    continue
            break
    return horas, minutos