from sistema.auxiliares.banco_de_frases import BANCO_DE_FRASES
from random import randint
import os
import qrcode
from pybrcode.pix import generate_simple_pix
from PIL import Image
from dotenv import load_dotenv
from usuarios.auxiliares.validadores_quantia import validaQuantia


def carteira(saldo, usuario_atual, imagens_pix):
    load_dotenv()

    saldo_do_usuario = 0.0
    if(usuario_atual not in saldo):
        saldo[usuario_atual] = 0.0
    else:
        saldo_do_usuario = saldo[usuario_atual]
        if saldo_do_usuario < 0.0:
            saldo[usuario_atual] = 0.0
            saldo_do_usuario = 0
    print(BANCO_DE_FRASES['titulo_carteira'])
    str_saldo_atual = BANCO_DE_FRASES['saldo_atual']
    print(f"{str_saldo_atual}{saldo_do_usuario:.2f}\n".center(66))
    print(BANCO_DE_FRASES['opcoes_carteira'])

    quantia = 0
    while True:
        opcao_carteira = input("     >>> ")
        if opcao_carteira.strip() == "":
            print(BANCO_DE_FRASES['digite_algo'])
        elif(opcao_carteira == '1'):
            while True:
                quantia = input(BANCO_DE_FRASES['quanto'])
                if quantia.strip() == "":
                    print(BANCO_DE_FRASES['digite_algo'])
                    continue
                quantia = float(quantia)
                if not validaQuantia(quantia):
                    continue
                break
            saldo[usuario_atual] += quantia
            pix_code = generate_simple_pix(
                key= os.getenv('CHAVE_PIX'),
                fullname = os.getenv('NOME'),
                city= os.getenv('CIDADE'),
                value= quantia
            )
            data = str(pix_code)
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            c_image = ""
            for i in range(0,5):
                c_image += str(randint(0,9))
            nome_imagem = f"pix-{usuario_atual}{c_image}.png"
            pasta = "dados/imagens_pix"
            os.makedirs(pasta, exist_ok=True)
            path = f"{pasta}/{nome_imagem}"
            img.save(path)
            imagens_pix.append(path)
            Image.open(path).show()
            os.system("cls" if os.name == 'nt' else 'clear')
            break
        elif (opcao_carteira == '2'):
            while True:
                quantia = input(BANCO_DE_FRASES['quanto'])
                if str(quantia).strip() == "":
                    print(BANCO_DE_FRASES['digite_algo'])
                    continue
                quantia = float(quantia)
                if not validaQuantia(quantia):
                    continue
                saldo[usuario_atual] -= quantia
                os.system("cls" if os.name == 'nt' else 'clear')
                break
            break
        elif (opcao_carteira == '3'):
            os.system("cls" if os.name == 'nt' else 'clear')
            break
        else:
            print(BANCO_DE_FRASES['opcao_invalida'])
    return saldo, imagens_pix