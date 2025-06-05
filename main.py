from sistema.prepara_bibliotecas import preparaBibliotecas
from sistema.traducao import traducao
from sistema.painel import painel
from sistema.fechar_programa import fecharPrograma
from sistema.auxiliares.validadores_opcao import validaVazio
from usuarios.cadastro_usuarios import cadastraUsuario
from usuarios.login_usuarios import loginUsuarios
from usuarios.sair_conta import sairConta

from caronas.oferecer_caronas import oferecerCaronas
from caronas.pegar_caronas import pegarCaronas
from caronas.listar_caronas import listarCaronas
from caronas.buscar_caronas import buscarCaronas
from caronas.detalhes_carona import detalhesCarona
from caronas.caronas_usuarios import caronasUsuarios
from caronas.cancela_reserva import cancelaReserva
from caronas.remover_carona import removerCarona
from usuarios.carteira import carteira
from usuarios.auxiliares.usuarios import doArquivo
from caronas.relatorio_caronas import relatorioCaronas

import os

preparaBibliotecas()
traducao()

os.makedirs("dados", exist_ok= True)
open("dados/usuarios.txt", "a")

usuarios_cadastrados = []
saldo = {}
usuarios_cadastrados, saldo = doArquivo(usuarios_cadastrados, saldo)
caronas_cadastradas = []
caronas_reservadas = {}
vagas = []
usuario_atual = -1
imagens_pix = []
logado = False

while True:
    opcao = painel(logado, usuario_atual, usuarios_cadastrados)
    if not validaVazio(opcao):
        continue
    if(opcao == '1' and not logado):
        usuarios_cadastrados, saldo = cadastraUsuario(usuarios_cadastrados, saldo)
        continue
    if(opcao == '2' and not logado):
        logado, usuario_atual = loginUsuarios(logado, usuarios_cadastrados, usuario_atual)
        continue
    if(opcao == '1' and logado):
        caronas_cadastradas, vagas = oferecerCaronas(usuario_atual, caronas_cadastradas, vagas)
        continue
    if(opcao == '2' and logado):
        saldo, caronas_reservadas = pegarCaronas(saldo, usuario_atual, caronas_cadastradas, usuarios_cadastrados, caronas_reservadas)
        continue
    if (opcao == '3' and logado):
        listarCaronas(caronas_cadastradas, usuarios_cadastrados)
        continue
    if(opcao == '4' and logado):
        buscarCaronas(caronas_cadastradas, usuarios_cadastrados)
        continue
    elif(opcao == '5' and logado):
        detalhesCarona(caronas_cadastradas, usuarios_cadastrados)
        continue
    elif(opcao == '6' and logado):
        caronasUsuarios(caronas_cadastradas, usuarios_cadastrados, usuario_atual)
        continue
    elif(opcao == '7' and logado):
        saldo, caronas_reservadas = cancelaReserva(caronas_cadastradas,saldo, usuarios_cadastrados, caronas_reservadas, usuario_atual)
        continue
    elif(opcao == '8' and logado):
        caronas_cadastradas, saldo, caronas_reservadas = removerCarona(caronas_cadastradas, usuario_atual, saldo, usuarios_cadastrados, caronas_reservadas)
        continue
    elif(opcao == '9' and logado):
        saldo, imagens_pix = carteira(saldo, usuario_atual, imagens_pix)
    elif(opcao == '10' and logado):
        relatorioCaronas(caronas_cadastradas, usuario_atual, vagas, usuarios_cadastrados)

    if(opcao == '0' and logado):
        logado = sairConta(logado)
    if(opcao == '00'):
        fecharPrograma(imagens_pix)
        break