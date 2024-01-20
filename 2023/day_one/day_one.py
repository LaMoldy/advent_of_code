def get_file_content() -> list[str]:
    file = open("input.txt", "r")
    content = file.readlines()
    file.close()
    return content

def get_numbers_per_line(input: list[str]) -> list[str]:
    nums = []
    current_number = ""
    for lines in input:
        for char in lines:
            if char >= '0' and char <= '9':
                current_number += char
        nums.append(current_number)
        current_number = ""
    return nums

def seperate_numbers(numbers: list[str]) -> list[str]:
    result = []
    for number in numbers:
        if len(number) == 1:
            same_digit = f"{number}{number}"
            result.append(same_digit)
        elif len(number) == 2:
            result.append(number)
        elif len(number) > 2:
            digits = f"{number[0]}{number[len(number) - 1]}"
            result.append(digits)
    return result

def sum_numbers(numbers: list[str]) -> int:
    sum: int = 0
    for number in numbers:
        sum += int(number)
    return sum


def main() -> int:
    input = get_file_content()
    all_numbers = get_numbers_per_line(input)
    numbers = seperate_numbers(all_numbers)
    sum_of_numbers = sum_numbers(numbers)
    print(sum_of_numbers)
    return 0

main()
