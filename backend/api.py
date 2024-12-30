from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from game_logic import HangmanGame

# Initialize the FastAPI app and Hangman game
app = FastAPI()
game = HangmanGame()


# Request model for guesses
class GuessRequest(BaseModel):
    letter: str


@app.post("/start_game")
def start_game():
    game.reset_game()
    return {"message": "New game started!", "game_state": game.get_game_state()}


@app.post("/guess")
def guess_letter(request: GuessRequest):
    if not request.letter.isalpha() or len(request.letter) != 1:
        raise HTTPException(status_code=400, detail="Invalid guess. Please provide a single letter.")
    response = game.guess_letter(request.letter)
    return {**response, "game_state": game.get_game_state()}


@app.get("/game_state")
def get_game_state():
    return game.get_game_state()
