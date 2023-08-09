import random
import os

cards_dict = {}
deck = []


def clear():
    os.system('cls') if os.name == 'nt' else os.system('clear')


clear()


def populate_deck(faces):
    colors = ['Spades ♠️', 'Hearts ♥️', 'Diamonds 🔶', 'Clubs ♣️']
    for face, value in faces:
        cards_dict[str(face)] = value
        for color in colors:
            card = f'{face} of {color}'
            deck.append(card)


def create_deck():
    populate_deck([['Ace', 11]])
    populate_deck([['King', 10], ['Queen', 10], ['Jack', 10]])
    for num in range(2, 11):
        populate_deck([[num, num]])


def deal_card(quantity):
    cards = []
    for _ in range(quantity):
        card = deck.pop(deck.index(random.choice(deck)))
        cards.append(card)
    if len(cards) > 1:
        return cards
    else:
        return cards[0]


def calculate_hand_value(hand):
    value = 0
    aces = []
    for card in hand:
        key = card.split(' ')[0]
        if key == 'Ace':
            aces.append(key)
        value += cards_dict[key]
        if value > 21 and aces:
            aces.pop()
            value -= 10

    return value


def display_player_summary(player, hand):
    cards_on_hand = ', '.join(hand)
    cards_value = calculate_hand_value(hand)
    emoji = '🙂' if player == 'player' else '💻'
    print(f"{emoji} {player} hand: {cards_on_hand}.\nTotal value of {player} cards: {cards_value}\n")


computer_hand = []
player_hand = []


def init():
    global computer_hand
    global player_hand

    create_deck()

    computer_hand = deal_card(2)
    player_hand = deal_card(2)

    display_player_summary('Your', player_hand)
    print('Computer has also 2 cards. You only see the first one.\n')
    display_player_summary('Computer', [computer_hand[0]])
    play_game()


def play_game():

    current_hand_value = 0
    playing = True
    while playing:
        another = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another == 'y':
            clear()
            player_hand.append(deal_card(1))
            display_player_summary('Your', player_hand)
            current_hand_value = calculate_hand_value(player_hand)
            if current_hand_value == 21:
                print('🏆 Black Jack, you win\n')
                playing = False
                replay()
            elif current_hand_value > 21:
                print('😔 Your hand is over 21 in total. You loose\n')
                playing = False
                replay()
            continue
        elif another == 'n':
            clear()
            playing = False
        else:
            print("🚫 Wrong input, type 'y' or 'n'.\n")
            continue
        final_computer_value = computer_round(computer_hand)
        check_winner(computer=final_computer_value, player=current_hand_value)
        replay()


def computer_round(hand):

    playing = True
    while playing:
        computer_hand_value = calculate_hand_value(hand)
        if computer_hand_value < 17:
            computer_hand.append(deal_card(1))
            continue
        else:
            return computer_hand_value


def check_winner(computer, player):

    display_player_summary('Your', player_hand)
    display_player_summary('Computer', computer_hand)

    if computer > player:
        if computer > 21:
            print('🏆 Computer hand is over 21 in total. You win.\n')
        else:
            print('😔 computer wins\n')
    elif player > computer:
        print('🏆 player wins\n')
    else:
        print("🟰 It's a draw\n")


def replay():
    play = input("▶️ Do you want to play again? Type 'y' 👍 or 'n' 👎: ").lower()
    if play == 'y':
        clear()
        init()
    elif play == 'n':
        clear()
        return print('👋 Thank you for playing\n')
    else:
        print("🚫 Wrong input, type 'y' or 'n'.\n")
        replay()


init()
