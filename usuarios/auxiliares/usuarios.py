from ast import literal_eval

def paraArquivo(dicionario):
    with open("dados/usuarios.txt", "+a") as arquivo:
        arquivo.write(f"{dicionario}\n")
        
def doArquivo(lista_usuarios_cadastrados: list, saldo: dict):
    with open("dados/usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            if linha.strip() != "":
                usuario = literal_eval(linha)
                lista_usuarios_cadastrados.append(usuario)
        for i in range(len(lista_usuarios_cadastrados)):
            usuario_atual = i
            saldo[usuario_atual] = 0.0
    return lista_usuarios_cadastrados, saldo