
def show_board(board):
    for b in board:
        print(" | ".join(b))

def check_winner(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False
def full_board(board):
    for row in board:
        for cell in row:
            if cell == "-":
                return False  # If there's an empty cell, the board is not full
    return True

def main():
    player = "X"
    board =[["-" for _ in range(3)] for _ in range(3)]
    is_running = True
    print("WELCOME TO TIC-TAC-TOE")
    print()
    while is_running:
        show_board(board)
        print()
        row = int(input("Enter the row for your move: "))
        column = int(input("Enter the column for your move: "))
        if not board[row][column] == "-":
            print()
            print("That spot is already taken.Try again!")
            print()
            continue
        else:
            board[row][column] = player

        if check_winner(board,player):
            show_board(board)
            print(f"Player {player} wins!")
            is_running = False
        elif full_board(board):
            print("It's a tie!")
            is_running = False
        else:
            player = "O" if player == "X" else "X"


if __name__ == "__main__":
    main()