from json import load

from deck import Card, Deck, get_poker_hand


def load_file(filename: str) -> list:

    output = []

    with open(filename, "r") as my_file:
        content = my_file.read()

    list_of_content = content.split("\n")
    for i in list_of_content:
        output.append(i.split())

    return output


suits_convert = {"H": "Hearts", "S": "Spades", "C": "Clubs", "D": "Diamonds"}


def convert_to_deck_format(card: list):
    if card[0] == "A":
        value = "ace"
    elif card[0] == "K":
        value = "king"
    elif card[0] == "Q":
        value = "queen"
    elif card[0] == "J":
        value = "jack"
    else:
        value = int(card[0])

    return Card(suits_convert[str(card[1])], value)


def who_wins(player_1: list, player_2: list, player1_name: str, player2_name: str) -> dict:
    result = {}
    player_1_hand = get_poker_hand(player_1)
    player_2_hand = get_poker_hand(player_2)
    if player_1_hand > player_2_hand:
        result["winner"] = player1_name
        result["hand"] = player_1_hand
    else:
        result["winner"] = player2_name
        result["hand"] = player_2_hand

    return result


def analyze_hand(hand: list) -> None:

    player_1 = []
    player_2 = []

    for i in hand[0:6:]:
        player_1.append(i)

    for j in hand[6:12:]:
        player_2.append(j)

    converted_player1 = []
    converted_player2 = []
    for x in range(1, 6):
        converted_player1.append(convert_to_deck_format(player_1[x]))
        converted_player2.append(convert_to_deck_format(player_2[x]))

    print(who_wins(converted_player1, converted_player2, player_1[0][:-1], player_2[0][:-1]))

    return None


if __name__ == "__main__":
    hands = load_file("20220224/hand.txt")

    for hand in hands:
        analyze_hand(hand)
