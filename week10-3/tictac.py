import random
def print_board(board):
    # Print the current state of the board 
    print("Current board:")
    # Join each row with ' | ' and print it
    for row in board:
        print(" | ".join(row))
        # Print a separator line
        print("-" * 9)
def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        # Check if all elements in the row are the same and not empty
        # If so, return the winner
        # If all elements in the row are the same and not empty, return the winner
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    for col in range(3): 
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None
def is_board_full(board):
    # Check if the board is full (no empty spaces)
    # Iterate through each row in the board
    for row in board:
        if " " in row:
            return False
    return True
def make_move(board, row, col, player):
    # Check if the move is valid (the cell is empty)
    # If the cell is empty, place the player's symbol in that cell
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False    
def get_available_moves(board):
    # Get a list of all available moves (empty cells)
    moves = []
    # Iterate through each cell in the board
    for i in range(3):
        # If the cell is empty, add its coordinates to the moves list
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves
def play_game():
    # Initialize the game board and players
    board = [[" " for _ in range(3)] for _ in range(3)]
    # Randomly choose the starting player
    players = ["X", "O"]
    current_player = random.choice(players) 


    while True:
        print_board(board)
        if is_board_full(board):
            print("It's a draw!")
            break
        
        if current_player == "X":
            row, col = map(int, input(f"Player {current_player}, enter your move (row and column): ").split())
        else:
            row, col = random.choice(get_available_moves(board))
            print(f"Player {current_player} (AI) chooses: {row} {col}")
        
        if make_move(board, row, col, current_player):
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")
if __name__ == "__main__":
    play_game()

