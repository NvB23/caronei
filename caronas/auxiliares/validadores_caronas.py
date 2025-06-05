from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES

def validaOrigemDestino(origem_destino):
    if origem_destino.strip() == "":
        print(BANCO_DE_FRASES['digite_algo']) 
        return False
    elif origem_destino.isnumeric() or origem_destino.isdecimal():
        print(BANCO_DE_FRASES['apenas_letras'])
        return False
    return True

def validaVagas(vagas):
    if vagas.strip() == "":
        print(BANCO_DE_FRASES['digite_algo'])
        return False
    elif(vagas.isalpha()):
        print(BANCO_DE_FRASES['apenas_numeros'])
        return False
    elif(int(vagas) < 1):
        print(BANCO_DE_FRASES['vagas_invalidas'])
        return False
    elif(not vagas.isdecimal()):
        print(BANCO_DE_FRASES['apenas_inteiros'])
        return False
    return True

def validaValorPorVagas(valor_por_vagas):
    if valor_por_vagas.strip() == "":
        print(BANCO_DE_FRASES['digite_algo'])
        return False
    elif(valor_por_vagas.isalpha()):
        print(BANCO_DE_FRASES['apenas_numeros'])
        return False
    elif(float(valor_por_vagas) < 0):
        print(BANCO_DE_FRASES['valor_positivo'])
        return False
    return True

def validaDia(dia_viagem):
    if dia_viagem.strip() == "":
        print(BANCO_DE_FRASES['digite_algo'])
        return False
    elif(not dia_viagem.isdigit()):
        print(BANCO_DE_FRASES['apenas_inteiros'])
        return False
    elif int(dia_viagem) < 1 or int(dia_viagem) > 31:
        print(BANCO_DE_FRASES['dia_invalido'])
        return False
    return True

def validaMes(mes_viagem):
    if mes_viagem.strip() == "":
        print(BANCO_DE_FRASES['digite_algo'])
        return False
    elif(not mes_viagem.isdigit()):
        print(BANCO_DE_FRASES['apenas_inteiros'])
        return False
    elif int(mes_viagem) < 1 or int(mes_viagem) > 12:
        print(BANCO_DE_FRASES['mes_invalido'])
        return False
    return True

def validaAno(ano_viagem):
    if ano_viagem.strip() == "":
        print(BANCO_DE_FRASES['digite_algo'])
        return False
    elif(not ano_viagem.isdigit()):
        print(BANCO_DE_FRASES['apenas_inteiros'])
        return False
    return True

def validaHoras(horas):
    if horas.strip() == "":
        print(BANCO_DE_FRASES['digite_algo'])
        return False
    elif(not horas.isdigit()):
        print(BANCO_DE_FRASES['apenas_inteiros'])
        return False
    elif int(horas) < 0 or int(horas) > 24:
        print(BANCO_DE_FRASES['hora_invalida'])
        return False
    return True

def validaMinutos(minutos):
    if minutos.strip() == "":
        print(BANCO_DE_FRASES['digite_algo'])
        return False
    elif(not minutos.isdigit()):
        print(BANCO_DE_FRASES['apenas_inteiros'])
        return False
    elif (int(minutos) < 0 or int(minutos) > 59):
        print(BANCO_DE_FRASES['minuto_invalido'])
        return False
    return True