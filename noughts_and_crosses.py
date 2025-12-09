grid = [["-","-","-"],["-","-","-"],["-","-","-"]]
winner = ""
won = False
gridFilled = False


def printGrid():
    print(grid[0][0]+grid[0][1]+grid[0][2])
    print(grid[1][0]+grid[1][1]+grid[1][2])
    print(grid[2][0]+grid[2][1]+grid[2][2])

def checkGrid():
    won = False
    for i in range(0, 3):
        if (grid[i][0] == grid[i][1] and grid[i][0] == grid[i][2] and (grid[i][0] != "-" and grid[i][1] != "-" and grid[i][2] != "-")) or (grid[0][i] == grid[1][i] and grid[0][i] == grid[2][i] and (grid[0][i] != "-" and grid[1][i] != "-" and grid[2][i] != "-")) or (grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2] and (grid[0][0] != "-" and grid[1][1] != "-" and grid[2][2] != "-")) or (grid[2][0] == grid[1][1] and grid[2][0] == grid[0][2] and (grid[2][0] != "-" and grid[1][1] != "-" and grid[0][2] != "-")):
            won = True
        
    
    if won == True:
        return won
    else:
        print("Game not yet won")
        
def checkDraw():
    draw = True
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "-":
                draw = False
    
    return draw

def checkGridFilled(x, y):
    gridFilled = False
    if grid[x][y] == "-":
        gridFilled = False
    else:
      gridFilled = True
    return gridFilled 
    
def setValue(x, y, player):
    if player == 1:
        grid[x][y] = "O"
    else:
        grid[x][y] = "X"


while not won:
  printGrid()
  move_p1 = input("Player 1 turn, please enter row and column numbers separated by a space (please input numbers 0, 1 or 2 only): ").split()
  x_p1 = int(move_p1[0])
  y_p1 = int(move_p1[1])
  
  gridFilled = checkGridFilled(x_p1, y_p1)
  while gridFilled == True:
      move_p1 = input("Space already taken, please re-enter").split()
      x_p1 = int(move_p1[0])
      y_p1 = int(move_p1[1])
  
      gridFilled = checkGridFilled(x_p1, y_p1)
  
  setValue(x_p1, y_p1, 1)
  
  printGrid()
  gameWon = checkGrid()
  if gameWon == True:
    winner = "Player 1"
    break
  else:
    draw = checkDraw()
    if draw == True:
        print("You drew!")
        winner = "No one"
        break



  move_p2 = input("Player 2 turn, please enter row and column numbers separated by a space (please input numbers 0, 1 or 2 only): ").split()
  x_p2 = int(move_p2[0])
  y_p2 = int(move_p2[1])
  
  gridFilled = checkGridFilled(x_p2, y_p2)
  while gridFilled == True:
      move_p2 = input("Space already taken, please re-enter").split()
      x_p2 = int(move_p2[0])
      y_p2 = int(move_p2[1])
  
      gridFilled = checkGridFilled(x_p2, y_p2)
  
  setValue(x_p2, y_p2, 2)
  
  printGrid()
  gameWon = checkGrid()
  if gameWon == True:
    winner = "Player 2"
    break
  else:
    draw = checkDraw()
    if draw == True:
        print("You drew!")
        winner = "No one"
        break

print("Game over")
print(winner, "wins!")

