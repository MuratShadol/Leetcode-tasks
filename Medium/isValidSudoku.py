"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 """

from collections import defaultdict


def isValidSudoku(board):
    for i in range(len(board)):
        row_hash = {}
        for j in range(len(board[i])):
            if board[i][j] != ".":
                if row_hash.get(board[i][j]):
                    return False
                else:
                    row_hash[board[i][j]] = True
    
    for j in range(len(board)):
        col_hash = {}
        for i in range(len(board[j])):
            if board[i][j] != ".":
                if col_hash.get(board[i][j]):
                    return False
                else:
                    col_hash[board[i][j]] = True
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = {}
            for k in range(i, i+3):
                for v in range(j, j+3):
                    if board[k][v] != ".":
                        if square.get(board[k][v]):
                            return False
                        else:
                            square[board[k][v]] = True
    return True


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

assert isValidSudoku(board) == True
assert isValidSudoku(board2) == False


def validSudoku(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                if (board[i][j] in rows[i] or
                    board[i][j] in cols[j] or
                    board[i][j] in squares[(i // 3, j // 3)]):
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i // 3, j // 3)].add(board[i][j])

    return True


assert validSudoku(board) == True
assert validSudoku(board2) == False