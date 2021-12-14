import pygame
import time

pygame.init()

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
        drawGrid(arr, 500, 500)
        pygame.display.flip()
        time.sleep(.01)
        if validNum(arr, row, col, x):

            arr[row][col] = x
            drawGrid(arr, 500, 500)
            pygame.display.flip()
            time.sleep(.01)
            #continue to recurse, if solve returns true The solution has been found
            if solve(arr):
                return True
        #this number wasnt a correct solution, replace with 0
        arr[row][col] = 0
        drawGrid(arr, 500, 500)
        pygame.display.flip()
        time.sleep(.01)
    return False


def drawGrid(arr, x, y):
    screen = pygame.display.set_mode([x, y])
    screen.fill((255, 255, 255))
    c = 0

    while c <= 9:
        loc = c * x/9
        if c % 3 == 0:
            pygame.draw.line(screen, (0, 0, 255), (loc,0), (loc,x), 5)
            pygame.draw.line(screen, (0, 0, 255), (0,loc), (y,loc), 5)
        else:
            pygame.draw.line(screen, (0, 0, 255), (loc,0), (loc,x))
            pygame.draw.line(screen, (0, 0, 255), (0,loc), (y,loc))
        c += 1
    drawNums(screen, arr, x, y)
    return screen

def drawNums(screen, grid, x, y):
    xloc = x/9
    yloc = y/9

    fnt = pygame.font.SysFont("Arial", 40)

    for xx in range(10):
        for yy in range(10):
            temp = grid[yy-1][xx-1]
            if temp != 0:
                text = fnt.render(str(temp), 1, (0,128,0))
                screen.blit(text, (xx * xloc - 50, yy * yloc - 50))

    return 0

def main():
    #dim of game board
    x = 500
    y = 500
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    
    running = True
    
    screen = drawGrid(grid, x, y)

    pygame.display.flip()
    while running:
    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solve(grid)
                    #drawGrid(grid, x, y)
                    




if __name__ == "__main__":
    main()
    pygame.quit()