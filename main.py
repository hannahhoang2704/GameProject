#Project Flight game
import sys
from time import sleep

import mysql.connector
import random

from geopy import distance
import time,os,sys

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='game_project',
         user='root',
         password='!QAZ2wsx#EDC',
         autocommit=True
         )



#Questionaires and answers
questions = ("Wasting less food is a way to reduce greenhouse gas emissions.", # 0
             "The overwhelming majority of scientists agree that climate change is real and caused by humans.",  # 1
             "Combustion removes carbon from the atmosphere",  # 2
             "Unplugging your electronics when you’re not using them could shave as much as 10 percent off your energy"  
             "bill.",  # 3
             "Climate change is heating the world evenly.",  # 4
             "Climate change and extreme weather are linked.",  # 5
             "As climate warms, we will no longer have snow storms and cold days.",  # 6
             "We definitely know that tornadoes are increasing in frequency because of climate change.",  # 7
             "All climate scientists in the 1970s were saying that we were going into an Ice Age or cooler Earth.",  # 8
             "Growing leafy green plants is the most effective method for permanently storing carbon dioxide.",  # 9
             "Scientists have reached common agreement and have adopted consensus-driven global policies that monitor"
             "effective, safe, reliable long-term storage of carbon dioxide.",  # 10
             "The atmosphere is composed mainly of nitrogen and oxygen.",  # 11
             "Climate change is the same thing as global warming",  # 12
             "The Earth's has climate changed before",  # 13
             "Climate change can harm plants and animals",  # 14
             "The sun causes global warming")  # 15
answers = ("true",#0
           "true", #1,
           "false", #2
           "true", #3
           "false", #4
           "true", #5
           "false", #6
           "false", #7
           "false", #8
           "false", #9
           "false", #10
           "true",  #11
           "false", #12
           "true", #13
           "true", #14
           "false") #15

##ALL FUNCTIONS
#Function for underlying the text
class Format:
    end = '\033[0m'
    underline = '\033[4m'

#Functions for text effect

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


#Function 1: to search the city

def municipality_search(city):
    sql = "SELECT ident, name FROM airport"
    sql += " WHERE municipality='" + city + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()


    if cursor.rowcount > 0:
        for row in result:
            print(f"       ICAO code: {row[0]}, Airport name: {row[1]}")
    return


#Function 2: to call the airport in the chosen city

def call_airport(icao):
    sql = "SELECT name FROM airport"
    sql += " WHERE ident='" + icao + "'"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            typingPrint(f"{player_name}, you are now in {row[0]}.Get ready for your flight!\n")
    return row[0]

#Function 3: to measure the distance between the chosen airport to Rovaniemi airport

def airport_position(ICAO):
    sql = "SELECT name, latitude_deg, longitude_deg from airport"
    sql += " WHERE ident='" + ICAO + "'"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            #print(f"Airport name: {row[0]}")
            deg = (row[1], row[2])
            #print(deg)
    return deg


#Function 4: to call score affected by weather
def weather(correct_answer):
    if correct_answer == True:
        ran_nr = random.randint(1, 4)
    else:
        ran_nr = random.randint(5,8)
    #print(ran_nr)
    cursor = connection.cursor()
    sql = "SELECT score, description from goal WHERE id= %s"
    ran = (ran_nr, ) # execute needs tuple to function properly
    cursor.execute(sql, ran)
    result = cursor.fetchall()
    for i in result:
        print(f"{Format.underline + 'Weather forcast:' + Format.end} {i[1]}.\n")
        text_effect(f"That's why your Co2 will change by {i[0]} units.\n")
        co2_score = int(i[0])
    return co2_score



#Main program
#Phase1: Intro of the game & set a goal for players

intro1 = f"Each year children from all over the world\nfly to {Format.underline + 'Rovaniemi' + Format.end} to meet Santa.\nBelievers to hug him and non-believers to expose him by pulling his beard. \n"
text_effect(intro1)

