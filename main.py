import random


def main():
    print("Welcome to the Rock Paper Scissor")
    rock_ascii = """
        ____   
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
"""
    paper_ascii = """
      _______
 ---'   ____)____
           ______)
          _______)
         _______)
---.__________)
"""
    scissors_ascii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
    confirm = input("press enter to continue or type (help) for rules").lower()

    if confirm == "help":
        print("""
              *************Rules************
              1:- you choose and the computer choices
              2:- Rock smashes Scissors -> Rock wins
              3:- Scissors cut Paper -> Scissors wins
              4:- Paper covers Rock -> Paper wins
              """)

    user_choice = input("enter your choice [Rock, Paper, Scissors]").lower()

    if user_choice not in ["rock", "scissors", "paper"]:
        print("Invalid choice please run the program again and choice rock, paper or scissors")
    else:
        if user_choice == "rock":
            print(f"\n you choose :\n {rock_ascii}")
        elif user_choice == "paper":
            print(f"\nyou choose :\n{paper_ascii}")
        else:
            print(f"\nyou choose:\n{scissors_ascii}")

    computer_choice = random.choice(["rock", "paper", "scissors"])

    if computer_choice == "rock":
        print(f"\ncomputer choose :\n {rock_ascii}")
    elif computer_choice == "paper":
        print(f"\ncomputer choose :\n{paper_ascii}")
    else:
        print(f"\ncomputer choose:\n{scissors_ascii}")

    if user_choice == computer_choice:
        print("it's a tie")
    elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or
            (user_choice == "paper" and computer_choice == "rock")
            or
            (user_choice == "scissors" and computer_choice == "paper")
    ):

        print(f"you wins! {user_choice} beats {computer_choice}")
    else:
        print(f"you lose! {computer_choice} beats {user_choice}")


if __name__ == '__main__':
    main()
