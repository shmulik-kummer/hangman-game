import pytest
from unittest.mock import patch
from backend.game_logic import HangmanGame


@pytest.fixture
def hangman_game():
    # Mock the `fetch_random_words` method to provide a predefined word list
    with patch("backend.game_logic.fetch_random_words", return_value=["PYTHON", "HANGMAN", "DEVELOPER"]):
        return HangmanGame()


def test_guess_correct_letter(hangman_game):
    hangman_game.word = "PYTHON"
    response = hangman_game.guess_letter("P")
    assert response["success"] is True
    assert "P" in hangman_game.guessed_letters
    assert "P" in hangman_game.display_word


def test_guess_incorrect_letter(hangman_game):
    hangman_game.word = "PYTHON"
    hangman_game.display_word = ["_" for _ in hangman_game.word]  # Ensure display_word matches the word
    response = hangman_game.guess_letter("Z")
    assert response["success"] is False
    assert "Z" in hangman_game.wrong_guesses
    assert hangman_game.remaining_attempts == 5


def test_game_state(hangman_game):
    hangman_game.word = "PYTHON"
    hangman_game.display_word = ["_" for _ in hangman_game.word]  # Ensure display_word matches the word
    hangman_game.guess_letter("P")
    state = hangman_game.get_game_state()
    assert state["display_word"] == "P _ _ _ _ _"
    assert state["remaining_attempts"] == 6
    assert not state["game_over"]
    assert not state["game_won"]


def test_reset_game(hangman_game):
    hangman_game.reset_game()
    assert hangman_game.word in ["PYTHON", "HANGMAN", "DEVELOPER"]
    assert hangman_game.remaining_attempts == 6
    assert "_" in hangman_game.display_word
