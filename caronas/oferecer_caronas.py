from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
import os
from time import sleep
from caronas.auxiliares.validadores_caronas import validaOrigemDestino, validaVagas, validaValorPorVagas
from caronas.auxiliares.data import data
from caronas.auxiliares.hora import hora

def oferecerCaronas(usuario_atual, caronas_cadastradas, vagas_total: list):
    # Pega origem
    while True:      
        origem = input(BANCO_DE_FRASES['digite_origem']).title()
        if validaOrigemDestino(origem) == False:
            continue
        break
    # Pega destino
    while True:
        destino = input(BANCO_DE_FRASES['digite_destino']).title()
        if validaOrigemDestino(destino) == False:
            continue
        break

    # Pega a data da viagem
    dia_viagem, mes_viagem, ano_viagem = data()
    
    data_viagem = f"{dia_viagem if len(dia_viagem) == 2 or dia_viagem[0] == '0' else f'0{dia_viagem}'}/{mes_viagem if len(mes_viagem) == 2 or mes_viagem[0] == '0' else f'0{mes_viagem}'}/{ano_viagem}"

    # Pega o horario da viagem
    horas, minutos = hora(dia_viagem, mes_viagem, ano_viagem)

    horario = f"{horas if len(horas) == 2 or horas[0] == '0' else f'0{horas}'}:{minutos if len(minutos) == 2 or minutos[0] == '0' else f'0{minutos}'}"

    # Pega vagas
    while True:
        vagas = input(BANCO_DE_FRASES['digite_vagas'])
        if validaVagas(vagas) == False:
            continue
        break
    
    # Pega preço por vagas
    while True:
        valor_por_vagas = input(BANCO_DE_FRASES['digite_valor'])
        if validaValorPorVagas(valor_por_vagas) == False:
            continue
        break

    if vagas.find(",") == 1:
        vagas = vagas.replace(",", ".")
    
    vagas_total.append({data_viagem: int(vagas)})
    caronas_cadastradas.append({'usuario_atual': usuario_atual, 'origem': origem, 'destino': destino, 'data_viagem': data_viagem, 'horario': horario, 'vagas': int(vagas), 'valor': f"{float(valor_por_vagas):.2f}"})

    print(f"\n{BANCO_DE_FRASES['carona_criada']}")
    sleep(1)
    os.system("cls" if os.name == 'nt' else 'clear')
    return caronas_cadastradas, vagas_total