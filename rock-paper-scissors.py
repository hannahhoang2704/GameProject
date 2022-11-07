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
option = [rock, paper, scissors]
user_choice= int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
print(option[user_choice])

computer_choice = random.randint(0, len(option) -1)
print(option[computer_choice])

if user_choice < computer_choice:
  if user_choice == 0 and computer_choice == 2:
    print("You win")
  else:
    print("You lost")
elif user_choice > computer_choice:
  if user_choice == 2 and computer_choice == 0:
    print("You lost")
  else:
    print("You win")
else:
  print("Draw!")
