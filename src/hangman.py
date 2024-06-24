class Hangman:
    # create a new one for every game
    def __init__(self, is_multiplayer: bool):
        self.is_multiplayer = is_multiplayer
        
    def select_word(self) -> None:
        ...