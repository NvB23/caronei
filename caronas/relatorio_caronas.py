from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
from caronas.auxiliares.validadoresRelatorio import validaOpcaoRelatorio
from time import sleep
import os
import re
from random import randint

def relatorioCaronas(caronas_cadastradas, usuario_atual, vagas, usuarios_cadastrados):
    str_origem = ""
    str_destino = ""
    str_data_carona = ""
    str_horario = ""
    str_vagas = ""
    str_valor = ""
    str_total_carona = ""
    str_divisor = ""
    str_total = ""

    valores_caronas = []
    dono_carona = -1

    id_carona = ""
    for i in range(0,5):
        numero_aleatorio = randint(0, 9)
        id_carona += str(numero_aleatorio)

    texto = ""

    encontrado = False
    for carona, vaga in zip(caronas_cadastradas, vagas):
        if carona["usuario_atual"] == usuario_atual:
            encontrado = True
            dono_carona = carona['usuario_atual']
            vaga_de_cada_carona = int(vaga.get(carona['data_viagem'], 0))
            valor_carona = float(carona['valor']) * int(vaga_de_cada_carona)
            
            str_origem = f"    {BANCO_DE_FRASES['label_origem']}: {carona['origem']}"
            str_destino = f"    {BANCO_DE_FRASES['label_destino']}: {carona['destino']}"
            str_data_carona = f"    {BANCO_DE_FRASES['label_data_carona']}: {carona['data_viagem']}"
            str_horario = f"    {BANCO_DE_FRASES['label_horario']}: {carona['horario']}"
            str_vagas = f"    {BANCO_DE_FRASES['label_vagas']}: {carona['vagas']}"
            str_valor = f"    {BANCO_DE_FRASES['label_valor']}: R${carona['valor']}"
            str_total_carona = f"    {BANCO_DE_FRASES['label_total_carona']}: R${valor_carona:.2f}"
            str_divisor = f"{'_' * 70}\n"

            print(f"{str_origem}\n".center(70))
            print(f"{str_destino}\n".center(70))
            print(f"{str_data_carona}\n".center(70))
            print(f"{str_horario}\n".center(70))
            print(f"{str_vagas}\n".center(70))
            print(f"{str_valor}\n".center(70))


            print(f"{str_total_carona}\n".center(70))
            valores_caronas.append(valor_carona)
            print(str_divisor)

            texto += tiraCores(str_origem) + "\n" + tiraCores(str_destino) + "\n"  + tiraCores(str_data_carona) + "\n"  + tiraCores(str_horario) + "\n"  + tiraCores(str_vagas) + "\n"  + tiraCores(str_valor) + "\n"  + tiraCores(str_total_carona) + "\n"  + tiraCores(str_divisor) + "\n" 

    if not encontrado:
        print(f"{BANCO_DE_FRASES['sem_caronas']} \n".center(70))
        sleep(3)
        os.system("cls" if os.name == 'nt' else 'clear')
    else:
        total = sum(valores_caronas)
        str_total = f"\n    {BANCO_DE_FRASES['label_total']}: R${total:.2f}"
        print(f"{str_total}".center(70))
        texto += tiraCores(str_total)
        while True:
            opcao_relatorio = input(BANCO_DE_FRASES['arquivo_relatorio'])
            validaOpcaoRelatorio(opcao_relatorio)
            if not validaOpcaoRelatorio:
                continue
            elif opcao_relatorio == "1":
                if os.path.isdir("dados/relatorios") != True:
                    os.makedirs("dados/relatorios", mode=True)
                with open(f"dados/relatorios/relatorio-{usuarios_cadastrados[dono_carona]['email']}-{id_carona}.txt", "w") as relatorio:
                    relatorio.write(texto)
                os.system("cls" if os.name == 'nt' else 'clear')
                break
            elif opcao_relatorio == "2":
                sleep(2)
                os.system("cls" if os.name == 'nt' else 'clear')
                break


def tiraCores(texto):
    return re.sub(r"\033\[[0-9;]*m", "", texto)