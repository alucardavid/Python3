print("********************************")
print("Bem vindo ao jogo de advinhacao!")
print("********************************")

numero_secreto = 42

chute_str = input("Digite o seu numero: ")

print("Você digitou ", chute_str)

chute = int(chute_str)
acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if acertou:
    print("Você acertou")
else:
    if maior:
        print("Você errou! O seu chute foi maior do que número secreto.")
    elif menor:
        print("Você errou! O seu chute foi menor do que número secreto.")

print("Fim do jogo")