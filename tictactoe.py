def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)
def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False
def check_win(board, player):

    for row in board:
        if all([cell == player for cell in row]):
            return True
    

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    
    return False

def check_draw(board):
    return all([cell != " " for row in board for cell in row])
def main():
    board = create_board()
    current_player = "X"
    
    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (0-2): "))
        col = int(input(f"Player {current_player}, enter the column (0-2): "))
        
        if make_move(board, row, col, current_player):
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("The game is a draw!")
                break
            
            # Switch players
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
