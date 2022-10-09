#Project Flight game
import sys
from time import sleep
import mysql.connector
import random
from geopy import distance

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='game_project',
         user='root',
         password='MyN3wP4ssw0rd',                              #CHECK PASSWORD TO RUN THE PROGRAM!!!
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

#Function 1: for text effect
def text_effect(text):
    for char in text:
        sleep(0.00)
        sys.stdout.write(char)

#Function 2: check if the city exists in database

def check_city(city):
    sql = "SELECT count(*) from airport"
    sql += " WHERE municipality ='" + city + "'"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            row[0]
    return row[0]

#Function 3: search airports in the city

def municipality_search(city):
    sql = "SELECT ident, name FROM airport"
    sql += " WHERE municipality='" + city + "'"
    icao_list = []
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"ICAO code: {row[0]}, Airport name: {row[1]}")
            icao_list.append(row[0])
            print(icao_list)
    return icao_list


#Function 4: call the airport in the chosen city

def call_airport(icao):
    sql = "SELECT name FROM airport"
    sql += " WHERE ident='" + icao + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"You are now in {row[0]} and ready for your flight!")
    return row[0]

#Function 5: to measure the distance between the chosen airport to Rovaniemi airport

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


#Function 6: to call score affected by weather

def weather(correct_answer):
    if correct_answer == True:
        ran_nr = random.randint(1, 4)
    else:
        ran_nr = random.randint(5, 8)
    #print(ran_nr)
    cursor = connection.cursor()
    sql = "SELECT score, description from goal WHERE id= %s"
    ran = (ran_nr, )    # execute needs tuple to function properly
    cursor.execute(sql, ran)
    result = cursor.fetchall()
    for i in result:
        print(f"You caught: {i[1]}. That's why your C02 will change by {i[0]} units.")
        co2_score = int(i[0])
    return co2_score


#Function 7: check how far the play is to Rovaniemi

def calc_distance_to_Rov(position, distance):
    dis_to_Rov = round(distance - (distance/5 * position),2)
    return dis_to_Rov


##START THE GAME/MAIN PROGRAM

#PHASE1: Intro of the game & set a goal for players

intro1 = "Each year there are children from all over the world\nwho don't believe in Santa Claus.\nOnce a year they decide to fly to Rovaniemi\n (where Santa apparently lives) with only one goal in their mind - to pull Santa's beard."
text_effect(intro1)

intro2 = "On your way to Rovaniemi you will come across different challenges.\nOne of them being the Co2 consumption.\nThe budget you're given is 10 000.\nTry to keep it as low as possible. "
text_effect(intro2)
intro3 = "Do you believe in Santa Clause? "
while True:
    start = input(intro3)
    start = start.lower()
    if start == "no":
        print("Join us on a quest.")
        break
    elif start == "yes":
        print("It's going to be an eye-opening experience for you. Let's go!")
        break
    else:
        print("Just type yes or no.")


print("Lucky for you, there are other like-minded people out there.")

friends = input("Wanna meet them? ")
friends = friends.lower()

while friends != "yes" or friends != "no":
    if friends == "yes":
        print("I thought so. Your new friends care about our planet Earth. "
          "In order to have them join you on a quest\nthey will have questions ready for you.\n"
          "Answer them correctly and you won't fly alone, plus you will have a good chance to stay within the Co2 budget.\n")
        break
    elif friends == "no":
        print("If you don't care about meeting new friends, I hope that you care about planet Earth.\n"
          "On your trip you will come across different questions. Answer them correctly and you might save some Co2 and reach your destination within the budget.")
        break
    friends = input("Just type yes or no!")
    friends = friends.lower()

#User input name and city

player_name = input("Let us start with your name: ")

municipality = input("Which city do you want to fly from: ")

while check_city(municipality) == 0:
    municipality = input("Oops! We can't find neither your city nor its airport. Another city please: ")
else:
    municipality_search(municipality)


#Users choose the airport in the chosen city

icao_selection = input("Here are the closest airports. Pick one by entering ICAO code: ")
                                                                            
while icao_selection not in municipality_search(municipality):
    print("Oops! Check again the ICAO code. You can't arrive the wanted airport if you don't call ICAO code correctly")
    icao_selection = str(input("Enter ICAO code again: "))
else:
    airport_name = call_airport(icao_selection) #store airport name in a variable


#The distance between the chosen airport to Rovaniemi airport

a = airport_position(icao_selection)
b = airport_position("EFRO")
dist = distance.distance(a, b).km
print(f"Distance between {airport_name} and Rovaniemi Airport is {dist:.2f} km")


#PHASE 2: GAME START!

co2_budget = 10000
co2_consumed = 5000
destinations = 1

questions = list(questions)
answers = list(answers)

while co2_consumed < co2_budget and destinations <= 5:
        print(f"You're in destination {destinations} and your Co2 consumption score is {co2_consumed}")
        #ask question & get point by answer
        random_index_number = random.randint(0, len(questions)-1)
        user_answer = "0"
        while user_answer != "true" and user_answer != "false":
            print(questions[random_index_number])
            user_answer = input("True or false: ")
            user_answer = user_answer.lower()

        right_answer = answers[random_index_number]
        questions.pop(random_index_number)
        answers.pop(random_index_number)

        if user_answer == right_answer:
            print("Correct.")
            co2_consumed += weather(True)
        else:
            print("Wrong")
            co2_consumed += weather(False)

        print(f"Your current Co2 level is: {co2_consumed}\n")
        destinations += 1
        print(f"You are {calc_distance_to_Rov(destinations, dist)} km away from Rovaniemi. Yay!!!") #Inform how far from that destination to Rovaniemi
else:
    if co2_consumed >= co2_budget:
        print(f"Game over. You consumed {co2_consumed} Co2!")
    else:
        print(f"You consumed {co2_consumed} Co2 & you passed 5 destinations. WIN!")



#PROBLEM 1: Can't define who win the game, who lost the game --> DONE (Run more test to check further)
#PROBLEM 2: when player keep answer correctly c02 go to minus point. we don't want it go minus. it need to stay at least >0 so we have to do smt with it  --> DONE
#PROBLEM 3: How to call random question and avoid duplicate question again --> DONE
#PROBLEM 4: How to add call weather and add score from weather table to co2_consumed score --> DONE



