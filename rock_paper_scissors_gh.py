import random
import time

classic = ["rock", "paper", "scissors"]
lightning = ["rock", "gun", "lightning", "devil", "dragon", "water", "air", "paper", "sponge", "wolf", "tree", "human", "snake", "scissors", "fire"]
spock = ["rock", "paper", "scissors", "lizard", "spock"]


winner_classic = {"rock":"scissors", "paper": "rock", "scissors": "paper"}
winner_spock = {"rock":("scissors","lizard"), "paper": ("rock", "spock"), "scissors": ("paper", "lizard"), "lizard": ("paper", "spock"), "spock": ("rock", "scissors")}
winner_lightning = {
    "rock":("fire", "scissors","snake","human","tree","wolf","sponge"),
    "fire":("scissors","snake","human","tree","wolf","sponge","paper"),
    "scissors":("snake","human","tree","wolf","sponge","paper","air"),
    "snake":("human","tree","wolf","sponge","paper","air", "water"),
    "human":("tree","wolf","sponge","paper","air", "water","dragon"),
    "tree":("wolf","sponge","paper","air", "water","dragon","devil"),
    "wolf":("sponge","paper","air", "water","dragon","devil","lightning"),
    "sponge":("paper","air", "water","dragon","devil","lightning","gun"),
    "paper":("air", "water","dragon","devil","lightning","gun","rock"),
    "air":("water","dragon","devil","lightning","gun","rock","fire"),
    "water":("dragon","devil","lightning","gun","rock","fire","scissors"),
    "dragon":("devil","lightning","gun","rock","fire","scissors","snake"),
    "devil":("lightning","gun","rock","fire","scissors","snake","human"),
    "lightning":("gun","rock","fire","scissors","snake","human","tree"),
    "gun":("rock","fire","scissors","snake","human","tree","wolf"),
    }

def introduction():
    print("Let's play game!")
    time.sleep(2)
    name = input("Enter your name: ")
    print(f"Hello, {name}")
    time.sleep(1)
    gtype = True
    while gtype:
        game_type = input("Write type of game (classic, spock, lightning): ")
        if game_type not in ["classic", "spock", "lightning"]:
            print("Invalid input")
        else:
            gtype = False
    print("Okay, let's start")
    return game_type

def classic_game(person_move):
    pc_move = random.choice(classic)
    human_won = (f"Well done. Computer chose {pc_move} and failed")
    pc_won = (f"Sorry, but computer chose {pc_move}")
    draw = (f"There is a draw ({pc_move})")
    if person_move not in ["rock", "paper", "scissors", "!exit"]:
        print("Invalid input")
    elif pc_move == person_move:
        print(draw)
    elif winner_classic[pc_move] == person_move:
        print(pc_won)
    else:
        print(human_won)

def spock_game(person_move,score):
    pc_move = random.choice(spock)
    human_won = (f"Well done. Computer chose {pc_move} and failed")
    pc_won = (f"Sorry, but computer chose {pc_move}")
    draw = (f"There is a draw ({pc_move})")
    if person_move not in ["!exit", "rock", "paper", "scissors", "lizard", "spock"]:
        print("Invalid input")
    elif pc_move == person_move:
        print(draw)
    elif winner_spock[pc_move][0] == person_move or winner_spock[pc_move][1] == person_move:
        print(pc_won)
    elif person_move == "!exit":
        exit()
    else:
        print(human_won)
        score += 100

def lightning_game(person_move, score):
    pc_move = random.choice(lightning)
    human_won = (f"Well done. Computer chose {pc_move} and failed")
    pc_won = (f"Sorry, but computer chose {pc_move}")
    draw = (f"There is a draw ({pc_move})")
    win_light = (winner_lightning[pc_move][0], winner_lightning[pc_move][1],winner_lightning[pc_move][2], winner_lightning[pc_move][3],winner_lightning[pc_move][4], winner_lightning[pc_move][5],winner_lightning[pc_move][6])
    if person_move not in ["!exit", "rock", "gun", "lightning", "devil", "dragon", "water", "air", "paper", "sponge", "wolf", "tree", "human", "snake", "scissors", "fire"]:
        print("Invalid input")
    elif pc_move == person_move:
        print(draw)
        score += 50
    elif person_move in win_light:
        print(pc_won)
    else:
        print(human_won)
        score += 100

def game():
    game_type = introduction()
    play = True
    while play:
        person_move = input()
        if person_move == "!exit":
            break
        if game_type == "classic":
            classic_game(person_move)
        if game_type == "spock":
            spock_game(person_move)
        if game_type == "lightning":
            lightning_game(person_move)
    print("Bye!")

game()
