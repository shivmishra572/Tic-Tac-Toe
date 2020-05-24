#ASKING USER FOR THEIR CHOICE 
def choose_marker():
    marker=''
    while marker!="X" and marker!="O":
        marker=input("SELECT X or O : ").upper()
    if marker=="X":
        return("X","O")
    elif marker=="O":
        return("O","X")

#CHOOSING RANDOMLY PLAYER1 OR PLAYER 2
import random
def choose_player():
    temp=random.randint(0,1)
    if temp==0:
        return("Player 1")
    else:
        return("Player 2")
#PRINTING THE BOARD
from IPython.display import clear_output
def draw_board(board):
    clear_output()
    print("    ||     ||   ")
    print(" "+board[7]+" "+' || '+" "+board[8]+" "+' || '+" "+board[9])
    print("    ||     ||   ")
    print("----------------")
    print("    ||     ||   ")
    print(" "+board[4]+" "+' || '+" "+board[5]+" "+' || '+" "+board[6])
    print("    ||     ||   ")
    print("----------------")
    print("    ||     ||   ")
    print(" "+board[1]+" "+' || '+" "+board[2]+" "+' || '+" "+board[3])
    print("    ||     ||   ")
    
#ACCEPTING THE POSITION FROM THE USER TO PLACE THE MARKER!!!
def position():
    position=int(input("Choose From 1-9 To Place Your Marker : "))
    return position

#TAKING INPUT FROM USER AND PRINTING IT ON BOARD
def place_marker(board,position,marker):
    board[position]=marker
    
#CHECKING IF THE POSITION GIVEN BY THE USER IS EMPTY OR NOT
def check_space(board,position):
    if board[position]==" ":
        return True
    
#CHEHCKIN IF THE BOARD IS FULL OR MATCH IS TIE!!
def board_check_full(board):
    if " " in board[1:]:
        return False
    else:
        return True

#FUNC TO CHECK IF THE WHICH PLAYER WON THE MATCH
def check_win(board,marker):
    if ((board[1]==board[2]==board[3]==marker) or 
        (board[4]==board[5]==board[6]==marker) or
        (board[7]==board[8]==board[9]==marker) or
        (board[1]==board[4]==board[7]==marker) or
        (board[2]==board[5]==board[8]==marker) or
        (board[3]==board[6]==board[9]==marker) or
        (board[1]==board[5]==board[9]==marker) or
        (board[7]==board[5]==board[3]==marker)):
        return True
    else:
        return False
 
#FUNC FOR ASKING USER TO PLAY AGAIN OR NOT      
def replay():
    r=input("PLAY AGAIN ? : CHOOSE YES OR NO !: ").upper()
    if r=="YES":
        return True
    else:
        return False
#MAIN FUNCTION AND THE LOGIC OF THE GAME
def main():
    print("----------Welcome To Tic-Tac-Toe---------")
    print("----------Rules For Tic-Tac-Toe----------")
    print("1. The game is played on a grid that's 3 squares by 3 squares.")
    print("2. You are X, your friend is O. Players take turns putting their marks in empty squares.")
    print("3. The first player to get 3 of him/her marks in a row (up, down, across, or diagonally) is the winner.")
    print("4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")
    i=input("Would You Like to Play Game ? Yes or No ? : ").upper()
    if i=="YES":
        player1,player2=choose_marker()
        print("Player 1:{} & Player 2:{} ".format(player1,player2))
        board=["#"," "," "," "," "," "," "," "," "," "]
        turn=choose_player()
        print(turn + " Will Play First!!!")
        game_on=True
        while game_on:
            if turn=="Player 1":
                draw_board(board)
                print("Player 1 Turn: ")
                pos=position()
                if check_space(board, pos):
                    place_marker(board,pos,player1)
                    if check_win(board, player1):
                        print("Player 1 won !! Congratulations!!!")
                        draw_board(board)
                        game_on=False
                        #break
                    else:
                        if board_check_full(board):
                            draw_board(board)
                            print("--------Match Ties!!!---------")
                            game_on=False
                            replay()
                        else:
                            turn="Player 2"
                else:
                    print("This Place is Preoccupied !!! TRY WITH DIFFERENT VALUE.!")
                
            else:
                draw_board(board)
                print("Player 2 Turn: ")
                pos=position()
                if check_space(board, pos):
                    place_marker(board,pos,player2)
                    if check_win(board, player2):
                        print("Player 2 won !! Congratulations!!!")
                        draw_board(board)
                        game_on=False
                        #break
                    else:
                        if board_check_full(board):
                            draw_board(board)
                            print("Match Ties!!!")
                            game_on=False
                            replay()
                        else:
                            turn="Player 1"
                else:
                    print("This Place is Preoccupied !!! TRY WITH DIFFERENT VALUE.!")
        else:
            if replay():
                clear_output()
                main()
            else:
                print("Thank You For Playing.!")
    else:
        print("Thank You !!!!")
    
if __name__=="__main__":
    main()