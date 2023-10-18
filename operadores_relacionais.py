# Solicita um número digitado pelo usuário
n = int(input("Digite um número:"))
#Comando de decisão: Verifica se o número é negativ o
if n < 0:
    n = n * (-1)
# Exibe o número positivo

print("Módulo: ",n)