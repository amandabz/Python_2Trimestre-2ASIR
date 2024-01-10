"""
Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 - El juego comienza proponiendo una palabra aleatoria incompleta
 - Por ejemplo "m_e_rc_ _l_ s", y el número de intentos que le quedan
 - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que  la palabra a adivinar)
 - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta uno al número de intentos
 - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno al número de intentos
 - Si el contador de intentos llega a 0, el jugador pierde
 - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 - Puedes utilizar las palabras que quieras y el número de intentos que consideres.
"""
import random

words_list = ["python", "javascript", "programming", "cherry", "orange", "amanda", "purple", "apple", "banana"]
word = random.choice(words_list)
attempts = 5

num_hidden = int(len(word) * 0.5)
positions = random.sample(range(len(word)), num_hidden)

game_word = ""

for i in range(len(word)):
    game_word += word[i] if i not in positions else "_"

print(game_word)

while attempts > 0:
    entry = input("Enter a letter or the solution: ")
    if len(entry) == 1:
        success = False

        if entry in word:
            for i, letter in enumerate(word):
                if letter == entry and game_word[i] == "_":
                    game_word = game_word[:i] + entry + game_word[i + 1:]
                    success = True
                    print("You have got it right!")
            print(game_word)

        if not success:
            print("Incorrect")
            attempts -= 1
            print(f"You have {attempts} attempts left")
            print(game_word)

    else:
        if entry == word:
            print("You won!")
            break

        else:
            print("The word is not correct")
            attempts -= 1
            print(f"You have {attempts} attempts left")

    if attempts == 0:
        print("You lost!")
        print(f'The word was "{word}"')
