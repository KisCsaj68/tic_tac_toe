from typing import Any, Tuple, List
from tic_tac_toe.tic_tac_toe.tic_tac_toe import \
    get_winning_player, check_board_full 
import pytest


test_winning: List[Tuple[List[List[str]],str, bool]] = [
    ([["X","X","X"],[".",".","."],[".",".","."]], "X", "X"),
    ([[".",".","."],["X","X","X"],[".",".","."]], "X", "X"),
    ([[".",".","."],[".",".","."],["X","X","X"]], "X", "X"),
    ([["X",".","."],[".","X","."],[".",".","X"]], "X", "X"),
    ([[".",".","X"],[".","X","."],["X",".","."]], "X", "X"),
    ([["X",".","."],["X",".","."],["X",".","."]], "X", "X"),
    ([[".","X","."],[".","X","."],[".","X","."]], "X", "X"),
    ([[".",".","X"],[".",".","X"],[".",".","X"]], "X", "X"),
    ([["X","X","O"],[".","O","."],["O",".","."]], "X", None),
    ([["X","O","X"],[".",".","."],[".","O","O"]], "X", None),
    ([["X",".","X"],[".",".","."],[".",".","."]], "X", None)
]

test_board_full: List[Tuple[List[List[str]], bool]] = [
    ([["X","X","X"],[".",".","."],[".",".","."]], False),
    ([[".",".","."],["X","X","X"],[".",".","."]], False),
    ([["X","X","X"],[".",".","."],["X","X","X"]], False),
    ([["X","X","X"],["O","O","O"],["X","O","X"]], True),
    ([["O","O","O"],[".",".","."],[".",".","."]], False),
    ([["O","O","O"],["O","O","O"],[".",".","."]], False),
    ([["X","X","X"],["O","O","O"],["O","O","O"]], True),
    ([[".",".","."],[".",".","."],[".",".","."]], False)
    

]


@pytest.mark.parametrize("board, player, win", test_winning)
def test_check_winning(board, player, win):
    assert get_winning_player(board, player) == win

@pytest.mark.parametrize("board, full", test_board_full)
def test_check_board_full(board, full):
    assert check_board_full(board) == full   
