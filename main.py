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
    password='!QAZ2wsx#EDC',  # MyN3wP4ssw0rd ##CHECK PASSWORD TO RUN THE PROGRAM!!!
    autocommit=True
)

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
#imports colors
class bcolors:
    GREEN = '\033[92m'
    RESET = '\033[0m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'

T = "Game over"
W = "HO HO HO"
ASCII_art_1 = pyfiglet.figlet_format(W)
print(bcolors.BLUE + ASCII_art_1 + bcolors.RESET)

##ALL FUNCTIONS
# Function for underlying the text
class Format:
    end = '\033[0m'
    underline = '\033[4m'


# Function 1: for text effect
def text_effect(text):
    for char in text:
        sleep(0.05)
        sys.stdout.write(char)


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)


def clearScreen():
    os.system("clear")


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
    #icao_list = []
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
            typingPrint(f"{player_name}, you are now in {row[0]}.Get ready for your flight!\n")
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
        print(
            f"{Format.underline + 'Weather forecast:' + Format.end} {i[1]}.\n")
        text_effect(f"That's why your Co2 will change by {i[0]} units.\n")
        co2_score = int(i[0])
    return co2_score


# Function 7: check how far the play is to Rovaniemi

def calc_distance_to_Rov(position, distance):
    dis_to_Rov = round(distance - (distance / 5 * position), 2)
    return dis_to_Rov


##START THE GAME/MAIN PROGRAM

# PHASE1: Intro of the game & set a goal for players

intro1 = f"Each year children from all over the world\nfly to {Format.underline + 'Rovaniemi' + Format.end} to meet {bcolors.BLUE + 'Santa' + bcolors.RESET}.\nBelievers to hug him and non-believers to expose him by pulling his beard. \n"
text_effect(intro1)

intro2 = f"\nOn your way to Rovaniemi you will come across different challenges.\nOne of them is flight's {Format.underline + 'Co2 consumption.' + Format.end}\nYour main goal is to {Format.underline + 'keep Co2 consumption as low as possible.' + Format.end}\nMake sure it doesn't go over 10 000 units!\n"
text_effect(intro2)

typingPrint("Your mission starts in 3..\n")
print(bcolors.YELLOW +"""                             ______
                            _\ _~-\___
                   =  = ==(____AA____D
                               \_____\___________________,-~~~~~~~`-.._
                               /     o O o o o o O O o o o o o o O o  |\_
                               `~-.__        ___..----..                  )
                                     `---~~\___________/------------`````
                                     =  ===(_________D
""" + bcolors.RESET)
time.sleep(1)
typingPrint("2..\n")
print(bcolors.YELLOW +"""                                                                  ______
                                                                  _\ _~-\___
                                                          =  = ==(____AA____D
                                                                      \_____\___________________,-~~~~~~~`-.._
                                                                      /     o O o o o o O O o o o o o o O o  |\_
                                                                     `~-.__        ___..----..                  )
                                                                           `---~~\___________/------------`````
                                                                             =  ===(_________D
""" + bcolors.RESET)

time.sleep(1)
typingPrint("1..\n")
print(bcolors.YELLOW +"""                                                                                                           ______
                                                                                                          _\ _~-\___
                                                                                                  =  = ==(____AA____D
                                                                                                                \_____\___________________,-~~~~~~~`-.._
                                                                                                              /     o O o o o o O O o o o o o o O o  |\_
                                                                                                               `~-.__        ___..----..                  )
                                                                                                                  `---~~\___________/------------`````
                                                                                                                   =  ===(_________D
""" + bcolors.RESET)
time.sleep(1)
clearScreen()
clearScreen()
intro3 = (bcolors.GREEN + 'Firstly, do you believe in Santa Claus? '  + bcolors.RESET)

while True:
    start = input(intro3)
    start = start.lower()
    if start == "no":
        text_effect("\nMe neither. Get ready for an adventure.\n")
        break
    elif start == "yes":
        text_effect(
            "\n***It's going to be an eye-opening experience for you. Let's go!***\n")
        break
    else:
        print("Just type yes or no. ")




text_effect("Lucky for you, there are other like-minded people out there. \n")

friends = input(bcolors.GREEN + "Do you want to meet them? " + bcolors.RESET)
friends = friends.lower()

while friends != "yes" or friends != "no":
    if friends == "yes":
        text_effect(
            f"\nI thought so.\nIn order to have them join you on your quest they will have {Format.underline + 'questions' + Format.end} for you.\n"
            f"Answer them correctly and you will save some C02!\n")
        break
    elif friends == "no":
        text_effect(
            "\nIf you don't care about meeting new friends, try to save some C02 during your flight\nby answering "
            f"{Format.underline + 'questions' + Format.end} correctly and {Format.underline + 'keep Co2 within the budget.' + Format.end}\n")
        break
    friends = input("Just type yes or no!")
    friends = friends.lower()

typingPrint(f"'Before reaching the 1st destination, your C02 is {Format.underline + '5000 units.' + Format.end}\n")
time.sleep(3)
clearScreen()

# User input name and city

player_name = input(bcolors.GREEN + 'Lets start with your name: ' + bcolors.RESET)
player_name = player_name.capitalize()


municipality = input(bcolors.GREEN + 'From which city you want to start your journey:' + bcolors.RESET)

while municipality.lower() == "rovaniemi":                      #Player can't choose Rovaniemi as a starting point
    municipality = input("Oops! You can't fly from this city. Another city please: ")
    while check_city(municipality) == 0:
        municipality = input("Oops! You can't fly from this city. Another city please: ")

else:
    print("\nHere are your adventure starting point options: ")
    municipality_search(municipality)

