from pydoc import doc
import random
def game():
  inputs = ["R", "P", "S"]
  cpu = random.choice(inputs)

#get users input and validate
  user_input = None
  while user_input not in inputs:
    user_input = input("Select an input:\nR for rock\nP for paper\nS for scissors: ")

  #print result
  def moves(select,player):
    if select == "R":
      return player,"(Rock)"
    elif select == "S":
      return player,"(Scissors)"
    elif select == "P":
      return player,"(Paper)"

  #check user_input and cpu
  player_moves = moves(user_input,"Player")
  cpu_moves = moves(cpu, "CPU")
  #tie
  if user_input == cpu:
    print("it\'s a tie\n")
    print(player_moves,":",cpu_moves)
    game()
  #endtie
  elif user_input == "R":
    if cpu == "S":
      print("Rock beats Scissors")
      print(player_moves,":",cpu_moves)
      print("PLAYER WINS")
    else:
      print("Paper beats Rock.")
      print(player_moves,":",cpu_moves)
      print("CPU WINS")
  elif user_input == "P":
    if cpu == "S":
      print("Scissors beats Paper.")
      print(player_moves,":",cpu_moves)
      print("CPU WINS")
    else:
      print("Paper beats Rock.")
      print(player_moves,":",cpu_moves)
      print("PLAYER WINS")
  elif user_input == "S":
    if cpu == "P":
      print("Scissors beats paper.")
      print(player_moves,":",cpu_moves)
      print("PLAYER WINS")
    else:
      print("Rock beats Scissors")
      print(player_moves,":",cpu_moves)
      print("CPU WINS")
#call game
game()  
