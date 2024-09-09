import random

def display_board(board):
    print('+-------'*3, '+' , sep = '')
    print('|       '*3, '|' , sep = '')
    print('|    ' , board[0][0] , '  |    ' ,  board[0][1] , '  |    ' , board[0][2] , '  |' , sep = '')
    print('|       '*3, '|' , sep = '')
    print('+-------'*3, '+' , sep = '')
    print('|       '*3, '|' , sep = '')
    print('|    ' , board[1][0] , '  |    ' ,  board[1][1] , '  |    ' , board[1][2] , '  |' , sep = '')
    print('|       '*3, '|' , sep = '')
    print('+-------'*3, '+' , sep = '')
    print('|       '*3, '|' , sep = '')
    print('|    ' , board[2][0] , '  |    ' ,  board[2][1] , '  |    ' , board[2][2] , '  |' , sep = '')
    print('|       '*3, '|' , sep = '')
    print('+-------'*3, '+' , sep = '')

def enter_move(board):
    register = False
    while not register:
        global check1
        check1 = 0
        try:
         move = int(input("Enter number where you want to place 'O': "))
         if move < 1 or move > 9:
            check1 = 1 
         elif move not in free_spaces:
            check1 = 2
         else:
            if move in board[0]:
                board[0][move-1] = 'O'
            elif move in board[1]:
                board[1][move-4] = 'O'
            else:
                board[2][move-7] = 'O'
        except ValueError:
            check1 = 3
        register = True 

def make_list_of_free_fields(board):
    free_spaces.clear()
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ['X' , 'O']:
                free_spaces.append(board[row][column])
            
        
            
def victory_for(board, sign):
    for sign in ['O' , 'X']:
        if  sign == 'O': 
            person = 'Player'
        else:
            person = 'Computer'
        
            
        if board[0] == [sign , sign , sign]:
            return (person + " wins!")
        elif board[1] == [sign , sign , sign]:
            return (person + " wins!")
        elif board[2] == [sign , sign , sign]:
            return (person + " wins!")
        elif [ board[0][0] , board[1][0] , board[2][0] ] == [sign , sign , sign]:
            return (person + " wins!")
        elif [ board[0][1] , board[1][1] , board[2][1] ] == [sign , sign , sign]:
            return (person + " wins!")
        elif [ board[0][2] , board[1][2] , board[2][2] ] == [sign , sign , sign]:
            return (person + " wins!")
        elif [ board[0][0] , board[1][1] , board[2][2] ] == [sign , sign , sign]:
            return (person + " wins!")
        elif [ board[0][2] , board[1][1] , board[2][0] ] == [sign , sign , sign]:
            return (person + " wins!")
        else:
            continue
        
            
def draw_move(board):
    for i in range(1000):
        cmove = random.randint(1,9)
        if cmove in free_spaces:
            if cmove in board[0]:
                board[0][cmove-1] = 'X'
                break
            elif cmove in board[1]:
                board[1][cmove-4] = 'X'
                break
            elif cmove in board[2]:
                board[2][cmove-7] = 'X'
                break
            
        else:
            continue
            
    
board = [[1 , 2 , 3] , [4 , 'X' , 6] , [7 , 8 , 9]]
free_spaces = []
sign = ''
check = False
while not check:
    display_board(board)
    make_list_of_free_fields(board)
    if free_spaces == []:
        print("It's a tie")
        check = True
        break
    else:
        enter_move(board)
        if check1 == 1:
            print("Invalid number please try again!")
            continue
        elif check1 == 2:
            print("Space already occupied please enter another number!")
            continue
        elif check1 == 3:
            print("Please enter a valid input!")
    
        elif free_spaces == []:
            print("It's a tie")
            break
        elif victory_for(board, sign) == "Player wins!":
            display_board(board)
            print("Player wins!")
            break
        elif victory_for(board, sign) == "Computer wins!":
            display_board(board)
            print("Computer wins!")
            break
        make_list_of_free_fields(board)
        if free_spaces == []:
            print("It's a tie")
            break
        draw_move(board)
        if free_spaces == []:
            print("It's a tie")
            break
        elif victory_for(board, sign) == "Player wins!":
            display_board(board)
            print("Player wins!")
            break
        elif victory_for(board, sign) == "Computer wins!":
            display_board(board)
            print("Computer  wins!")
            break
        else:
            continue
