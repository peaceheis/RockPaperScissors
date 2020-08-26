#Boilerplate
import time
import sys
import random
choices = {"rock", "paper", "scissors"}
outcomes = {"draws!", "loses!", "wins!"}
sad_replies = {"That was... quick.", "Bye. :(", "See you..."}
computer_count = 0
player_count = 0
player_input = ""
player_equivalent = 0
computer_input = 0
computer_equivalent = ""

#function for deciding computer decision and randomized time for decision
def computer_initiate() :
  for i in range(random.randrange(1,4)) :
    for i in range(3) :
      print("Computer: calculating", end = "")
      time.sleep(1)
      print(".", end = '')
    time.sleep(random.randrange(0,4))
  computer_input = random.randrange(0,3)
  print("Computer has decided!")

try :
  computer_initiate()
#Intro to Game

#print("Let's play Rock, Paper, Scissors!")
#time.sleep(1)
#print("To stop, say 'stop' at any time.")
#print("Let's start!")
#computer_initiate()
#player_input = input("Player, decide: ")
#function for converting input to numbers

