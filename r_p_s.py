from random import randint

rounds = int(input("You will play rock paper scissors! - CHOOSE amount of ROUNDS: "))

def game(rounds):

    user_score = 0
    comp_score = 0
    current_round = 1

    if rounds <= 0:
        print("You choose the wrong number 	｡ﾟ･ (>﹏<) ･ﾟ｡")
        return "ERROR"

    for i in range(0, rounds):
        user = int(input("\n" + r"rock(0)/paper(1)/scissors(2)? "))

        while user < 0 or user > 2:
            print("You choose the wrong number 	｡ﾟ･ (>﹏<) ･ﾟ｡")
            user = int(input("\n" + r"rock(0)/paper(1)/scissors(2)? "))
       
        computer = randint(0,2)
        if computer == 0:
            print("computer choosed ROCK!", end="  ")
        elif computer == 1:
            print("computer choosed PAPER!", end="  ")
        else:
            print("computer choosed SCISSORS!", end="  ")

        if user - computer == 0:
            print("it`s DRAW 0_0")
        elif user - computer == 1 or user - computer == -2:
            print("you WIN:)")
            user_score += 1
        else:
            print("you LOSE:(")
            comp_score += 1

        print(f"\nIt was ROUND {current_round}! Score: YOU [ {user_score} ] - COMP [ {comp_score} ]")
        current_round += 1
    if user_score == comp_score:
        print(r"MATCH ended in a draw  ¯\_(ツ)_/¯ ")
    elif user_score > comp_score:
        print(r"You WON this MATCH 	<(￣︶￣)>")
    else:
        print(r"You LOSE this MATCH (・`ω´・)")

game(rounds)