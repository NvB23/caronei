from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
from datetime import date
from caronas.auxiliares.validadores_caronas import validaDia, validaMes, validaAno

def data():
    data_atual = str(date.today())

    while True:
        data_opcao = input(BANCO_DE_FRASES['hoje_viagem'])
        if(data_opcao == '1'):
            ano_viagem = data_atual[0:4]
            mes_viagem = data_atual[5:7]
            dia_viagem = data_atual[8:10]
            break
        elif(data_opcao == '2'):
            print(BANCO_DE_FRASES['quando_viagem'])

            # Pega dia
            while True:
                dia_viagem = input(BANCO_DE_FRASES['dia_viagem'])
                if validaDia(dia_viagem) == False:
                    continue
                break

            # Pega mês
            while True:
                mes_viagem = input(BANCO_DE_FRASES['mes_viagem'])
                if validaMes(mes_viagem) == False:
                    continue
                break
            
            # Pega ano
            while True:
                ano_viagem = input(BANCO_DE_FRASES['ano_viagem'])
                if validaAno(ano_viagem) == False:
                    continue
                break
            
            # Verifica se a data já passou
            data_informada = date(int(ano_viagem), int(mes_viagem), int(dia_viagem))
            if data_informada < date.today():
                print(BANCO_DE_FRASES['data_passada'])
                continue

            break
        else:
            print(BANCO_DE_FRASES["opcao_invalida"] + "\n")
            continue
    return dia_viagem, mes_viagem, ano_viagem