from time import sleep
import mysql.connector
import random
from geopy import distance
import time, os, sys
import pyfiglet

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='game_project',
    user='root',
    password='!QAZ2wsx#EDC',  # !QAZ2wsx#EDC or MyN3wP4ssw0rd ##CHECK PASSWORD TO RUN THE PROGRAM!!!
    autocommit=True
)

replay_option = ""


def game_replay():
    # Questionaires and answers
    questions = (
        "Wasting less food is a way to reduce greenhouse gas emissions.",  # 0
        "The overwhelming majority of scientists agree that climate change is real and caused by humans.",
        # 1
        "Combustion removes carbon from the atmosphere",  # 2
        "Unplugging your electronics when you’re not using them could shave as much as 10 percent off your energy"
        "bill.",  # 3
        "Climate change is heating the world evenly.",  # 4
        "Climate change and extreme weather are linked.",  # 5
        "As climate warms, we will no longer have snow storms and cold days.",  # 6
        "We definitely know that tornadoes are increasing in frequency because of climate change.",
        # 7
        "All climate scientists in the 1970s were saying that we were going into an Ice Age or cooler Earth.",
        # 8
        "Growing leafy green plants is the most effective method for permanently storing carbon dioxide.",
        # 9
        "Scientists have reached common agreement and have adopted consensus-driven global policies that monitor"
        "effective, safe, reliable long-term storage of carbon dioxide.",  # 10
        "The atmosphere is composed mainly of nitrogen and oxygen.",  # 11
        "Climate change is the same thing as global warming",  # 12
        "The Earth's climate has changed before",  # 13
        "Climate change can harm plants and animals",  # 14
        "The sun causes global warming")  # 15
    answers = ("true",  # 0
               "true",  # 1,
               "false",  # 2
               "true",  # 3
               "false",  # 4
               "true",  # 5
               "false",  # 6
               "false",  # 7
               "false",  # 8
               "false",  # 9
               "false",  # 10
               "true",  # 11
               "false",  # 12
               "true",  # 13
               "true",  # 14
               "false")  # 15

    # Function 2: check if the city exists in database

    def check_city(city):
        sql = "SELECT count(*) from airport"
        sql += " WHERE municipality ='" + city + "'"
        # print(sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in result:
                row[0]
        return row[0]

    # Function 3: search airports in the city

    icao_list = []

    def municipality_search(city):
        sql = "SELECT ident, name FROM airport"
        sql += " WHERE municipality='" + city + "'"
        # icao_list = []
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in result:
                print(f"     ICAO code: {row[0]}, Airport name: {row[1]}")
                icao_list.append(row[0])
        return icao_list

    # Function 4: call the airport in the chosen city

    def call_airport(icao):
        sql = "SELECT name FROM airport"
        sql += " WHERE ident='" + icao + "'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in result:
                print(f"\n{player_name}, you are now in {row[0]}. Get ready for your flight!\n")
        return row[0]

    # Function 5: to measure the distance between the chosen airport to Rovaniemi airport

    def airport_position(ICAO):
        sql = "SELECT name, latitude_deg, longitude_deg from airport"
        sql += " WHERE ident='" + ICAO + "'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in result:
                deg = (row[1], row[2])
        return deg

    # Function 6: to call score affected by weather

    def weather(correct_answer):
        if correct_answer == True:
            ran_nr = random.randint(1, 4)
        else:
            ran_nr = random.randint(5, 8)
        # print(ran_nr)
        cursor = connection.cursor()
        sql = "SELECT score, description from goal WHERE id= %s"
        ran = (ran_nr,)  # execute needs tuple to function properly
        cursor.execute(sql, ran)
        result = cursor.fetchall()
        for i in result:
            print(f"Weather forecast: + {i[1]}.")
            print(f"That's why your CO2 will change by {i[0]} units.\n")
            co2_score = int(i[0])
        return co2_score

    # Function 7: check how far the play is to Rovaniemi

    def calc_distance_to_Rov(position, distance):
        dis_to_Rov = round(distance - (distance / 5 * position), 2)
        return dis_to_Rov

    def introduction():
        print("Ho Ho Ho")

        # PHASE1: Intro of the game & set a goal for players

        intro1 = f"Each year children from all over the world\nfly to Rovaniemi to meet Santa\nBelievers to hug him and non-believers to expose him by pulling his beard. \n"
        print(intro1)

        intro2 = f"\nOn your way to Rovaniemi you will come across different challenges.\nOne of them is flight's CO2 consumption.\nYour main goal is to keep CO2 consumption as low as possible.\nMake sure it doesn't go over 10 000 units!\n"
        print(intro2)
        print("Your mission starts in 3..\n")
        print("2")
        print("1")

        intro3 = ("Firstly, do you believe in Santa Claus?")

        while True:
            start = input(intro3)
            start = start.lower()
            if start == "no":
                print("\n***Me neither. Get ready for an adventure.***\n")
                break
            elif start == "yes":
                print(
                    "\n***It's going to be an eye-opening experience for you. Let's go!***\n")
                break
            else:
                print("Just type yes or no. ")

        print("Lucky for you, there are other like-minded people out there. \n")

        friends = input("\nDo you want to meet them? ")
        friends = friends.lower()

        while friends != "yes" or friends != "no":
            if friends == "yes":
                print(
                    f"\nI thought so.\nIn order to have them join you on your quest they will have questions for you.\n"
                    f"Answer them correctly and you will save some C02!\n")
                break
            elif friends == "no":
                print(
                    "\nIf you don't care about meeting new friends, try to save some C02 during your flight\nby answering "
                    f"questions correctly and keep CO2 within the budget.\n")
                break
            friends = input("Just type yes or no! ")
            friends = friends.lower()

        print(
            f"Before reaching the 1st destination, your C02 is 5000 units.\n")

    ##START THE GAME
    if replay_option.lower() != "y":
        introduction()

    # User input name and city

    player_name = input("Let's start with your name: ")
    player_name = player_name.capitalize()

    municipality = input('From which city you want to start your journey: ')

    while check_city(
            municipality) == 0 or municipality.lower() == "rovaniemi":  # Player can't choose Rovaniemi as a starting point
        municipality = input("Oops! You can't fly from this city. Another city please: ")
    else:
        print("\nHere are your adventure starting point options: ")
        municipality_search(municipality)

    # Users choose the airport in the chosen city

    icao_selection = input(
        f"You can see all the airports in your city above.\n(Enter ICAO to choose the airport you want to fly:)")

    while icao_selection.upper() not in icao_list:
        print("Oops! Check again the ICAO code. You can't arrive to the airport if you don't call ICAO code correctly!")
        icao_selection = str(input("Enter ICAO code again:")
    else:
        location = icao_selection.upper()  # store value of icao
        airport_name = call_airport(icao_selection)  # store airport name in a variable

    # The distance between the chosen airport to Rovaniemi airport

    a = airport_position(icao_selection)
    b = airport_position("EFRO")
    dist = distance.distance(a, b).km
    print(
        f"'Distance between {airport_name} and Rovaniemi Airport is {dist:.2f}km.'\n")

    print("Take-off in 3...2...1")

    # PHASE 2: GAME START!

    co2_budget = 10000
    co2_consumed = 5000
    destinations = 1

    questions = list(questions)
    answers = list(answers)

    while co2_consumed < co2_budget and destinations <= 5:
        time.sleep(0.5)
        print(f"You are approaching destination {destinations}. Answer the question:\n")
        # ask question & get point by answer
        random_index_number = random.randint(0, len(questions) - 1)
        user_answer = "0"
        while user_answer != "true" and user_answer != "false":
            print(questions[
                      random_index_number])  # call random question in questions list
            user_answer = input('True or false: ')
            user_answer = user_answer.lower()

        right_answer = answers[random_index_number]
        questions.pop(
            random_index_number)  # pop the question from the list to avoid duplicated question in next destination
        answers.pop(random_index_number)

        # Check if players answer correct or not

        if user_answer == right_answer:
            print(f"Good job! That was the correct answer.")
            print(
                f"{player_name}, look ahead, it looks like the weather is in your favor.\n")
            co2_consumed += weather(True)

        elif user_answer != right_answer:
            print(f"You answered incorrectly")
            print(
                f"{player_name}, not only you didn't answer correctly but also the weather has changed.\n")
            co2_consumed += weather(False)

        print(f"Your current CO2 is: {co2_consumed} units\n")  # inform players their co2 score
        print(
            f"\nYou are {calc_distance_to_Rov(destinations, dist)} km away from Rovaniemi.\n")  # Inform players how far from that destination to Rovaniemi

        destinations += 1

    else:
        # Check if players win or lost the game
        if co2_consumed >= co2_budget:
            print(
                f"Oh, no! Your CO2 consumption level was {co2_consumed} units. This exceeds your budget.\nTry again soon - Santa won't wait forever.\n")
            print("Game Over")
        else:
            print(
                f"Congratulations!\nYour flight is about to land with {co2_consumed} CO2 units consumed. You passed all the challenges and now Santa awaits.\n")
            print("You won.")

    # Store the player score in the database

    def record_score(co2_consumed, co2_budget, location, screen_name):
        sql = "insert into game(co2_consumed, co2_budget, location, screen_name) values(" \
              + str(co2_consumed) + "," + str(co2_budget) + ", '" + str(
            location) + "', '" + str(screen_name) + "')"
        # print(sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        # if cursor.rowcount == 1:              # Confirm the score and record it in system
        # print("Data is inserted")

    record_score(co2_consumed, co2_budget, location, player_name)

    # Check the best-recording score

    def record_check():
        sql = "select screen_name, co2_consumed from game order by co2_consumed limit 5"
        # print(sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        order = 0  # give the order 1-5
        for row in result:
            order += 1
            print(f"{order}. Player: {row[0]}, Score: {row[1]}")
        return

    ask_recording = input(f"\nDo you want to check top 5 best record (yes/no): ")
    ask_recording.lower()

    if ask_recording == "yes":
        record_check()


# Ask players to replay the game
game_replay()

replay_option = input("Do you want to restart the game? (y/n): ")

if replay_option.lower() == "y":
    game_replay()
else:
    print("See you next time!")
