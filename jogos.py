import advinhacao
import forca

print("********************************")
print("********Escolha seu jogo********")
print("********************************")

print("(1) Forca (2) Adivinhcao")

jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando adivinhacao")
    advinhacao.jogar()