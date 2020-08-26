
#Boilerplate
import time
import sys
import random
choices = ["rock", "paper", "scissors"]
valid = ["rock", "paper", "scissors", "stop"]
outcomes = ["draws!", "loses!", "wins!"]
sad_replies = ["That was... quick.", "Bye. :(", "See you..."]
computer_count = 0
player_count = 0
player_input = ""
player_equivalent = 0
computer_input = 0
computer_equivalent = ""

#function for deciding computer decision and randomized time for decision
def computer_initiate() :
  for i in range(random.randrange(1,4)) :
    print("Computer: calculating ", end = "")
    for i in range(3) :
      print(".", end = '', flush = "true")
      time.sleep(2)
    time.sleep(random.randrange(0,4))
    print("")
  time.sleep(3)
  computer_input = random.randrange(0,3)
  print("Computer has decided!")

#search choices for player's input and return index
def search_choices(input):
    for i in range (len(choices)):
        if choices[i] == input:
            return i
    return -1

#determines winner of round and updates scores
def player_results(player_equivalent, computer_input, countc, countp) :
  if ((computer_input - player_equivalent) % 3) == 1 :
    countc = countc + 1
  elif ((computer_input - player_equivalent) % 3) == 2 :
    countp = countp + 1
  print("Player " + outcomes[(computer - player) % 3])

#Prints scores
  def print_scores() : 
    print("Player's score: " + player_count)
    print("Computer's score :" + computer_count)

#converts computer's number input to string
def computer_convert(computer) :
  return choices[computer]
#First Round

print("Let's play Rock, Paper, Scissors!")
time.sleep(1)
print("To stop, say 'stop' at any time.")
print("Let's start!")
computer_initiate()
player_input = input("Player, decide: ")

#check player input
while player_input.lower() not in valid :
    player_input = input("Please say 'rock', 'paper', 'scissors', or 'stop'.")

#If player immediately says stop, give a sad reply:
if player_input.lower() == "stop" :
  sys.exit(sad_replies[random.randrange(0,2)])

#Logic to determine winner
def decisions() : 
  player_equivalent = search_choices(player_input)
  computer_equivalent = computer_convert(computer_input)
  print("Computer chose: " + computer_equivalent)
  player_results(player_equivalent, computer_input, computer_count, player_count)

decisions
#Rest of Game
while (player_input != "stop") :
  computer_initiate()
  player_input = input("Player, decide: ")
  while player_input.lower() not in valid :
    player_input = input("Please say 'rock', 'paper', 'scissors', or'stop'")
  if player_input.lower() == "stop" :
    break
  decisions()
  

time.sleep(1)
sys.exit("See ya!")



 
