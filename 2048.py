import random

# Initialize the board
board = [[0] * 4 for _ in range(4)]

# Function to print the board
def print_board():
    print("-------------")
    for row in board:
        print(row)


# Function to add a new random number to the board
def add_number():
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 2

# Function to merge two tiles in a row or column
def merge(line):
    merged = [False] * 4
    new_line = [0] * 4
    index = 0
    for i in range(4):
        if line[i] != 0:
            if merged[i]:
                continue
            if i < 3 and line[i] == line[i+1]:
                new_line[index] = line[i] * 2
                merged[i] = True
                merged[i+1] = True
            else:
                new_line[index] = line[i]
            index += 1
    return new_line

# Function to move tiles in a row or column
def move_left():
    global board
    new_board = []
    for row in board:
        new_row = merge(row)
        new_board.append(new_row)
    board = new_board

def move_right():
    global board
    new_board = []
    for row in board:
        new_row = merge(row[::-1])[::-1]
        new_board.append(new_row)
    board = new_board

def move_up():
    global board
    new_board = [[board[j][i] for j in range(4)] for i in range(4)]
    for i in range(4):
        new_col = merge(new_board[i])
        for j in range(4):
            new_board[i][j] = new_col[j]
    board = [[new_board[j][i] for j in range(4)] for i in range(4)]

def move_down():
    global board
    new_board = [[board[j][i] for j in range(4)] for i in range(4)]
    for i in range(4):
        new_col = merge(new_board[i][::-1])[::-1]
        for j in range(4):
            new_board[i][j] = new_col[j]
    board = [[new_board[j][i] for j in range(4)] for i in range(4)]

# Function to check if the game is over
def is_game_over():
    for row in board:
        if 0 in row:
            return False
        for i in range(3):
            if row[i] == row[i+1]:
                return False
    for col in range(4):
        for i in range(3):
            if board[i][col] == board[i+1][col]:
                return False
    return True

# Main game loop
while True:
    add_number()
    print_board()
    if is_game_over():
        print("Game over!")
        break
    move_made = False
    while not move_made:
        move = input("Enter move (w/a/s/d): ")
        if move == "a":
            move_left()
            move_made = True
        elif move == "d":
            move_right()
            move_made = True
        elif move == "w":
            move_up()
            move_made = True
        elif move == "s":
            move_down()
            move_made = True