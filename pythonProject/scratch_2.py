import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

message = {
    "win_bj": "Win with a Blackjack 😎",
    "win": "You win 😃",
    "win_over": "Opponent went over. You win 😁",
    "draw": "Draw 🙃",
    "lose_bj": "Lose, opponent has Blackjack😱",
    "lose": "You lose 😤",
    "lose_over": "You went over. You lose 😤"
}

situation = {
    "y": True,
    "n": False
}

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def switch(user):
    return situation[user]


def messages(p_score, c_score,p_cards,c_cards):
    if cpu_score == 21 and c_cards == 2:
        return message["lose_bj"]
    elif player_score == 21 and c_cards == 2:
        return message["win_bj"]
    elif player_score > 21:
        return message["lose_over"]
    elif cpu_score > 21:
        return message["win_over"]
    elif player_score > cpu_score:
        return message["win"]
    elif cpu_score > player_score:
        return message["lose"]
    else:
        return message["draw"]


def deal(hand, number_of_cards):
    dealt = hand + random.choices(cards, k=number_of_cards)
    if 11 in hand and sum(cards) > 21:
        dealt.remove(11)
        dealt.append(1)
    return dealt



# While allows the game to restart if we want to
while switch(input("Do you want to play a game of Blackjack? Type 'y' or 'n':")):
    cpu_cards = []
    player_cards = []
    time = 2
    print(logo)
    hit = True


    # Dealing first hand
    cpu_cards = deal(cpu_cards, time)
    cpu_score = sum(cpu_cards)
    while hit:
        player_cards = deal(player_cards, time)
        time = 1
        player_score = sum(player_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {cpu_cards[0]}")

        if ((cpu_score == 21 or player_score == 21) and cpu_cards == 2) or player_score > 21:
            break

        hit = switch(input("Type 'y' to get another card, type 'n' to pass:"))
    while cpu_score < 17:
        cpu_cards = deal(cpu_cards, time)
        cpu_score = sum(cpu_cards)



    win = messages(player_score, cpu_score,player_cards, cpu_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {cpu_cards}, final score:{cpu_score}")
    print(win)
