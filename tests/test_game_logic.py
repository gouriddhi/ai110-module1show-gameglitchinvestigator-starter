from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

import os

import pytest
from streamlit.testing.v1 import AppTest

APP_PATH = os.path.join(os.path.dirname(__file__), "..", "app.py")

@pytest.mark.parametrize("difficulty, low, high", [
    ("Easy", 1, 20),
    ("Normal", 1, 100),
    ("Hard", 1, 50),
])
def test_info_box_shows_difficulty_range(difficulty, low, high):
    # The info box used to always say "between 1 and 100", regardless of difficulty
    at = AppTest.from_file(APP_PATH).run()
    at.sidebar.selectbox[0].select(difficulty).run()
    assert f"Guess a number between {low} and {high}." in at.info[0].value
