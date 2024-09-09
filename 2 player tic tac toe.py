board = [[1 , 2 , 3] , [4 , 5 , 6] , [7 , 8 , 9]]
free_spaces = []
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

def enter_move_P1(board):
    register = False
    while not register:
        global check1
        check1 = 0
        try:
         move = int(input(f"Enter your move {P1}: "))
         if move < 1 or move > 9:
            check1 = 1                        
         elif move not in free_spaces:
            check1 = 2
         else:
            if move in board[0]:
                board[0][move-1] = 'X'
            elif move in board[1]:
                board[1][move-4] = 'X'
            else:
                board[2][move-7] = 'X'
        except ValueError:
         check1 = 3 
        register = True 

def enter_move_P2(board):
    register = False
    while not register:
        global check2
        check2 = 0
        try:
          move1 = int(input(f"Enter your move {P2}:"))
          if move1 < 1 or move1 > 9:
            check2 = 1 
          elif move1 not in free_spaces:
            check2 = 2
          else:
            if move1 in board[0]:
                board[0][move1-1] = 'O'
            elif move1 in board[1]:
                board[1][move1-4] = 'O'
            else:
                board[2][move1-7] = 'O'
        except ValueError:
            check2 = 3
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
            person = P2
        else:
            person = P1   
        if board[0] == [sign , sign , sign]:
            return (  f"{person} wins!")
        elif board[1] == [sign , sign , sign]:
            return (  f"{person} wins!")
        elif board[2] == [sign , sign , sign]:
            return (  f"{person} wins!")
        elif [ board[0][0] , board[1][0] , board[2][0] ] == [sign , sign , sign]:
            return (  f"{person} wins!")
        elif [ board[0][1] , board[1][1] , board[2][1] ] == [sign , sign , sign]:
            return (  f"{person} wins!")
        elif [ board[0][2] , board[1][2] , board[2][2] ] == [sign , sign , sign]:
            return (  f"{person} wins!")
        elif [ board[0][0] , board[1][1] , board[2][2] ] == [sign , sign , sign]:
            return (  f"{person} wins!")
        elif [ board[0][2] , board[1][1] , board[2][0] ] == [sign , sign , sign]:
            return (  f"{person} wins!")
        else:
            continue

sign = ''
print("Welocome to tic tac toe !")
print("Please select players!")
P1 = input("Please Enter Name for Player using X :")
P2 = input("Please Enter Name for Player using 0 :")
while True:
    display_board(board)
    make_list_of_free_fields(board)
    if free_spaces == []:
        print("It's a tie")
       # check = True
        break
    else:
        while True : 
         enter_move_P1(board)
         if check1 == 1:
            print("Invalid number please try again!") # String handle 
            continue
         elif check1 == 3 :
             print("Invalid Input!")
             continue
         elif check1 == 2:
            print("Space already occupied please enter another number!")
            continue   
         elif free_spaces == []:
            print("It's a tie")
            break
         elif victory_for(board, sign) == f"{P1} wins!":
            display_board(board)
            print(f"{P1} wins!")
            break
         else : 
             break 
        display_board(board)
        make_list_of_free_fields(board)
        if free_spaces == []:
            print("It's a tie")
            break
        while True : 
         enter_move_P2(board)
         if check2 == 1:
            print("Invalid number please try again!")
            continue
         elif check2 == 2:
            print("Space already occupied please enter another number!")
            continue
         elif check2 == 3 :
             print("Invalid Input!")
             continue
         elif victory_for(board, sign) == f"{P2} wins!":
            display_board(board)
            print(f"{P2} wins!")
            break
         else:
            break 

