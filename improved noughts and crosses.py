grid = [["-"] * 3 for _ in range(3)]

def print_grid():
    for row in grid:
        print("".join(row))
    print()

def check_winner():
    lines = (
        # rows
        grid +
        # columns
        [[grid[r][c] for r in range(3)] for c in range(3)] +
        # diagonals
        [[grid[i][i] for i in range(3)], [grid[i][2 - i] for i in range(3)]]
    )
    for line in lines:
        if line[0] != "-" and all(cell == line[0] for cell in line):
            return True
    return False

def is_draw():
    return all(cell != "-" for row in grid for cell in row)

def valid_move(x, y):
    return 0 <= x < 3 and 0 <= y < 3 and grid[x][y] == "-"

def make_move(player):
    mark = "O" if player == 1 else "X"
    while True:
        try:
            x, y = map(int, input(f"Player {player} ({mark}) enter row and column (0–2): ").split())
            if valid_move(x, y):
                grid[x][y] = mark
                break
            else:
                print("Invalid or filled position, try again.")
        except ValueError:
            print("Please enter two numbers separated by a space.")

def play_game():
    print_grid()
    for turn in range(9):  # max 9 moves
        player = 1 if turn % 2 == 0 else 2
        make_move(player)
        print_grid()
        if check_winner():
            print(f"Player {player} wins!")
            return
        if is_draw():
            print("It's a draw!")
            return
    print("It's a draw!")

play_game()
