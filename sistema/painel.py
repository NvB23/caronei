from sistema.auxiliares.banco_de_frases import linhas, BANCO_DE_FRASES, caronei

def painel(logado, usuario_atual, usuarios_cadastrados):
    # Mostra nome de usuário se logado
    if(logado == True and usuario_atual != -1):
        print(f"\n\n\033[1;34m{linhas*2}\n") 

        str_usuario = BANCO_DE_FRASES['titulo_usuario']

        nome_estilizado = f"{str_usuario}: {usuarios_cadastrados[usuario_atual]['nome']}".center(50).upper()
        print(f"\033[3;34m{nome_estilizado}\033[m")
        print(f"\n\033[1;34m{linhas*2}")
    
    str_bem_vindo = BANCO_DE_FRASES['bem_vindo']
    str_opcoes = BANCO_DE_FRASES['opcoes']

    # Painel de boas vindas e opções
    print(f"\n\033[1;34m{str_bem_vindo}\n\n{caronei}\n\n\033[1;34m{str_opcoes}:\n")
    if(logado == False):
        print(BANCO_DE_FRASES['menu_deslogado'])
    if(logado == True):
        print(BANCO_DE_FRASES['oferer_pegar_carona'])
        print(BANCO_DE_FRASES['menu_logado'])
    print(BANCO_DE_FRASES['opcao_sair'])

    opcao = input(BANCO_DE_FRASES['selecione_opcao'])
    print("\n")

    return opcao