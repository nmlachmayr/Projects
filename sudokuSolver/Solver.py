import math

def pGrid(arr):
    N = len(arr)
    for x in range(N):
        print(arr[x])
    return 0

#check if given num is valid in the row and col
def checkRowCol(arr, row, col, num):
    #check row
    if num in arr[row]:
        return False
    #check col
    for x in range(9):
        if arr[x][col] == num:
            return False
    return True
#check if num is valid in the box
def checkBox(arr, row, col, num):
    Brow = row-row%3
    Bcol = col-col%3
    for x in range(3):
        for y in range(3):
            if arr[x+Brow][y+Bcol] == num:
                return False
    return True

#wrapper for rowcol and box
def validNum(arr, row, col, num):
    if not checkRowCol(arr,row,col,num):
        return False
    if not checkBox(arr,row,col,num):
        return False
    return True
        
#finds first unset space
def findNotSet(arr):
    N = len(arr)
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 0:
                return (x,y)
    return None

#solves sudoku with backtracking
def solve(arr):
    f = findNotSet(arr)
    if f:
        row, col = f
    else:
        return True

    #check 1-9
    for x in range(1,10):
        if validNum(arr, row, col, x):
            arr[row][col] = x

            #continue to recurse, if solve returns true The solution has been found
            if solve(arr):
                return True
        #this number wasnt a correct solution, replace with 0
        arr[row][col] = 0
    return False


def main():
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    solve(grid)
    pGrid(grid)

if __name__ == "__main__":
    main()

