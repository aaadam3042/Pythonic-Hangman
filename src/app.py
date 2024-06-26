from hangman import Hangman 
from utils import load_dictionary, yn_input

DICTIONARY_PATH = "./resources/dictionary.txt"

def app() -> None:
    dictionary = load_dictionary(DICTIONARY_PATH)

    print(f"Welcome to pythonic-hangman\n")
    is_multiplayer = yn_input("Do you wish to play with a friend (Y/N)")

    game = Hangman(is_multiplayer)
    game.load_valid_words(dictionary)
    game.select_word()

if __name__ == "__main__":
    app()
