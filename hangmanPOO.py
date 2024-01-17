# Hangman Game (Jogo da Forca)

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Método para gerar uma palavra aleatória
def gerar_palavra_aleatoria():
    palavra_aleatoria = random.choice(['programacao', 'computador', 'python', 'sql', 'google'])
    return palavra_aleatoria

# Classe
class Hangman:

# Método Construtor
    def __init__(self, palavra_secreta):
        self.palavra_secreta = palavra_secreta
        self.palavra_descoberta = ['_' for _ in palavra_secreta]
        self.tentativas_erradas = 0
        self.letras_tentadas = []

# Método para começar o jogo
    def jogar(self):
        while self.tentativas_erradas < 6 and '_' in self.palavra_descoberta:
            self.exibir_estado()
            letra = self.solicitar_letra()

            if letra in self.letras_tentadas:
                print("Você já tentou esta letra. Tente outra")
                continue

            self.adicionar_letra_tentada(letra)

            if letra in self.palavra_secreta:
                self.atualizar_palavra_descoberta(letra)
            else:
                self.tentativas_erradas += 1

        self.exibir_resultado()

# Método para exibir o exibir o estado do jogo
    def exibir_estado(self):
        print(board[self.tentativas_erradas])
        print("\nPalavra: " + " ".join(self.palavra_descoberta))
        print("Letras tentadas: " + ", ".join(self.letras_tentadas))
        print("Tentativas restantes " + str(6 - self.tentativas_erradas))

# Método para solicitar uma letra
    def solicitar_letra(self):
        letra = input("Digite uma letra: ")
        return letra

# Método para adicionar letra tentada
    def adicionar_letra_tentada(self, letra):
        self.letras_tentadas.append(letra)

# Método para atualizar a palavra descoberta
    def atualizar_palavra_descoberta(self, letra):
        for i, caractere in enumerate(self.palavra_secreta):
            if caractere == letra:
                self.palavra_descoberta[i] = letra.lower()

# Método para incrementar tentativas erradas
    def incrementar_tentativas_erradas(self):
        self.tentativas_erradas += 1

# Método para exibir o resultado
    def exibir_resultado(self):
        if '_' not in self.palavra_descoberta:
            print("Parábens! Você descobriu a palavra: " + "".join(self.palavra_descoberta))
        else:
            print("Você perdeu! A palavra era: " + self.palavra_secreta)

jogo = Hangman(gerar_palavra_aleatoria())

jogo.jogar()