import random

class Hangman:
    # create a new one for every game
    def __init__(self, is_multiplayer: bool) -> None:
        self.is_multiplayer = is_multiplayer
        self.word = ""
        self.dictionary = []
        self.state = 0 # 0 on init, 1 on dictionary, 2 on word selection, 3 once playing

    def load_valid_words(self, dictionary: list[str]) -> None:
        if self.state != 0:
            raise RuntimeError(f"Invalid game state - Attempted to load dictionary while in state {self.state}")
        self.dictionary = dictionary
        self.state = 1

    def select_word(self) -> None:
        if self.state != 1:
            raise RuntimeError(f"Invalid game state - Attempted to select word while in state {self.state}")
        
        assert self.is_multiplayer != None
        assert isinstance(self.is_multiplayer, bool)
        assert self.dictionary != None
        assert len(self.dictionary) != 0

        if self.is_multiplayer:
            while True:
                word = input("Choose a word: ")
                if word in self.dictionary:
                    self.word = word
                    break
                print("Please choose a valid word.")
        else:
            self.word = self.dictionary[random.randint(0, len(self.dictionary)-1)]
        self.state = 2

    def play(self) -> None:
        if self.state != 2:
            raise RuntimeError(f"Invalid game state - Attempted to start game while in state {self.state}")

        assert self.word != None
        assert self.word.strip() != ""
        assert isinstance(self.word, str)

        self.display_message()
        self.draw_frame()   # There should be only one draw function, instead we update state
        self.get_user_input()
    