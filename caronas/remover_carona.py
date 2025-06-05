from time import sleep
import os
from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
from caronas.auxiliares.data import data


def removerCarona(caronas_cadastradas, usuario_atual, saldo, usuarios_cadastrados, caronas_reservadas):
    for carona in caronas_cadastradas:
            if(usuario_atual == carona['usuario_atual']):
                dia_viagem, mes_viagem, ano_viagem = data()
            
                data_viagem = f"{dia_viagem if len(dia_viagem) == 2 or dia_viagem[0] == '0' else f'0{dia_viagem}'}/{mes_viagem if len(mes_viagem) == 2 or mes_viagem[0] == '0' else f'0{mes_viagem}'}/{ano_viagem}"

                para_remover = None
                for car in caronas_cadastradas:
                    if (data_viagem == car['data_viagem']):
                        para_remover = car
                
                if para_remover != None:
                    tupla_verifica = (usuarios_cadastrados[usuario_atual]['email'], data_viagem)

                    if(tupla_verifica in caronas_reservadas):
                        for passageiro in caronas_reservadas[tupla_verifica]:
                            saldo[passageiro] += float(para_remover['valor'])
                            saldo[usuario_atual] -= float(para_remover['valor'])
                    
                        caronas_reservadas.pop(tupla_verifica)

                    caronas_cadastradas.remove(para_remover)

                    print(BANCO_DE_FRASES['carona_removida'])
                    sleep(3)
                    os.system("cls" if os.name == 'nt' else 'clear')
            else:
                print(BANCO_DE_FRASES['nao_permissao'])
                sleep(3)
                os.system("cls" if os.name == 'nt' else 'clear')
                continue
    return caronas_cadastradas, saldo, caronas_reservadas