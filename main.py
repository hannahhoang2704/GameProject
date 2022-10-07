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
         password='MyN3wP4ssw0rd',
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

#Functions for text effect
def text_effect(text):
    for char in text:
        sleep(0.05)
        sys.stdout.write(char)


#Function 1: to search the city

def municipality_search(city):
    sql = "SELECT ident, name FROM airport"
    sql += " WHERE municipality='" + city + "'"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"ICAO code: {row[0]}, Airport name: {row[1]}")
    return


#Function 2: to call the airport in the chosen city

def call_airport(icao):                                                                                 #NEED TO CHECKED!!!!!!
    sql = "SELECT name FROM airport"
    sql += " WHERE ident='" + icao + "'"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"You are now in {row[0]} and ready for your flight!")
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


#Function 4: to call score affected by weather                                                     #NEED TO CHECKED!!!!!!

def weather(score):
    score = random.randint(4, 8)
    sql = "SELECT score, description from goal WHERE id= score"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"You caught this type of weather: {row[1]}. That's why your C02 will added: {row[0]}")
            #co2_score = row[0]
    return #co2_score

#Main program
#Phase1: Intro of the game & set a goal for players

"""intro1 = "Each year there are children from all over the world\nwho don't believe in Santa Claus.\nOnce a year they decide to fly to Rovaniemi\n (where Santa apparently lives) with only one goal in their mind - to pull Santa's beard."
text_effect(intro1)

intro2 = "On your way to Rovaniemi you will come across different challenges.\nOne of them being the Co2 consumption.\nThe budget you're given is 10 000.\nTry to keep it as low as possible. "
text_effect(intro2)
intro3 = "Do you believe in Santa Clause? "
start = input(intro3)
start = start.lower()

if start == "no":
    print("Join us on a quest.")
elif start == "yes":
    print("It's going to be an eye-opening experience for you. Let's go!")
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

municipality = str(input("Where do you live: "))

municipality_search(municipality)

#Users choose the airport in the chosen city
icao_selection = str(input("Here are the closest airports. Pick one by entering ICAO code: "))
call_airport(icao_selection)


#Measure the distance between the chosen airport to Rovaniemi airport

a = airport_position(icao_selection)
b = airport_position("EFRO")
dist = distance.distance(a, b).km
print(f"Distance between {call_airport(icao_selection)} and Rovaniemi Airport is {dist:.2f} km")

"""
#Start the game

co2_budget = 10000
co2_consumed = 5000
destinations = 5

used_index = []      #Store the used questions' indexes to avoid duplicate questions

while co2_consumed < co2_budget and destinations > 0:
        #ask question & get point by answer
        random_index_number = random.randint(0, len(questions) - 1)
        print(questions[random_index_number])
        user_answer = str(input("Give answer: "))
        right_answer = answers[random_index_number]
        if user_answer == right_answer:
            print("correct.")
            co2_consumed -= 2000
            print(co2_consumed)
        # weather(random_weather1)
        else:
            print("Wrong")
            co2_consumed += 2500
            print(co2_consumed)
        destinations -= 1
else:
    if co2_consumed > co2_budget:
        print("co2_consumed > co2_budget")
    else:
        print(f"{co2_consumed} & you passed 5 destinations. WIN!")


#PROBLEM 1: Can't define who win the game, who lost the game --> DONE (Run more test to check further)
#PROBLEM 2: when player keep answer correctly c02 go to minus point. we don't want it go minus. it need to stay at least >0 so we have to do smt with it 
#PROBLEM 3: How to call random question and avoid duplicate question again
#PROBLEM 4: How to add call weather and add score from weather table to co2_consumed score





#TASK NEED TO BE DONE: 
#Task 1: Update question list: more questions, give users idea to put T/F, Y/N, A/B/C/D (Can you also shorten the answer: put only T for True, F for False , Y for Yes, N for No coz it also save time for us to test the code lol I'm tired of typing true, false lol)
#Task 2: How to call the different score in random weather and add on the co2consumed Score (fix the function 4: function called weather)
#Task 3: fix the function 2 called call_airport since it prints 2 times instead of 1 time (Arijana you can tried to change the code like the way you usual call sql instead of my way. Maybe it helps)
#Task 4: make a while loop statement in every input part so if player dont answer yes/no or don't input the result as we expect, the question is asked again until they answer as we want to proceed to next step







#DRAFT TO REUSE WHEN NEEDED, not a code to run in program
"""while co2_consumed < co2_budget:
    for x in range(destinations):
        random_index_number = random.randint(0, len(questions) - 1)
        print(questions[random_index_number])
        user_answer = str(input("Give answer: "))
        right_answer = answers[random_index_number]
        if user_answer == right_answer:
            print("Good job! Your answer is correct.")
            co2_consumed -= 2000
            print(co2_consumed)
            #weather(random_weather1)
        else:
            print("Oops! The answer is wrong. You've consumed 1000 C02 more. Let's check the weather you got!")
            co2_consumed += 2000
            print(co2_consumed)
else:
    print("Game over!")"""

#call Random question
"""
random_index_number = random.randint(0, len(questions)-1)

if random_index_number not in used_index:                               #TO AVOID DUPLICATE QUESTIONS
    print(questions[]) #Random questions
    used_index.append(random_index_number) #Insert the used question's index in the list
    print(used_index)

user_answer = str(input("Give answer: "))
right_answer = answers[random_index_number]
if user_answer == right_answer:
    print("Good job! Your answer is correct. ")

    weather(random_weather1)
else:
    print("Oops! The answer is wrong. You've consumed 1000 C02 more. Let's check the weather you got!")
    random_weather2 = random.randint(1,4)
    weather(random_weather2)
    co2_consumed = co2_consumed + 1000
"""




