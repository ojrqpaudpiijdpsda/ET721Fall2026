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
'''

Reflection:

1. What was the most interesting part of the unit testing project, justify answer?
The most interesting part of the unit test is learning about monkeypatch, although it wasnt taught in class learning about what it does made it interesting, it also seems like it has alot of use in a real dev environment for testing

2. What was the most difficult part of the unit testing project, and how did you manage to overcome those difficulties?
The most difficult part was learning different things pytest actually has, overcoming the difficulty was simply just searching up what the different syntax can do

3. Did you use any AI tools or assistants to complete this lab? If so, briefly explain how you used them.
Yes, i used it to help me learn about the different ways to use monkeypatch but other than that there was nothing.



'''