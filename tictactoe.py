import random
import msvcrt
import os
import Add
import check_win as Check

round_counter = 0
win_condition = False
signs_added_to_board = [" ", " ", " ", " ", " ", " ", " ", " ", " ",]
X_win_counter = 0
O_win_counter = 0
print_once = True
error_printed_once = True
same_input_twice = True

value = random.randint(0, 1)
starting_player = "O" if value == 0 else "X" #Ternary operator

clear = lambda: os.system("cls")

def increment_round():
  global round_counter #Big lesson learned here. If you want to change the value of a global variable you need to use global, otherwise Python will think that you declared a new variable in the local scope.
  round_counter += 1
  
def switch_players():
  global starting_player
  starting_player = "O" if starting_player == "X" else "X"

def thank_you_message():
  clear()
  print("")
  print("     Thanks for playing!")
  print("")

def restart():
  global signs_added_to_board, round_counter, X_win_counter, O_win_counter, print_once, error_printed_once, same_input_twice
  p_input = input("     Want to play again? (Y/n)")
  if p_input == "n":    
    thank_you_message()
  else:
    if starting_player == "X" and round_counter != 9:
      X_win_counter += 1
    elif starting_player == "O" and round_counter != 9:
      O_win_counter += 1    
    switch_players()
    print_once = True
    error_printed_once = True
    same_input_twice = True
    round_counter = 0
    signs_added_to_board = [" " for x in signs_added_to_board]    
    start_game()

def end_game():
  clear()  
  draw_board(signs_added_to_board)
  if win_condition:   
    print("")
    print(f"     Congratulations! {starting_player} has won the game!")  
  else:
    print("")
    print("     It's a draw!")  
  restart()

def new_round():
  global print_once    
  if (round_counter < 9 and not(win_condition)) :
    draw_board(signs_added_to_board)
    switch_players()    
    print(f"     It's {starting_player}'s turn!")
    print_once = True
    player_input()
  else:
    end_game()

def player_input ():
  global win_condition, print_once, error_printed_once, same_input_twice
  if print_once:
    print("")
    print("     Press a button on the Numpad! ")
    print("     Press Esc if you wish to stop playing.")
    print("")
    print_once = False
  input_num = msvcrt.getch()
  if input_num.isdigit():    
    is_ok = Add.add_sign_to_board( input_num, signs_added_to_board, starting_player)
    if is_ok:          
      win_condition = Check.check_for_win( signs_added_to_board, starting_player)
      error_printed_once = error_printed_once = True if False else True
      same_input_twice = same_input_twice=True if False else True
      increment_round()
      new_round()
    else:
      if same_input_twice:
        print("     A mark has already been placed there!")
        same_input_twice = False
      player_input()
  elif not(input_num.isdigit()) and input_num != b'\x1b':
    if error_printed_once:
      print("     Error! A number must be pressed!")
      error_printed_once = False
    player_input() 
  elif input_num == b'\x1b':     
    thank_you_message()     

def start_game():    
    draw_board(signs_added_to_board)
    if round_counter == 0: 
      print(f"     {starting_player} moves first!")
    player_input()

def draw_board(sign): 
    clear()
    print("     Good Luck!")
    print("") 
    print("     +---+---+---+")
    print(f"     | {sign[0]} | {sign[1]} | {sign[2]} |")
    print("     +---+---+---+")
    print(f"     | {sign[3]} | {sign[4]} | {sign[5]} |")
    print("     +---+---+---+")
    print(f"     | {sign[6]} | {sign[7]} | {sign[8]} |")
    print("     +---+---+---+")
    print("")
    print(f"     X has won: {X_win_counter} times!")
    print(f"     O has won: {O_win_counter} times!")
    print("")

start_input = input("     Let's start: (Y/n): ")
if start_input == "n":
  print("     Alright then. Bye!")  
else:
  start_game()


