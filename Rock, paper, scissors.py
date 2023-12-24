import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
choice = int(input("Enter your choice: 0 is Rock, 1 is Scissors, 2 is Paper:\n"))
if choice >= 3 or choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[choice])
    print("You chose: ")
    if choice == 0:
        print("Rock")
    elif choice == 1:
        print("Scissors")
    else:
        print("Paper")

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])
    if computer_choice == 0:
        print("Rock")
    elif computer_choice == 1:
        print("Scissors")
    else:
        print("Paper")

    if choice == computer_choice:
        print("It's a tie")
    elif choice == 0 and computer_choice == 1:
        print("You win")
    elif choice == 1 and computer_choice == 2:
        print("You win")
    elif choice == 2 and computer_choice == 0:
        print("You win")
    else:
        print("You lose")
