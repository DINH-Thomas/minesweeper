import pytest

from src import minesweeper


def test_module_exists():
    assert minesweeper


def test_place_mines():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    # TODO : Add assertions
    assert len(game.mines) == 2


def test_reveal():
    import random

    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    game.reveal(2, 2)
    # TODO : Add assertions
    assert game.revealed == {(2, 2)}


def test_get_board():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    board = game.get_board()
    # TODO : Add assertions
    assert isinstance(board, list)


def test_is_winner():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    # Simulate revealing all non-mine cells
    for r in range(3):
        for c in range(3):
            if (r, c) not in game.mines:
                game.reveal(r, c)
    assert game.is_winner() == True


def test_restart():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.restart()
    # TODO : Add assertions
    assert (game.rows == 3) & (game.cols == 3) & (game.num_mines == 2)
