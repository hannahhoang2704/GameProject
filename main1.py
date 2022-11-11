from time import sleep
import mysql.connector
import random
from geopy import distance
import time, os, sys
import pyfiglet
from art import questions, answers

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='game_project',
    user='root',
    password='MyN3wP4ssw0rd',  # !QAZ2wsx#EDC or MyN3wP4ssw0rd ##CHECK PASSWORD TO RUN THE PROGRAM!!!
    autocommit=True
)

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
            print(f"\nYou are now in {row[0]}. Get ready for your flight!\n")
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
            print(deg)
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


def pick_airport1(coordinator_dif_x, coordinator_a_x, coordinator_a_y, coordinator_dif_y):
    sql = "SELECT name FROM airport"
    sql += " WHERE latitude_deg between " + coordinator_dif_x + " and " + coordinator_a_x +" and longitude_deg between " + coordinator_a_y +" and " +coordinator_dif_y
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print({row[0]})
    return row[0]

#Todo1: call the airport name everytime transit to new destinations.
#Todo2: make a new class and add all the game in the class _Main program
#Todo3: change the database to add the gift score_main program
#todo4: calculate the co2 consumption every stop


##START THE GAME
                                      #User input name and city
"""
player_name = input("Let's start with your name: ")
player_name = player_name.capitalize()
"""
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
    icao_selection = str(input('Enter ICAO code again:'))
else:
    location = icao_selection.upper()  # store value of icao
    airport_name = call_airport(icao_selection)  # store airport name in a variable

# The distance between the chosen airport to Rovaniemi airport

coordinator_a = airport_position(icao_selection)
coordinator_b = airport_position("EFRO")

dist = distance.distance(coordinator_a, coordinator_b).km
print(
    f"'Distance between {airport_name} and Rovaniemi Airport is {dist:.2f}km.'\n")
coordinator_scope_x = coordinator_b[0] - coordinator_a[0]
coordinator_scope_y = coordinator_b[1] - coordinator_a[1]
distance_between_coordinator_x = coordinator_scope_x/5
distance_between_coordinator_y = coordinator_scope_y/5

coordinator_a_to_des_1_x = coordinator_a[0] + distance_between_coordinator_x
coordinator_a_to_des_1_y = coordinator_a[1] + distance_between_coordinator_y

pick_airport1(str(coordinator_a[0]), str(coordinator_a_to_des_1_x), str(coordinator_a[1]), str(coordinator_a_to_des_1_y))










"""
x1 = int(input("Put a nr x: "))
y1 = int(input("Put a nr y: "))

a = 1
b = 100

c = 1
d = 100

if x1 >= a and x1 <= b:
    if y1 >= c and y1 <= d:
        print("In Europe!")
else:
    print("Not in Europe!")



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

municipality = input('From which city you want to start your journey: ')
while check_city(municipality) == 0 or municipality.lower() == "rovaniemi":  # Player can't choose Rovaniemi as a starting point
    municipality = input("Oops! You can't fly from this city. Another city please: ")
else:
    print("\nHere are your adventure starting point options: ")
    municipality_search(municipality)


# Users choose the airport in the chosen city

icao_selection = input(f"You can see all the airports in your city above.\n(Enter ICAO to choose the airport you want to fly:)")

while icao_selection.upper() not in icao_list:
    print("Oops! Check again the ICAO code. You can't arrive to the airport if you don't call ICAO code correctly!")
    icao_selection = str(input('Enter ICAO code again:'))
else:
    location = icao_selection.upper()  # store value of icao


calc_distance_to_Rov(1, )
# Function 3: search latitude and longitude coordinates












lat_long_list = []
def lat_long(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident='" + icao + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            lat_long_list.append(row[0])
            latitude = float(row[0])
            longitude = float(row[1])
    return [latitude, longitude]


print(lat_long(icao_selection))

man = lat_long(icao_selection)

latitude = man[0]
longitude = man[1]

rovaniemi_lat = 66.564796447754
rovaniemi_long = 25.830400466919

europe_north = 72.0
europe_south = 34.0

europe_west = -25.0
europe_east = 45.0

if latitude >= europe_south and latitude <= europe_north:
    if longitude >= europe_west and longitude <= europe_east:
        print("In Europe!")
    else:
        print("Not in Europe!")
else:
    print("Not in Europe!")"""

