'''
Jia Xi Pang
Project 2

'''

import pytest
from main import *
#testing play_game(self)

def test_play_game_win(monkeypatch):
    inputs = iter(["1", "1", "2", "2", "3", "3", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    game = Connect4()

    try:
        game.play_game()
    except StopIteration:
        pass

    assert game.check_win("!") is True

def test_play_game_invalid_move_breaks_loop(monkeypatch):
    inputs = iter(["9"]) 
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    game = Connect4()
    
    try:
        game.play_game()
    except StopIteration:
        pass

    assert game.board[5][0] == " "

def test_play_game_tie(monkeypatch):
    inputs = iter(["1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    game = Connect4()
    

    monkeypatch.setattr(game, "is_full", lambda: True)

    try:
        game.play_game()
    except StopIteration:
        pass

    assert game.current_player == "!"


'''
Results:
All 3 tests passed

Issues: The only issue i really had was actually setting up monkeypatch correctly which led to some failures but otherwise there isnt any issues with testing game results

'''
