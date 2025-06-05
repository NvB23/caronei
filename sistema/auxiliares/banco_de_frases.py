caronei = """
   ______   ___       ____     ____     _   __   ______   ____   __
  / ____/  /   |     / __ \   / __ \   / | / /  / ____/  /  _/  / /
 / /      / /| |    / /_/ /  / / / /  /  |/ /  / __/     / /   / / 
/ /___   / ___ |   / _, _/  / /_/ /  / /|  /  / /___   _/ /   /_/  
\____/  /_/  |_|  /_/ |_|   \____/  /_/ |_/  /_____/  /___/  (_)  
"""

linhas = "-" * 25

BANCO_DE_FRASES = {
    "titulo_cadastro": f"\033[1;36m{linhas} Cadastro {linhas}",
    "titulo_carteira": f"\033[1;36m{linhas} Minha Carteira {linhas}",
    "titulo_usuario": "Usuário",
    "titulo_login": f"\033[1;36m{linhas} Login {linhas}",
    "titulo_reservar": f"\033[1;36m{linhas} Reservar Carona {linhas}",
    "titulo_caronas_disponiveis": f"\033[1;36m{linhas} Caronas Disponíveis {linhas}",
    "titulo_busca": f"\033[1;36m{linhas} Busca de Caronas {linhas}",
    "titulo_detalhes": f"\033[1;36m{linhas} Detalhes de uma Carona {linhas}",
    "titulo_suas_caronas": f"\033[1;36m{linhas} Suas Caronas {linhas}",
    
    "opcao_invalida": "\033[1;31mOpção Inválida!",
    "digite_algo": "\033[1;31mDigite algo!",
    "apenas_letras": "\033[1;31mApenas letras!",
    "email_invalido": "\033[1;31mEmail inválido!",
    "email_cadastrado": "\033[1;31mEmail já cadastrado!",
    "senha_invalida": "\033[1;31mA senha precisa ter no mínimo 8 caracteres e no máximo 15 caracteres!",
    "diverge_campo": "\033[1;31mDiverge do campo anterior!",
    "cadastro_sucesso": "\n\033[1;32mCadastro realizado com sucesso!",
    "login_falhou": "\033[1;31mFalha ao logar! Tente novamente!",
    "carona_criada": "\033[1;32mCarona criada com sucesso!",
    "carona_reservada": "\033[1;32mCarona reservada!",
    "sem_caronas": "\033[1;31mSem caronas cadastradas!",
    "nenhuma_carona": "\033[1;31mNenhuma carona para essa busca!",
    "reserva_cancelada": "\033[1;32mReserva cancelada!",
    "sem_reserva": "\033[1;31mVocê não tinha reserva nessa carona!",
    "sem_saldo": "\033[1;31mVocê não tem saldo para reservar essa carona!",
    "carona_removida": "\033[1;32mCarona removida!",
    "nao_permissao": "\033[1;31mEsta carona não te pertence!",
    "saindo_conta": "\033[1;33mSaindo da conta...",
    "conta_saiu": "\033[1;32mConcluído!",
    
    "bem_vindo": "Bem vido ao ",
    "opcoes": "Opções",
    "menu_deslogado": "     [1] Cadastrar Usuário\n     [2] Fazer Login",
    "oferer_pegar_carona": "     [1]  Oferecer Carona\n     [2]  Pegar Carona",
    "menu_logado": "     [3]  Listar Todas as Caronas Disponíveis\n     [4]  Buscar Carona\n     [5]  Mostrar Detalhes da Carona\n     [6]  Mostrar Todas as Suas Caronas\n     [7]  Cancelar Reserva\n     [8]  Remover Carona\n     [9]  Minha Carteira\n     [10] Relatório de Totais\n     [0]  Logout\n",
    "opcao_sair": "     [00] Fechar\n",
    "selecione_opcao": "\033[1;34mSelecione uma opção >>> \033[m",
    "opcoes_carteira": "     [1] Depositar Dinheiro na Carteira\n     [2] Sacar Dinheiro da Carteira\n     [3] Voltar\n",
    
    "digite_nome": "\033[1;36mDigite seu nome: ",
    "digite_email": "\n\033[1;36mDigite seu email: ",
    "digite_senha": "\033[1;36mDigite sua senha: ",
    "confirme_senha": "\033[1;36mDigite sua senha novamente: ",
    "digite_origem": "\033[1;36mDe onde você vai partir: ",
    "digite_destino": "\033[1;36mPara onde você vai: ",
    "digite_vagas": "\033[1;36mQuantas vagas disponíveis: ",
    "digite_valor": "\033[1;36mQual o valor de cada vaga? R$",
    "email_motorista": "\033[1;36mDigite o email do motorista: ",
    "origem_busca": "\033[1;36mDigite a origem buscada: ",
    "destino_busca": "\033[1;36mDigite o destino buscado: ",
    "saldo_atual": "\033[1;36mSaldo Atual: R$ ",
    "quanto": "\033[1;36mQuanto: R$",
    
    "hoje_viagem": "\033[1;36mVai ser hoje? \n  [1] Sim \n  [2] Não\n>>> ",
    "agora_viagem": "\033[1;36mVai ser agora? \n  [1] Sim \n  [2] Não\n>>> ",
    
    "quando_viagem": "\033[1;36mQuando vai ser a viagem: ",
    "dia_viagem": "\033[1;36m    Dia: ",
    "mes_viagem": "\033[1;36m    Mês: ",
    "ano_viagem": "\033[1;36m    Ano: ",
    "hora_viagem": "\033[1;36m    Hora: ",
    "minuto_viagem": "\033[1;36m    Minuto: ",
    
    "apenas_numeros": "\033[1;31mApenas números!",
    "apenas_inteiros": "\033[1;31mApenas números inteiros!",
    "valor_positivo": "\033[1;31mApenas valor positivo!",
    "data_passada": "\033[1;31mSomente data atual ou futura!",
    "hora_passada": "\033[1;31mHora já passada!",
    "ano_invalido": "\033[1;31mSomente anos atuais ou futuros!",
    "mes_invalido": "\033[1;31mApenas valores entre 1 e 12!",
    "dia_invalido": "\033[1;31mApenas valores entre 1 e 31!",
    "hora_invalida": "\033[1;31mApenas números entre 1 e 24!",
    "minuto_invalido": "\033[1;31mApenas números entre 1 e 59!",
    "vagas_invalidas": "\033[1;31mApenas uma ou mais vagas!",
    "quantia_positiva": "\033[1;31mApenas valores positivos!\033[m",
    
    "sem_vagas": "\033[1;31mNão há mais vagas!",
    "nao_pegar_propria": "\033[1;31mNão é permitido pegar uma carona que você criou!",
    "carona_nao_encontrada": "\033[1;31mCarona não encontrada!",
    "nenhuma_reserva": "\033[1;31mNenhuma reserva encontrada para essa carona.",

    "label_motorista": "\033[1;36mMotorista",
    "label_email_motorista": "\033[1;36mEmail do Motorista",
    "label_origem": "\033[1;36mOrigem",
    "label_destino": "\033[1;36mDestino",
    "label_data_carona": "\033[1;36mData da Carona",
    "label_horario": "\033[1;36mHorário",
    "label_vagas": "\033[1;36mVagas",
    "label_valor": "\033[1;36mValor por Vagas",
    "label_total_carona": "\033[1;36mTotal a ser recebido nessa carona",
    "label_total": "\033[1;36mTotal a ser recebido de todas as caronas",

    "arquivo_relatorio": "\033[1;36mVocê vai querer um arquivo do relatório?\n  [1] Sim \n  [2] Não\n>>> "
}