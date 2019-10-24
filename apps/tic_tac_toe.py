board = ["  " for i in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
        
    print("Your turn player {}".format(number))
    
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice -1] == "  ":
        board[choice -1 ] = icon
    else:
        print()
        print("That space is taken!")
        
def check_board(a,b,c, icon):
    # This checks to see if pos a,b,c are the same icon
    win = False
    if board[a] == icon:
        if board[b] == icon:
            if board[c] == icon:
                win = True
    return win

def is_victory(icon):
    winlines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    win = False
    for line in winlines:
        if not win:
            win = check_board(line[0],line[1],line[2], icon)
    return win
            
def is_draw():
    if "  " not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X Wins! Congratulations!")
        break
    elif is_draw():
        print("Its a draw!")
        break
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O Wins! Congratulations!")
        break
    elif is_draw():
        print("Its a draw!")
        break

    

    
