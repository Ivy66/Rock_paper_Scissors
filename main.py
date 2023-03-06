import random

choices = ["rock", "paper", "scissors"]


def generate_computer_choice():
    number = random.randint(1, 3)
    return number


def generate_player_choice():
    user_input = int(input("Please enter a number between 1 and 3: "))
    if user_input < 1 or user_input > 3:
        print("Please enter a number between 1 and 3")
        return None
    else:
        return user_input


def determine_winner():
    computer_number = generate_computer_choice()
    player_number = generate_player_choice()
    if player_number is None:
        return
    computer_choice = convert_choice(computer_number)
    player_choice = choices[player_number - 1]
    print("Computer chose:", computer_choice)
    print("Player chose:", player_choice)
    if computer_number == player_number:
        print("It's a draw")
    elif (computer_number == 1 and player_number == 2) or \
            (computer_number == 2 and player_number == 3) or \
            (computer_number == 3 and player_number == 1):
        print("Player wins!")
    else:
        print("Computer wins")


def convert_choice(number):
    return choices[number - 1]


def main():
    determine_winner()


main()
