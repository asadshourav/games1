board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_still_loading = True
winner = None
current_player = "x"
def display_board():
    print(board[0] + " | "+board[1] + " | "+board[2])
    print(board[3] + " | "+board[4] + " | "+board[5])
    print(board[6] + " | "+board[7] + " | "+board[8])
def play_game():
    display_board()
    while game_still_loading:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    if winner == "x" or winner == "o":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")
def handle_turn(player):
    print(player +"'s turn.")
    position = input("Choose a number from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input.Choose a position from 1-9: ")
            position = int(position)-1
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there")
    board[position] = player
    display_board()
def check_if_game_over():
    check_if_win()
    check_if_tie()
def check_if_win():
    global winner
    row_winner =row_win()
    column_winner = column_win()
    diagonal_winner = diagonal_win()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner =diagonal_winner
    else:
        winner = None
    return
def row_win():
    global game_still_loading
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_loading = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return
def column_win():
    global game_still_loading
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_loading = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return
def diagonal_win():
    global game_still_loading
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    if diagonal_1 or diagonal_2:
        game_still_loading = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return
def check_if_tie():
    global game_still_loading
    if "-" not in board:
        game_still_loading = False
    return
def flip_player():
    global current_player
    if current_player == "x":
        current_player = "o"
    elif current_player == "o":
        current_player = "x"
    return
play_game()