# Julia Lieberman
# Spring 2020

# problem 4: N-queens (a slightly more advanced iteration of 8 queens)
# this is a very common problem in coding interviews

import numpy #this is to enable the zero-filling matrix function

# set number of queens in problem
N=8

# fill the board with zeroes. dtype=numpy.int makes them ints instead of floats
board=numpy.zeros([N, N], dtype=numpy.int)

# python does a pretty nice job of printing stuff out
def printBoard(board):
    for row in board:
        print(row)


def isValid(board, row, col):
    #check the row and column just to the left of where we are currently
    for i in range(col):
        if board[row][i]==1:
            return False

    for i in range(row):
        if board[i][col]==1:
            return False

    countRow=row
    countCol=col

    #check upper left diagonal
    while countRow >=0 and countCol >= 0:
        if board[countRow][countCol]==1:
            return False
        countRow-=1
        countCol-=1

    #check lower left diagonal. Starting at our current row and column passed in will ensure we aren't looking just at the square diagonals, but at the actual diagonals of the current index
    countRow=row
    countCol=col
    while countRow <= N-1 and countCol >=0:
        if board[countRow][countCol]==1:
            return False
        countRow+=1
        countCol-=1
    return True

#end of isValid function

            
def pythonNQueensProblem(board, index):
    if index>=N:
        return True

    for i in range(N):
        if isValid(board, i, index):
            board[i][index]=1

            if pythonNQueensProblem(board, index+1):
                return True
            else:
                board[i][index]=0 #and go to the next i value in the for loop

    return False

if pythonNQueensProblem(board, 0):
    printBoard(board)
else:
    print("didn't work")
