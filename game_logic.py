import random
from typing import Dict, List


class HangmanGame:
    def __init__(self, word_list: List[str], max_attempts: int = 6):
        self.display_word = None
        self.remaining_attempts = None
        self.wrong_guesses = None
        self.guessed_letters = None
        self.word = None
        self.word_list = word_list
        self.max_attempts = max_attempts
        self.reset_game()

    def reset_game(self):
        self.word = random.choice(self.word_list).upper()
        self.guessed_letters = set()
        self.wrong_guesses = set()
        self.remaining_attempts = self.max_attempts
        self.display_word = ["_" if char.isalpha() else char for char in self.word]

    def guess_letter(self, letter: str) -> Dict:
        letter = letter.upper()
        if letter in self.guessed_letters or letter in self.wrong_guesses:
            return {"error": "Letter already guessed!"}

        if letter in self.word:
            self.guessed_letters.add(letter)
            for index, char in enumerate(self.word):
                if char == letter:
                    self.display_word[index] = letter
            return {"success": True, "message": f"'{letter}' is correct!"}
        else:
            self.wrong_guesses.add(letter)
            self.remaining_attempts -= 1
            return {"success": False, "message": f"'{letter}' is incorrect!"}

    def get_game_state(self) -> Dict:
        return {
            "display_word": " ".join(self.display_word),
            "guessed_letters": sorted(list(self.guessed_letters)),
            "wrong_guesses": sorted(list(self.wrong_guesses)),
            "remaining_attempts": self.remaining_attempts,
            "game_over": self.remaining_attempts <= 0,
            "game_won": "_" not in self.display_word,
        }
