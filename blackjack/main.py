import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards_player = []
cards_computer = []


def display_score():
    print(f"Your cards: {cards_player}, current score : {sum(cards_player)}")
    print(f"Computer's first card: {cards_computer[0]}")


def win_lose():
    sum_player = sum(cards_player)
    sum_computer = sum(cards_computer)
    while sum_computer <= 16:
        cards_computer.append(random.choice(cards))
        sum_computer = sum(cards_computer)

    print(f"Your final hand: {cards_player}, final score: {sum(cards_player)}")
    print(
        f"Computer's final hand: {cards_computer}, final score: {sum(cards_computer)}"
    )
    if sum_player == sum_computer:
        print("Draw")
    elif sum_player > sum_computer and sum_player <= 21 or sum_player < sum_computer and sum_computer >= 21 and sum_player <= 21:
        print("You win")
    elif sum_player < sum_computer and sum_computer <= 21:
        print("You lose")
    else:
        print("You lose")
        
def pick_eleven():
    if sum(cards_computer) > 21 and 11 in cards_computer:
        cards_computer.remove(11)
        cards_computer.append(1)
    if sum(cards_player) > 21 and 11 in cards_player:
        cards_player.remove(11)
        cards_player.append(1)


def black_jack():
        cards_player.append(random.choice(cards))
        cards_player.append(random.choice(cards))
        cards_computer.append(random.choice(cards))
        pick_eleven()
        display_score()
        choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if choice == "y":
            cards_player.append(random.choice(cards))
            cards_computer.append(random.choice(cards))
            cards_computer.append(random.choice(cards))
            pick_eleven()
            display_score()
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == "y":
                cards_player.append(random.choice(cards))
                cards_computer.append(random.choice(cards))
                pick_eleven()
                display_score()
                win_lose()
            else:
                win_lose()
        else:
            win_lose()

def start_game():
    while True:
        game_debut = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if game_debut == 'y':
            black_jack()
        else:
            print("Thanks for playing! Goodbye!")
            break
        
        
start_game()