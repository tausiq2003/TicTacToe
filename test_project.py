from project import *

def test_checkWinner():
    board_x_wins = [["X", "O", "O"],
                    ["X", "X", "X"],
                    ["O", "X", "O"]]
    assert checkWinner(board_x_wins, "X") == True
    assert checkWinner(board_x_wins, "O") == False

    board_o_wins = [["X", "O", "O"],
                    ["X", "O", "X"],
                    ["O", "O", "O"]]
    assert checkWinner(board_o_wins, "O") == True
    assert checkWinner(board_o_wins, "X") == False

    board_no_winner = [["", "", ""],
                       ["", "", ""],
                       ["", "", ""]]
    assert checkWinner(board_no_winner, "X") == False
    assert checkWinner(board_no_winner, "O") == False

def test_checkDraw():
    board_draw = [["X", "O", "X"],
                  ["O", "X", "O"],
                  ["O", "X", "O"]]
    assert checkDraw(board_draw, checkWinner) == True

    board_no_draw = [["X", "O", "O"],
                      ["X", "X", "O"],
                      ["O", "X", "O"]]
    assert checkDraw(board_no_draw, checkWinner) == False
