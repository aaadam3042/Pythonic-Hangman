import os
from hangman import Hangman 
from utils import load_animation, load_dictionary, yn_input

DICTIONARY_PATH = "./resources/dictionary.txt"
ANIMATION_PATH = "./resources/animation.anim"

def app() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

    dictionary = load_dictionary(DICTIONARY_PATH)
    animation = load_animation(ANIMATION_PATH)

    print(f"Welcome to pythonic-hangman\n")
    is_multiplayer = yn_input("Do you wish to play with a friend (Y/N)")

    game = Hangman(is_multiplayer)
    game.load_animation(animation)
    game.load_valid_words(dictionary)
    while True:
        game.select_word()
        game.play()
        if not yn_input("Do you want to play again (Y/N): "):
            break

if __name__ == "__main__":
    app()
