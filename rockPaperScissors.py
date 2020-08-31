
#Boilerplate
import time
import random
import sys
choices = ["rock", "paper", "scissors"]
valid = ["rock", "paper", "scissors", "stop"]
outcomes = ["draws!", "loses!", "wins!"]
player_input = ""
computer_score = 0
player_score = 0

#FUNCTION DEFINING TIME!

#CHECKS PLAYER INPUT IS VALID
def check_valid(player_inp) :
    while(player_inp.lower() not in valid) :
        player_inp = input("Please enter 'rock', 'paper', 'scissors', or 'stop'. ")
    return player_inp
    
#CHECKS IF PLAYER SAID 'STOP'
def check_stop(player_inp) :
    if (player_inp.lower() == "stop") :
        time.sleep(1.5)
        print("See ya!")
        return True
        sys.exit()

#CREATES COMPUTER CHOICE
def computer_choice_maker() :
    computer_choice = random.randrange(0,3)
    print("Computer has decided!")
    return computer_choice

#CONVERTS PLAYER INPUT INTO PROGRAM-READABLE FORMAT
def player_convert(player_inp) :
    return choices.index(player_inp)

#DECIDES WHO WON
def decisions(computer_choice, player_choice) :
    return outcomes[(computer_choice - player_choice) %3]

#SCOREBOARD COUNTER
def scoreboard(computer_choice, player_choice) :
    global computer_score
    global player_score
    did_lose = ((computer_choice - player_choice) %3 ==1)
    did_win = ((computer_choice - player_choice) %3 ==2)
    if did_lose :
        computer_score
        computer_score+= 1
    if did_win :
        player_score
        player_score += 1
 
    
# </FUNCTION DEFINING TIME>

#INTRO TO GAMEPLAY
print("Let's play Rock, Paper, Scissors!")
time.sleep(1)
print("To stop the game, say 'stop' at any time!")
time.sleep(1.5)
#GAMEPLAY LOOP
while("true" == "true") :
     print("New Round!")
     time.sleep(1)
     computer_var = computer_choice_maker()
     player_input = input("Player choice: ")
     player_input = check_valid(player_input)
     check_stop(player_input)
     time.sleep(1)
     player_number = player_convert(player_input)
     print("Computer chose " + choices[computer_var] + "!")
     time.sleep(1)
     print("Player " + decisions(computer_var, player_number))
     time.sleep(2)
     scoreboard(computer_var, player_number)
     time.sleep(1)
     print("Player score : " ,player_score)
     time.sleep(1)
     print("Computer score : " ,computer_score)
     time.sleep(3)
     print("")
     print("")
     
     
     
        
