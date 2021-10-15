import random

def jogar():
    print("********************************")
    print("***Bem vindo ao jogo de Forca***")
    print("********************************")

    arquivo = open("palavra.txt", "r", encoding = "utf-8")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta] #inicializa a lista com todos os caracteres "_" de acordo com o tamanho da palavra secreta

    enforcou = False
    acertou = False
    erros = 0    

    print(letras_acertadas)

    #enquanto(True)
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))
        
        enforcou = erros == 6 #verifica que erros é igual a 6, se for define enforcou igual a True
        acertou = "_" not in letras_acertadas #verifica se o _ não está dentro das letras acertadas.
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!!!")
    else:
        print("Você perdeu!!!")        
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()