# Users choose the airport in the chosen city

icao_selection = input(f"You can see all the airports in your city above.\n{(bcolors.GREEN + 'Enter ICAO to choose the airport you want to fly: ' + bcolors.RESET)}  ")

while icao_selection.upper() not in icao_list:
    print("Oops! Check again the ICAO code. You can't arrive to the airport if you don't call ICAO code correctly!")
    icao_selection = str(input(bcolors.GREEN + 'Enter ICAO code again:'  + bcolors.RESET))
else:
    location = icao_selection.upper() # store value of icao
    airport_name = call_airport(icao_selection)  # store airport name in a variable

# The distance between the chosen airport to Rovaniemi airport

a = airport_position(icao_selection)
b = airport_position("EFRO")
dist = distance.distance(a, b).km
print(
    f"\n{Format.underline + f'Distance between {airport_name} and Rovaniemi Airport is {dist:.2f}km.' + Format.end}\n")

time.sleep(3)
clearScreen()
clearScreen()
#typingPrint("Take-off in 3..\n")

print("""Take-off in 3..\n
      \         /   \         /   \         /   \         /
      _\/     \/_   _\/     \/_   _\/     \/_   _\/     \/_
       _\-'"'-/_     _\-'"'-/_     _\-'"'-/_     _\-'"'-/_
      (_,     ,_)   (_,     ,_)   (_,     ,_)   (_,     ,_)
        | ^ ^ |       | o o |       | a a |       | 6 6 |
        |     |       |     |       |     |       |     |
        |     |       |     |       |     |       |     |
        |  Y  |       |  @  |       |  O  |       |  V  |
        `._|_.'       `._|_.'       `._|_.'       `._|_.'""")

time.sleep(2)
clearScreen()
clearScreen()
#typingPrint("")
print("""2..\n
                     \         /   \         /  
                     _\/     \/_   _\/     \/_   
                      _\-'"'-/_     _\-'"'-/_     
                     (_,     ,_)   (_,     ,_)     
                       | q p |       | @ @ |           
                       |     |       |     |          
                       |     |       |     |          
                       | \_/ |       |  V  |     
                       `._|_.'       `._|_.'            """)

time.sleep(2)
clearScreen()
clearScreen()
#yestypingPrint("")
print("""1..\n
                           \         /
                           _\/     \/_
                            _\-'"'-/_
                           (_,     ,_)
                             | e e |
                             |     |
                        '-.  |  _  |  .-'
                       --=   |((@))|   =--
                        .-'  `._|_.'  '-.

""")
time.sleep(2)
clearScreen()
clearScreen()


# PHASE 2: GAME START!

co2_budget = 10000
co2_consumed = 5000
destinations = 1

questions = list(questions)
answers = list(answers)

while co2_consumed < co2_budget and destinations <= 5:
    time.sleep(0.5)
    text_effect(
        f"You are approaching destination {destinations}. {(bcolors.GREEN + 'Answer the question: ' + bcolors.RESET)}\n")
    # ask question & get point by answer
    random_index_number = random.randint(0, len(questions) - 1)
    user_answer = "0"
    while user_answer != "true" and user_answer != "false":
        print(questions[
                  random_index_number])  # call random question in questions list
        user_answer = input(bcolors.GREEN + 'True or false: ' + bcolors.RESET)
        time.sleep(2)
        user_answer = user_answer.lower()

    right_answer = answers[random_index_number]
    questions.pop(
        random_index_number)  # pop the question from the list to avoid duplicated question in next destination
    answers.pop(random_index_number)

    # Check if players answer correct or not

    if user_answer == right_answer:
        print(
            f"{(bcolors.BLUE + 'Good job!' + bcolors.RESET)} That was the {Format.underline + 'correct' + Format.end} answer.")
        text_effect(
            f"{player_name}, look ahead, it looks like the weather is in your favor.\n")
        co2_consumed += weather(True)

    elif user_answer != right_answer:
        print(f"You answered {bcolors.RED + 'incorrectly' + bcolors.RESET}")
        text_effect(
            f"{player_name}, not only you didn't answer correctly but also the weather has changed.\n")
        co2_consumed += weather(False)

    text_effect(
        f"{Format.underline + 'Your current Co2 is:' + Format.end} {co2_consumed} units\n")  # inform players their co2 score
    print(
        f"You are {calc_distance_to_Rov(destinations, dist)} km away from Rovaniemi.")  # Inform players how far from that destination to Rovaniemi

    destinations += 1

else:
    # Check if players win or lost the game
    if co2_consumed >= co2_budget:
        text_effect(f"Oh, no! Your Co2 consumption level was {co2_consumed} units. This exceeds your budget.\nTry again soon - Santa won't wait forever.\n")
        T = "GAME OVER"
        ASCII_art_1 = pyfiglet.figlet_format(T)
        print(bcolors.RED + ASCII_art_1 + bcolors.RESET)
    else:
        text_effect(
            f"Congratulations!\nYour flight is about to land with {co2_consumed} Co2 units consumed. You passed all the challenges and now Santa awaits.\n")
        C = "YOU WON!"
        ASCII_art_1 = pyfiglet.figlet_format(C)
        print(bcolors.BLUE + ASCII_art_1 + bcolors.RESET)


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

#Check the best-recording score

def record_check():
    sql = "select screen_name, co2_consumed from game order by co2_consumed limit 5"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(f"Player's name: {row[0]}, Score: {row[1]}")
    return

ask_recording = input(f"\n{bcolors.GREEN + 'Do you want to check top 5 best record (yes/no): ' + bcolors.RESET}")
ask_recording.lower()

if ask_recording == "yes":
    record_check()
else:
    print("See you again!")
