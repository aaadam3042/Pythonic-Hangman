from hangman import Hangman 
from utils import yn_input

def app():
    print(f"Welcome to pythonic-hangman\n")
    is_multiplayer = yn_input("Do you wish to play with a friend (Y/N)")

    game = Hangman(is_multiplayer)
    game.select_word()

if __name__ == "__main__":
    app()
