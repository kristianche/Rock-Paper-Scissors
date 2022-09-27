import random
command = "yes"
wins_player_counter = 0
wins_computer_counter = 0
draws = 0
while command == "yes":
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
        print("Invalid Input. Try again...")
        continue
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
        wins_player_counter += 1
    elif player_move == computer_move:
        print("Draw!")
        draws += 1
    else:
        print("You lose!")
        wins_computer_counter += 1
    command = input("Do you want to continue [yes] or [no]: ")
print("Thank you for playing!")
