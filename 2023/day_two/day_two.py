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

def get_largest_cube_amount_from_game(game: str, id: int) -> list[int]:
    largest_red = None
    largest_green = None
    largest_blue = None
    hands = seperate_hands(game, id)
    for hand in hands:
        hand_info = seperaate_color_and_number(hand)
        number = int(hand_info[0])
        color = hand_info[1]
        if color == "red":
            if largest_red is None:
                largest_red = number
            elif largest_red < number:
                largest_red = number
        elif color == "green":
            if largest_green is None:
                largest_green = number
            elif largest_green < number:
                largest_green = number
        else:
            if largest_blue is None:
                largest_blue = number
            elif largest_blue < number:
                largest_blue = number
    if largest_red is not None and largest_green is not None and largest_blue is not None:
        return [largest_red, largest_green, largest_blue]
    else:
        return [0, 0, 0]

def get_smallest_cube_amounts(games: list[str]) -> list[list[int]]:
    largest_games = []
    for game in games:
        id = get_game_id(game)
        largest_values = get_largest_cube_amount_from_game(game, id)
        largest_games.append(largest_values)
    return largest_games

def get_power_of_list(values: list[int]) -> int:
    return values[0] * values[1] * values[2]

def get_all_powers_of_games(numbers: list[list[int]]) -> list[int]:
    result = []
    for number in numbers:
        values = get_power_of_list(number)
        result.append(values)
    return result


def main() -> int:
    games = get_input()
    game_ids = get_valid_games(games)
    sum_of_ids = sum_list(game_ids)
    print(sum_of_ids)
    largest_amounts = get_smallest_cube_amounts(games)
    powers = get_all_powers_of_games(largest_amounts)
    sum_of_powers = sum_list(powers)
    print(sum_of_powers)
    return 0

main()
