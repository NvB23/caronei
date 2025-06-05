from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
from time import sleep

def resumoCaronas(caronas_cadastradas, usuarios_cadastrados):
    str_motorista = BANCO_DE_FRASES['label_motorista']
    str_email_motorista = BANCO_DE_FRASES['label_email_motorista']
    str_origem = BANCO_DE_FRASES['label_origem']
    str_destino = BANCO_DE_FRASES['label_destino']
    str_data_carona = BANCO_DE_FRASES['label_data_carona']
    str_horario = BANCO_DE_FRASES['label_horario']
    str_vagas = BANCO_DE_FRASES['label_vagas']
    str_valor = BANCO_DE_FRASES['label_valor']

    cont = 0
    for carona in caronas_cadastradas:
        print(f"    {str_motorista}: {usuarios_cadastrados[carona['usuario_atual']]['nome']}".center(70))
        print(f"    {str_email_motorista}: {usuarios_cadastrados[carona['usuario_atual']]['email']}".center(70))
        print(f"    {str_origem}: {carona['origem']}".center(70))
        print(f"    {str_destino}: {carona['destino']}".center(70))
        print(f"    {str_data_carona}: {carona['data_viagem']}".center(70))
        print(f"    {str_horario}: {carona['horario']}".center(70))
        print(f"    {str_vagas}: {carona['vagas']}".center(70))
        print(f"    {str_valor}: R${carona['valor']}".center(70))
        print(f"{'_' * 70}\n")

        cont += 1
    
    sleep(cont * 3)