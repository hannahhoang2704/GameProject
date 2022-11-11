import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='game_project',
    user='root',
    password='!QAZ2wsx#EDC',  # !QAZ2wsx#EDC or MyN3wP4ssw0rd ##CHECK PASSWORD TO RUN THE PROGRAM!!!
    autocommit=True
)
'''
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

'''

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
rovaniemi_long =25.830400466919

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
    print("Not in Europe!")

