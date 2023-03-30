import math

# The Tic Tac Toe board is represented as a 3x3 array of integers:
# 0 represents an empty space, 1 represents X, and -1 represents O.
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# The maximizing player is X, and the minimizing player is O.
MAX_PLAYER = 1
MIN_PLAYER = -1

# The utility function calculates the score for the current board state.
# If X wins, the score is 1; if O wins, the score is -1; otherwise, the score is 0.
def utility(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == MAX_PLAYER:
                return 1
            elif board[i][0] == MIN_PLAYER:
                return -1
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == MAX_PLAYER:
                return 1
            elif board[0][i] == MIN_PLAYER:
                return -1
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == MAX_PLAYER:
            return 1
        elif board[0][0] == MIN_PLAYER:
            return -1
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == MAX_PLAYER:
            return 1
        elif board[0][2] == MIN_PLAYER:
            return -1
    return 0

# The alpha-beta search function performs a depth-limited search of the game tree.
# It returns the best move for the current player.
def alpha_beta_search(board, depth, alpha, beta, player):
    if depth == 0 or utility(board) != 0:
        return None, utility(board)
    if player == MAX_PLAYER:
        best_score = -math.inf
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = MAX_PLAYER
                    _, score = alpha_beta_search(board, depth-1, alpha, beta, MIN_PLAYER)
                    board[i][j] = 0
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
                    alpha = max(alpha, best_score)
                    if alpha >= beta:
                        break
            if alpha >= beta:
                break
        return best_move, best_score
    else:
        best_score = math.inf
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = MIN_PLAYER
                    _, score = alpha_beta_search(board, depth-1, alpha, beta, MAX_PLAYER)
                    board[i][j] = 0
                    if score < best_score:
                        best_score = score
                        best_move = (i, j)
                    beta = min(beta, best_score)
                    if alpha >= beta:
                        break
            if alpha >= beta:
                break
        return best_move, best_score

# The main game loop.
# The main game loop.
def play_game():
    print("Welcome to Tic Tac Toe!")
    print("You are X.")
    print("Enter the row and column number (0-2) of your move, separated by a space.")

    # The game loop continues until the board is full or one player wins.
    while True:
        print("Current board state:")
        for row in board:
            print(row)

        # The human player takes a turn.
        while True:
            try:
                row, col = map(int, input("Your move: ").split())
                if board[row][col] == 0:
                    board[row][col] = MAX_PLAYER
                    break
                else:
                    print("That space is already taken.")
            except:
                print("Invalid input. Please try again.")

        # Check if the human player has won.
        if utility(board) == 1:
            print("Congratulations! You win!")
            break

        # Check if the board is full.
        if all(all(row) for row in board):
            print("It's a tie!")
            break

        # The AI takes a turn.
        print("AI is thinking...")
        move, _ = alpha_beta_search(board, depth=6, alpha=-math.inf, beta=math.inf, player=MIN_PLAYER)
        board[move[0]][move[1]] = MIN_PLAYER

        # Check if the AI has won.
        if utility(board) == -1:
            print("Sorry, you lose!")
            break
play_game()
