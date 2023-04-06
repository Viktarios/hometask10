# The palindrome

def check_palindrome(number):
    temp_number = number
    reverse_number = 0

    while number > 0:
        digit = number % 10
        reverse_number = reverse_number * 10 + digit
        number = number // 10

    if temp_number == reverse_number:
        msg = "Palindrome"
    else:
        msg = "Not a Palindrome"

    return msg


def main():
    number = int(input("Enter your number: "))
    msg = f"Result is: {check_palindrome(number)}."
    print(msg)


if __name__ == "__main__":
    main()
