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
            exibir_estado()
            letra = solicitar_letra()

            if letra in self.letras_tentadas:
                print("Você já tentou esta letra. Tente outra")
                continue

            self.letras_tentadas.append(letra)

            if letra in self.palavra_secreta:
                self.palavra_descoberta.append(letra)
            else:
                self.tentativas_erradas += 1

        exibir_resultado()

# Metódo para exibir o exibir o estado do jogo
    def exibir_estado(self):
        print("Palavra: " + " ".join(self.palavra_descoberta))
        print("Letras tentadas: " + ", ".join(self.letras_tentadas))
        print("Tentativas restantes " + str(6 - self.tentativas_erradas))
