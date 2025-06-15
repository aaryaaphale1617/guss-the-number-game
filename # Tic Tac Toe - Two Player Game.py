# Tic Tac Toe - Two Player Game

def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("🎮 Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))

            if board[row][col] != " ":
                print("⛔ Cell already taken! Try again.")
                continue

            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"🏆 Player {current_player} wins!")
                break
            elif is_draw(board):
                print("🤝 It's a draw!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"
        except (ValueError, IndexError):
            print("⚠️ Invalid input! Enter numbers between 0 and 2.")

# Run the game
tic_tac_toe()
