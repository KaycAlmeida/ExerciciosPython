print("Bem vindo ao jogo de Adivinhação")

numero_secreto = 42

chute = int(input("Digite seu número"))

print("Você digitou:", chute)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")