import random
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_move = input("Choose [r]ock [p]aper [s]cissors):")
if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")
random_number = random.randint(1, 3)
computer_move = ""
if random_number == 1:
    computer_move = rock
elif random_number == 2:
    computer_move = paper
elif random_number == 3:
    computer_move = scissors
print(f"The computer chose {computer_move}.")
if (player_move == rock and computer_move == scissors) or \
       (player_move == paper and computer_move == rock) or \
       (player_move == scissors and computer_move == paper):
    print("You win!")
elif player_move == computer_move:
    print("Draw!")
else:
    print("You lose!")