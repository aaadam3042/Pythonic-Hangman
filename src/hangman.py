import random
from os import system, name
from utils import StateError

class Hangman:
    # create a new one for every game
    def __init__(self, is_multiplayer: bool) -> None:
        self.is_multiplayer = is_multiplayer
        self.dictionary = []
        self.word = []
        self.guessed_word = []
        self.guesses = []
        self.animation = []
        self.current_frame = 0
        self.max_lives = -1
        self.game_lives = -1

        # Game state variable
        # 0 on init, 1 on dictionary, 2 on word selection, 3 once playing
        self.state = 0 

    def load_animation(self, animation: list[str]) -> None:
        """
        Loads animation and sets lives
        """

        if self.state != 0:
            raise StateError(f"Attempted to load animation while in state {self.state}")
        self.animation = animation
        
        if len(self.dictionary) != 0:
            self.state = 1

        self.max_lives = len(self.animation)-1

    def load_valid_words(self, dictionary: list[str]) -> None:
        if self.state != 0:
            raise StateError(f"Attempted to load dictionary while in state {self.state}")
        self.dictionary = dictionary
        
        if len(self.animation) != 0:
            self.state = 1

    def select_word(self) -> None:
        if self.state != 1:
            raise StateError(f"Attempted to select word while in state {self.state}")
        
        assert self.is_multiplayer != None
        assert isinstance(self.is_multiplayer, bool)
        assert self.dictionary != None
        assert len(self.dictionary) != 0

        if self.is_multiplayer:
            while True:
                word = input("Choose a word: ").strip()
                if word in self.dictionary:
                    self.word = list(word)
                    break
                print("Please choose a valid word.")
        else:
            word = self.dictionary[random.randint(0, len(self.dictionary)-1)].split()[0]
            self.word = list(word)
        self.state = 2

    def play(self) -> None:
        if self.state != 2:
            raise StateError(f"Attempted to start game while in state {self.state}")

        assert self.word != None
        assert len(self.word) != 0
        assert isinstance(self.word, list)

        self.game_lives = self.max_lives
        self.current_frame = 0
        self.guesses = []
        self.guessed_word = []
        for char in self.word:
            self.guessed_word.append("_")

        # Game loop
        has_won = False
        has_lost = False
        first_attempt = True
        in_word = True
        while not has_won and not has_lost:
            self.clear_screen()
            self.display_message(in_word, first_attempt)
            self.draw_frame(in_word)  
            in_word = self.get_user_guess()  

            has_won = self.check_word_complete()
            has_lost = self.check_has_lost()
            first_attempt = False

        self.clear_screen()
        if has_won:
            print(f"CONGRATULATIONS - YOU won the game!\nThe word was: {''.join(self.word)}")
            print(self.animation[0])
        elif has_lost:
            print(f"Sorry, YOU LOSE! The word was: {''.join(self.word)}")
            print(self.animation[len(self.animation)-1])
        self.state = 1

    def clear_screen(self) -> None:
        system('cls' if name == 'nt' else 'clear')
    
    def display_message(self, in_word: bool, first_attempt: bool) -> None:
        message = ""
        if first_attempt:
            message = f"""Welcome to hangman! \n 
Try to save the man by guessing letters in the word correctly.\n
You have {self.game_lives} lives.
The word is: {" ".join(self.guessed_word)} """
        else:
            if self.game_lives < 0:
                raise RuntimeError("Negative lives left! Game error occured.")
            correct = ""
            if in_word:
                correct = "You guessed correctly!"
            else:
                correct = "Incorrect. Try again!"
            message = f"""
                {correct}\n
                You have {self.game_lives} lives left.
                Your guess: {" ".join(self.guessed_word)}
                Your guesses are: {" ".join(self.guesses)}"""

        print(f"""
###########################################################\n
{message}\n
###########################################################
            """)

    def draw_frame(self, in_word: bool) -> None:
        print(self.animation[self.current_frame])

    def get_user_guess(self) -> bool:
        
        guess = ""
        while True:
            guess = input("Guess a character: ").lower()
            if len(guess) != 1:
                print("Invalid guess! Ensure that your guess is a single character.")
            elif not guess.isalpha() and guess != "-":
                print("Invalid guess! Ensure that your guess is an alphabet character or '-'.")
            elif guess in self.guesses:
                print("Already guessed that letter! Try again.")
            else: 
                break
        if guess.strip() == "":
            raise RuntimeError("Guess returned empty string. Critical error!")
        
        self.guesses.append(guess)

        if guess.lower().strip() not in self.word:
            self.current_frame += 1
            self.game_lives -= 1
            return False
        
        # Update stored guessed word
        temp_word = [] 
        for i, char in enumerate(self.word):
            if char == guess:
                temp_word.append(f"{guess}")
            else:
                temp_word.append(self.guessed_word[i])
        self.guessed_word = temp_word

        return True

    def check_word_complete(self) -> bool:
        return "".join(self.word) == "".join(self.guessed_word)
    
    def check_has_lost(self) -> bool:
        return self.game_lives == 0
