# QA2022 Sadovskaya Viktoriya
# Bank deposit

def count_deposit_summ(percent, initial_deposit):
    summ = initial_deposit
    months = 0

    while summ < 2 * initial_deposit:
        summ += summ * percent / 100
        months += 1

    return months, summ


def english_ui(months, summ):
    return f"After {months} months the sum of the bank deposit will double and be {round(summ)} byn."


def main():
    initial_deposit = int(input("Enter your deposit: "))
    percent = int(input("Enter percent: "))
    months, summ = count_deposit_summ(percent, initial_deposit)
    print(english_ui(months, summ))


if __name__ == "__main__":
    main()
