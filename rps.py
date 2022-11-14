import random

def rock_paper_scissors():
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

    round = 0
    while round <3:
        round +=1

        option = [rock, paper, scissors]
        user_choice= int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
        print(option[user_choice])

        computer_choice = random.randint(0, len(option) -1)
        print(option[computer_choice])
        print(f"This was the round number {round}/3 and ", end ="")

        if user_choice < computer_choice:
          if user_choice == 0 and computer_choice == 2:
            print("you win")
          else:
            print("you lost")
        elif user_choice > computer_choice:
          if user_choice == 2 and computer_choice == 0:
            print("you lost")
          else:
            print("you win")
        else:
          print("it's a draw!")


rock_paper_scissors()
