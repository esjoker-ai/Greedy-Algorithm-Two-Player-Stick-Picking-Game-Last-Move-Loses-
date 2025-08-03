# Variable initialization
import random
sticks = random.randint(7,10) # use randint() for generate random numbers
print(f'Initial number of stikers are {sticks}')
player = "P1"
for i in range(0, 10):
  print(player)
  
def player_shifter(player): # Player shifter function
  if player == "P1":
    return "P2"
  else:
    return "P1"
def turn(player, sticks): # Turn Function Plays turn of current player
  print(f"{player}'s Turn...")
  if sticks == 1:
    s = int(input("You can only pick one: "))
    return 0
  while(True):
      s = int(input("Enter the number of sticks you want to pick: "))
      if s == 1 or s == 2:
        break
      else:
        print("Wrong Input")
  sticks = sticks - s
  print(f'{sticks} sticks are left')
  return sticks
  # main block
# stop when all sticks are picked up and limit input from 1 to 2
while sticks > 0: 
  sticks = turn(player, sticks)
  player = player_shifter(player)
else:
  player = player_shifter(player)
  print(f"{player} is winner")