intro2 = f"\nOn your way to Rovaniemi you will come across different challenges.\nOne of them is flight's high {Format.underline + 'Co2 consumption.' + Format.end}\n{Format.underline + 'Your main challenge is to keep Co2 consumption as low as possible.' + Format.end}\nMake sure it doesn't go over 10 000, otherwise it is GAME OVER.\n"
text_effect(intro2)
typingPrint("Your mission starts in 3..")
time.sleep(1)
typingPrint("2..")
time.sleep(1)
typingPrint("1..")
time.sleep(1)
clearScreen()
clearScreen()
intro3 = "First things first, do you believe in Santa Clause? "
while True:
    start = input(intro3)
    start = start.lower()
    if start == "no":
        text_effect("\nMe neither. Get ready for an adventure.")
        break
    elif start == "yes":
        text_effect("\n***It's going to be an eye-opening experience for you. Let's go!***\n")
        break
    else:
        print("Just type yes or no.")


text_effect("Lucky for you, there are other like-minded people out there. \n")

friends = input("Do you want to meet them? ")
friends = friends.lower()

while friends != "yes" or friends != "no":
    if friends == "yes":
        text_effect(f"\nI thought so.\nYour new friends care about our planet Earth.\nIn order to have them join you on your quest they will have {Format.underline + 'questions' + Format.end} for you.\n"
          f"Answer them correctly and you won't fly alone, plus you will have a good chance to stay within the Co2 budget.\n")
        break
    elif friends == "no":
        text_effect("\nIf you don't care about meeting new friends, I hope that you care about planet Earth.\n"
          f"On your trip you will come across different {Format.underline + 'questions.' + Format.end}\nAnswer correctly and you might save some {Format.underline + 'Co2' + Format.end} and reach your destination within the budget.\n")
        break
    friends = input("Just type yes or no!")
    friends = friends.lower()

typingPrint(f"{Format.underline + 'Your current Co2 consumption : 5000'+ Format.end}\n")
time.sleep(3)
clearScreen()


#User input name and city
player_name = input("Lets start with your name: ")

municipality = input("Where do you live: ")
print("\nHere are your adventure starting point options: ")


municipality_search(municipality)

#Users choose the airport in the chosen city
icao_selection = str(input("Which one do you pick? Enter ICAO:  "))
airport_name = call_airport(icao_selection) #store airport name in a variable


#Measure the distance between the chosen airport to Rovaniemi airport

a = airport_position(icao_selection)
b = airport_position("EFRO")
dist = distance.distance(a, b).km
print(f"\n{Format.underline + f'Distance between {airport_name} and Rovaniemi Airport is {dist:.2f}km.' + Format.end}\n")
typingPrint("Take-off in 3..")
time.sleep(1)
typingPrint("2..")
time.sleep(1)
typingPrint("1..")
time.sleep(1)
clearScreen()
clearScreen()




#Start the game

co2_budget = 10000
co2_consumed = 5000
destinations = 1

questions = list(questions)
answers = list(answers)

#used_index = []
while co2_consumed < co2_budget and destinations <= 5:
        time.sleep(3)
        text_effect(f"\nYou are approaching stop number: {destinations}. Get your thinking hat on and answer the question:\n")
        random_index_number = random.randint(0, len(questions)-1)
        user_answer = "0"
        while user_answer != "true" and user_answer != "false":
            print(questions[random_index_number])
            user_answer = input("True or false: ")
            time.sleep(3)
            user_answer = user_answer.lower()


        right_answer = answers[random_index_number]
        #used_index.append(questions[random_index_number])
        questions.pop(random_index_number)
        answers.pop(random_index_number)
        if user_answer == right_answer:
            print(f"Good job! That was the {Format.underline + 'correct' + Format.end} answer.")
            text_effect(f"{player_name} look ahead, it looks like the weather is in your favor.\n")
            co2_consumed += weather(True)
            text_effect(f"{Format.underline + 'Your current Co2 level is:' + Format.end} {co2_consumed} units\n")



        else:
            print(f"You answered {Format.underline + 'incorrectly.' + Format.end}")
            text_effect(f"{player_name} not only you didn't answer correctly but now it seems that the weather has changed.\n")
            co2_consumed += weather(False)
            text_effect(f"{Format.underline + 'Your current Co2 level is:' + Format.end} {co2_consumed} units\n")


        destinations += 1
else:
    if co2_consumed >= co2_budget:
        text_effect(f"Oh, no! Your Co2 consumption level was {co2_consumed} units. This exceeds your budget. Game over! Try again soon - Santa won't wait forever.")
    else:
        text_effect(f"Congratulations, your flight is about to land with {co2_consumed} Co2 units consumed. You passed all the challenges and now Santa awaits.")







