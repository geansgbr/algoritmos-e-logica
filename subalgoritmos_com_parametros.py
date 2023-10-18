# Criação do procedimento com parâmetros
def saudacao2(usuario, hora):
    if hora < 12:
        msg = "Bom dia!"
    elif hora < 18:
        msg = "Boa tarde!"
    else:
        msg = "Boa noite!"
    print("Olá "+ usuario +", "+ msg +" Você está logado")

# Chamada do procedimento
saudacao2("Edson", 16)