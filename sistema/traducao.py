from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
import re
from deep_translator import GoogleTranslator

def opcoes_traducao(num_opcoes, sigla_opcoes):
    while True:
        global sigla_lingua, nao_traduz
        lingua_opcao = input("\033[1;33mSelect your language: ")
        if lingua_opcao.strip() == "":
            print("\033[1;31mType something!\033[1;m")
            continue
        elif(lingua_opcao == '1'):
            return "", True
        for n_opcoes, s_opcoes in zip(num_opcoes, sigla_opcoes):
            if(lingua_opcao == str(n_opcoes)):
                return s_opcoes, False
        else:
            print("\033[1;31mInvalid option!\033[1;m")
            continue

def traducao():
    para_traduzir = []

    for frase in BANCO_DE_FRASES.values():
        frase_descolorida = re.sub(r"\033\[[0-9;]*m", "", frase)

        para_traduzir.append(frase_descolorida)

    print("""\033[1;33m
            [1] Portuguese 
            [2] English 
            [3] Spanish 
            [4] Japanese
    """)

    sigla_lingua, nao_traduz = opcoes_traducao([2,3,4], ['en', 'es', 'ja'])

    if nao_traduz != True:
        traduzido = GoogleTranslator(target=sigla_lingua, source='pt').translate_batch(para_traduzir)

        for i in range(len(BANCO_DE_FRASES.keys())):
            lista_chaves = list(BANCO_DE_FRASES.keys())
            chave = lista_chaves[i]
            frase = traduzido[i]
            BANCO_DE_FRASES[chave] = frase