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
                   

                                      
     

import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
    
def calculate_score(list):
    if 11 in list and sum(list)>21:
        list.remove(11)
        list.append(1)
    
    if sum(list)==21:
        return 0
    return sum(list)

def compare(user_score,computer_score):
    if user_score>21 and computer_score>21:
        return "\n\tYou went over, you lose!"

    
    if user_score==computer_score:
        return "\n\tDraw"
    elif computer_score==0:
        return "\n\tYou lose, Dealer has Blackjack!"
    elif user_score==0:
        return "\n\tWin with a Blackjack"
    elif user_score>21:
        return "\n\tYou went over, you lose!"
    elif computer_score>21:
        return "\n\tDealer went over, you win!"
    elif user_score>computer_score:
        return "\n\tYou Win!"
    else:
        return "\n\tYou lose!"

    
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    program_run = True
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while program_run:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\n\tYour cards: {user_cards}, current score: {user_score}")
        print(f"\n\tComputer's first card: {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            program_run=False
        else:
            opt = input("\n\tType hit to pick another card, otherwise type stand.\n")
            if opt=="hit":  
                user_cards.append(deal_card())
            else:
                program_run=False
    
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\n\tYour final hand: {user_cards}, final score: {user_score}")
    print(f"\n\tComputer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("\n\tDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()