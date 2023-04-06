# Increasing/decreasing sequence

def check_sequence(num):
    num_str = str(num)
    is_increasing = True
    is_decreasing = True
    while num > 0:
        num, digit = divmod(num, 10)
        next_digit = num % 10
        if next_digit >= digit and next_digit != 0:
            is_increasing = False
        if next_digit <= digit and next_digit != 0:
            is_decreasing = False
    return is_decreasing, is_increasing, num_str


def english_ui(is_decreasing, is_increasing, num_str):
    if is_increasing:
        msg = f"The digits of {num_str} is increasing sequence."
    elif is_decreasing:
        msg = f"The digits of {num_str} is decreasing sequence."
    else:
        msg = f"The digits of {num_str} don't form either increasing or decreasing sequence."
    return msg


def main():
    num = int(input("Enter your number: "))
    is_decreasing, is_increasing, num_str = check_sequence(num)
    print(english_ui(is_decreasing, is_increasing, num_str))

if __name__ == "__main__":
    main()
