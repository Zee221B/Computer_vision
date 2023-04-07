import random

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])



def get_winner(computer_choice, user_choice):
    if computer_choice == "Rock":
        if user_choice == "Rock":
            print(f"You chose: {user_choice}")
            print("It's a tie!")
        elif user_choice == "Paper":
            print(f"You chose: {user_choice}")
            print("Congratulations, you won!")
        else:
            print(f"You chose: {user_choice}")
            print("Oh no! You lost!")
    if computer_choice == "Paper":
        if user_choice == "Rock":
            print(f"You chose: {user_choice}")
            print("Oh no! You lost!")
        elif user_choice == "Paper":
            print(f"You chose: {user_choice}")
            print("It's a tie!")
        else:
            print(f"You chose: {user_choice}")
            print("Congratulations, you won!")
    if computer_choice == "Scissors":
        if user_choice == "Rock":
            print(f"You chose: {user_choice}")
            print("Congratulations, you won!")
        elif user_choice == "Paper":
            print(f"You chose: {user_choice}")
            print("Oh no! You lost!")
        else:
            print(f"You chose: {user_choice}")
            print("It's a tie!")


def get_user_choice():
    while True:
        user_choice = input("Choose either Rock, Paper or Scissors: ").lower()
        return (f" You chose: {user_choice}")
    
        
print (get_user_choice())

def play(get_winner, get_user_choice, get_computer_choice):
     computer_choice = get_computer_choice()
     user_choice = get_user_choice()
     winner = get_winner(computer_choice, user_choice)
     print(winner)
     

print (play(get_winner, get_user_choice, get_computer_choice))