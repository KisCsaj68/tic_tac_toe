import sys
import os
from typing import Dict, List, Tuple


def get_empty_board() -> List[List[str]]:
    board: List[List[str]] = []
    for _ in range(3):
        column_ = []
        for _ in range(3):
            column_.append(".")
        board.append(column_)
    return board


def set_player_avatar() -> str:
    player: str = ""
    while player not in ["X", "O"]:
        player = input("Please choose your avatar( X or O)! ").upper()

    return player


def change_player(player: str) -> str:
    if player == "X":
        return "O"
    else:
        return "X"


def get_human_coordinates(board: List[List[str]]) -> Tuple[int, int]:
    valid_coordinates: Dict[str, Tuple[int, int]] = {
        "A1": (0, 0),
        "A2": (0, 1),
        "A3": (0, 2),
        "B1": (1, 0),
        "B2": (1, 1),
        "B3": (1, 2),
        "C1": (2, 0),
        "C2": (2, 1),
        "C3": (2, 2)
    }
    valid_coordinates_list: List[str] = [
        key for key in valid_coordinates.keys()]
    coordinates_are_valide: bool = False
    while not coordinates_are_valide:
        human_coordinates: str = input("Give Your coordinates: ").upper()
        if human_coordinates == "QUIT":
            sys.exit()
        if human_coordinates in valid_coordinates.keys():
            coordinates: Tuple[int, int] = valid_coordinates.get(
                human_coordinates)
            if board[coordinates[0]][coordinates[1]] == ".":
                coordinates_are_valide = True
                return coordinates
            else:
                os.system('clear')
                print_board(board)
                print("Please give a not taken coordinat! Use: " +
                    ", ".join(valid_coordinates_list))    
        else:
            os.system('clear')
            print_board(board)
            print("Please give a valid coordinat! Use: " +
                  ", ".join(valid_coordinates_list))


def marking_move(player: str, board: List[List[str]], move: Tuple[int, int]) -> List[List[str]]:
    board[move[0]][move[1]] = player
    return board

def get_winning_player(board: List[List[str]], player: str) -> str:
    #win for horizontal
    for row in board:
        if row.count(player) == 3:
            return player

    #win for vertical
    counter: int = 0
    if ["X", "O"] in board[0]:
        index_:int = board[0].index(player)
        for row in board:
            if row[index_] == player:
                counter += 1
        if counter == 3:
            return player    

    #win for diagonal from 0,0
    counter = 0
    for i, row in enumerate(board):
        if row[i] == player:
            counter += 1
    if counter == 3:
        return player

    #win for diagonal from 0,2
    counter = 0
    for i, row in enumerate(board):
        if row[len(row)-1-i] == player:
            counter += 1
    if counter == 3:
        return player
    return None

def check_board_full(board: List[List[str]]) -> bool:
    for row in board:
        if "." in row:
            return False
    else:
        return True       


def print_board(board: List[List[str]]) -> None:
    print("   1   2   3")
    separator_pattern: str = "---+---+---"
    row_index: List[str] = ["A", "B", "C"]
    for i,row in enumerate(board):
        print(f"{row_index[i]}  " + ' | '.join(row))
        if i != len(board) - 1:
            print(f"  {separator_pattern}")


def print_game_result(player: str) -> None:
    if player == "X":
        print("X has won!")
    elif player == "O":
        print("O has won!")
    else:
        print("It's a tie!")

def tic_tac_toe() -> None:
    board: List[List[str]] = get_empty_board()
    player: str = "X"
    wait_for_winner = True
    while not check_board_full(board) and wait_for_winner:
        print_board(board)
        print(f"It's Player {player}'s turn!")
        move: Tuple[int, int] = get_human_coordinates(board)
        board = marking_move(player, board, move)
        if get_winning_player(board, player):
            os.system('clear')
            print_board(board)
            print_game_result(player)
            wait_for_winner = False
        else:    
            player = change_player(player)
            os.system('clear') 

tic_tac_toe()



