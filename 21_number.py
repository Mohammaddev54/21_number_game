import os


def check_for_consecutive_number(number_list):
    i = 1
    while i < len(number_list):
        if (number_list[i] - number_list[i - 1]) != 1:
            return False
        i = i + 1
    return True


def check_for_last_number(number_list):
    # if number_list is empty
    if len(number_list) == 0:
        last_number = 0
        return last_number
    last_number = number_list[-1]
    return last_number


def game_description():
    print("Game description: ")
    print("21, Bagram, or Twenty plus one is a game which progresses")
    print("by counting up 1 to 21, with the player who calls (21) is")
    print("eliminated.\n")

# Not implemented completely
def game_help():
    print("game_help function called!")


def clean_terminal():
    os.system("cls")

# Number of rounds
def rounds(number_list):
    while True:
        try:
            number_of_rounds = int(input("How many numbers do you want to enter? (1, 2, 3): "))
        except ValueError as error:
            show_error(error, None, number_list)
            continue
        if number_of_rounds <= 0 or number_of_rounds > 3:
            message = "The lowest number you can enter is 1\n\tThe highest number you can enter is 3\n"
            show_error(None, message,  number_list)
            continue
        return number_of_rounds

# Finding the upper multiples of number 4
def upper_multiple_of_4(number_list):
    last_number = check_for_last_number(number_list)
    if last_number > 4 or last_number == 4:
        return last_number + (4 - (last_number % 4))
    return 4


def computer_choice_of_numbers(number_list):
    computer_numbers = []
    # Confirming if there is any numbers in number_list
    last_number = check_for_last_number(number_list)
    # Creating a list of numbers according to number_list
    for number in range(last_number + 1, upper_multiple_of_4(number_list) + 1):
        # If computer_numbers hass 3 numbers break loop
        if len(computer_numbers) == 3:
            break
        # if computer_numbers doesn't have 3 numbers run
        computer_numbers.append(1)
        number_list.append(number)
    # For loop finished
    clean_terminal()
    print("Computer: ")
    print(number_list)


def verify_user_input(user_input, ):
    if user_input == 21:
        #LOSING DUE TO user_input==21
        return False
    elif user_input <= 0 or user_input > 21:
        # LOSING DUE TO user_input<=0 or user_input>21
        return False
    return True


def user_input(number_list, round_number):
    while round_number > 0:
        try:
            number = int(input("Enter a number: ").strip())
        except ValueError as error:
            show_error(error, None, number_list)
            continue
        
        if verify_user_input(number) != True:
            lose()
            return "lose"

        number_list.append(number)

        if check_for_consecutive_number(number_list):
            round_number = round_number - 1
        else:
            lose(message="Entering an inconsecutive number!")
            return "lose"


def lose(message=None):
    if message is not None:
        print("\nYou lose!\n")
        print(f"Reason: {message}")
        print()
        return
    print("\nYou lose!\n")


def win():
    print("\nYou WIN!\n")


def show_error(error, message, number_list):
    clean_terminal()
    if error:
        print(f"ERROR: \n\t{error}")
    print(f"Message: \n\t {message}")
    if number_list != False:
        print(f"Numbers: \n\t {number_list}\n")


def computer_start():
    numbers_played = []
    clean_terminal()
    game_description()

    while True:
        if check_for_last_number(numbers_played) == 20:
            win()
            break

        computer_choice_of_numbers(numbers_played)
        number_of_rounds = rounds(numbers_played)
        if user_input(numbers_played, number_of_rounds) != "lose":
            continue
        break


def player_start():
    numbers_played = []
    clean_terminal()
    game_description()

    while True:
        number_of_rounds = rounds(numbers_played)
        if user_input(numbers_played,number_of_rounds) == "lose":
            break
        else:
            computer_choice_of_numbers(numbers_played)

# Question function only to be used for (Yes, No) answerable questions
def question(yes_no_question):
    while True:
        user_input = input(yes_no_question + " (Yes/No):  ").strip().lower()
        if user_input == "no":
            return False
        elif user_input == "yes":
            return True
        elif user_input == "help":
            game_help()
        else:
            show_error(None, "Invalid input please answer only with Yes or No!\n", False)
            continue


def start_game():
    clean_terminal()
    game_description()

    if question("Do you want to start first?"):
        player_start()
    else:
        computer_start()


def main():
    if question("Do you want to play 21 number game!?"):
        while True:
            start_game()
            if question("Do you want to restart?"):
                continue

            else:
                clean_terminal()
                print("Bye!")
                break


if __name__ == "__main__":
    main()
