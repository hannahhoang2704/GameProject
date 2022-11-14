import random


def rock_paper_scissors():
    def game_replay():
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

        player_score = 0
        comp_score = 0
        round = 1

        while round <= 3:
            print(f"Round number : {round}/3.")
            option = [rock, paper, scissors]
            user_choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
            print(option[user_choice])


            computer_choice = random.randint(0, len(option) - 1)
            print(option[computer_choice])


            if user_choice < computer_choice:
                if user_choice == 0 and computer_choice == 2:
                    player_score += 1
                    print(f"You: {player_score} | Comp: {comp_score} ")
                else:
                    comp_score += 1
                    print(f"You: {player_score} | Comp: {comp_score} ")
            elif user_choice > computer_choice:
                if user_choice == 2 and computer_choice == 0:
                    comp_score += 1
                    print(f"You: {player_score} | Comp: {comp_score} ")
                else:
                    player_score += 1
                    print(f"You: {player_score} | Comp: {comp_score} ")
            else:
                print(f"You: {player_score} | Comp: {comp_score} ")

            round += 1


        if player_score < comp_score:
            print("You lost the game. Computer won the game with score: ", comp_score)
        elif player_score == comp_score:
            print("Game is tie. Play again!")
            new_game = input("Do you want to restart the game: y/n")
            print(new_game)
            if new_game == "y":
                game_replay()
            else:
                print("Sorry to see you go")
        else:
            print("You won the game with score: ", player_score)
    game_replay()

rock_paper_scissors()
