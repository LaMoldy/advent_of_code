import re

def get_input() -> list[str]:
    file = open("input.txt", "r")
    content = file.readlines()
    file.close()
    return content

def sum_list(game_ids: list[int]) -> int:
    return sum(game_ids)

def get_game_id(game: str) -> int:
    game_elements = game.split(" ")
    game_id = game_elements[1]
    game_id = game_id[0:-1]
    return int(game_id)

def get_valid_games(games: list[str]) -> list[int]:
    valid_game_ids = []
    for game in games:
        id = get_game_id(game)
        if (is_game_legal(game, id)):
            valid_game_ids.append(id)
    return valid_game_ids

def seperate_hands(game: str, id: int) -> list[str]:
    game = game.replace("\n", "")
    prefix = 7 + len(str(id))
    hands = re.split("; |, ", game[prefix:])
    return hands

def seperaate_color_and_number(hand: str) -> list[str]:
    return hand.split(" ")

def is_game_legal(game: str, id: int) -> bool:
    MAX_VALUES = (12, 13, 14)
    hands = seperate_hands(game, id)
    for hand in hands:
        hand_info = seperaate_color_and_number(hand)
        number = int(hand_info[0])
        color = hand_info[1]
        if color == "red" and number > MAX_VALUES[0]:
            return False
        elif color == "green" and number > MAX_VALUES[1]:
            return False
        elif color == "blue" and number > MAX_VALUES[2]:
            return False
        else:
            continue
    return True

def main() -> int:
    games = get_input()
    game_ids = get_valid_games(games)
    sum_of_ids = sum_list(game_ids)
    print(sum_of_ids)
    return 0

main()
