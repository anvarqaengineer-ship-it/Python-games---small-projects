#Working with the LISTS - This is just a display of the LIST elements
"""
ListElements = ['M1', 'M2', 'M3']
for BMWtypes in ListElements:
    print(BMWtypes)
"""
#Doing more work with the list - Adding some text and displaying the elements each with the TEXT
"""
CarTypes = ["BMW M1", "BMW M2", "BMW M3"]
for BMWs in CarTypes:
    print(f"\nThe available BMW types in our store are {BMWs}!")
"""
#Adding general text after the LOOP of the List
"""
CarTypes = ["BMW M1", "BMW M2", "BMW M3"]
for BMWs in CarTypes:
    print(f"\nThe available BMW types in our store are {BMWs}!")
print("\nThanks for your presence!")
"""
#Making numeral LISTS - Simple numerical list display
"""
for number in range(1, 5):
    print(number)
""" 
#Display of the numerical values in the WHOLE LIST within the TYPE
"""
numbers = list(range(1, 5))
print(numbers)
"""
#SimpleTask - Squaring the number -> Calling the list by squaring each element in the LIST
"""
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    print(f"The squared number is {square}\n")
print(f"The list of squared numbers is {squares}\n")
print(f"The square number of their subtruction {square}!\n")
"""
#LIST Comprehensions
"""
squares = [value**2 for value in range(1, 11)]
print(squares)
"""

#WORKING with the part of a list - Selecting range of elements in the list to display
"""
players = ['Abu', 'Shokir', 'Baxti', 'Akmal', 'Jennifer', 'Jamila', 'John', 'Doston']
print(f"This is the whole list below\n{players}\n")
print(players[0:4])
print(players[0:3])
print(players[0:2])
print(players[0:1])
print(f"\nNow, we are cutting in reverse order!")
print(players[0:-1])
print(players[0:-2])
print(players[0:-3])
print(players[0:-4])
print(f"\nNow are are cutting from both sides")
print(players[1:-1])
print(players[2:-2])
print(players[3:-3])

print(f"\nHere, we are setting the ENDING element in the List starting from the beginning of the list - {players}!")
print(players[:4])

print(f"\nHere, we are setting the ENDING element in the List coming from the end of the list - {players}!")
print(players[2:])

print(f"\nHere, we are cutting the elements in the List coming from start of the list till the last metioned elements - {players}!")
print(players[-3:])
"""
#Copying the list to another list
"""
myFood_List = ['Pizza', 'Falafel', 'Carrot Cake', 'Cheese Cake', ' Lagman', 'Osh']
friendFood_List = myFood_List[:]
print(f"My favourite foods are {myFood_List}!\n")
print(f"My friend's favourite foods are {friendFood_List}!\n")
"""
#Adding elements to the list
"""
myFood_List = ['Pizza', 'Falafel', 'Carrot Cake', 'Cheese Cake', ' Lagman', 'Osh']
myFood_List.append('Burger')
print(f"New list of my favourite {myFood_List}\n")
"""
#Defining a tuple - displaying the elements by INDEX
"""
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
"""
#Looping Through All Values in a Tuple
"""
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
"""
"""
#Writing over a Tuple
dimensions = (200, 50)
print(f"\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print(f"\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
"""
#IF statements - A Simple Example
"""
cars = ['Audi', 'BMW', 'Subaru', 'Toyoto']
for carTypes in cars:
    if carTypes == 'BMW':
        print(carTypes.upper())
    else:
        print(carTypes.title())
"""
#Checking Whether a Value Is in a List - Checking the AGE and comparing it in IF STATEMENTS
"""
age = 15
if age >= 18:
    print(f"\nYou are old enough to vote!")
else:
    print(f"\nYou are not old enough to vote!")
"""
#The if-elif-else Chain - Checking the AGE within the statements
"""
age = 21
if age < 8:
    print(f"\nYour admission cost is $0.")
elif age < 18:
    print(f"\nYour admissions cost is $25.")
else:
    print(f"\nYour admissions cost is $50.")
"""
#Testing Multiple Conditions
"""
Requested_toppings = ['Mushrooms', 'Extra cheese', 'Extra souce', 'Green pepper', 'Chili pepper']
if 'Mushrooms' in Requested_toppings:
    print(f"\nAdding mushrooms to the pizza.")
if 'Extra cheese' in Requested_toppings:
    print(f"\nAdding extra cheese to the pizza.")
if 'Extra souce' in Requested_toppings:
    print(f"\nAdding extra souce to the pizza.")
print(f"\nFinished making your pizza with the additions {Requested_toppings[0], Requested_toppings[1], Requested_toppings[2]}!")
"""
#Checking for Special Items -  An if statement inside the for loop
"""
Requested_toppings = ['Mushrooms', 'Extra cheese', 'Extra souce', 'Green pepper', 'Chili pepper']
for toppings in Requested_toppings:
    if toppings == 'Green pepper':
        print(f"\nAdding the topping '{toppings}'!")
    else:
        print(f"\nSorry, we are run out of the requested ingredient right now!")
print(f"\nFinished making your pizza with the toppings!")
"""
#DICTIONARIES - A Simple Dictionary
"""
aliens = {'color': 'green', 'points': 5}
print(f"\nThe alien's characteristics are {aliens['color'], aliens['points']}!")
#Accessing Values in a Dictionary
aliens = {'color': 'green', 'points': 5, 'eyes': 'One'}
print(f"\nThe view of alien is {aliens['eyes']}!")
#Adding New Key-Value Pairs
alien = {'color': 'green', 'points': 5}
print(alien)
alien['x_position'] = 0
alien['y_position'] = 25
print(f"\nAlien is about {alien}!")
"""
"""
#Starting with an Empty Dictionary
alien = {}
alien['color'] = 'green'
alien['points'] = 5
print(alien)
#Modifying Values in a Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(f"\nThe alien is {alien_0['color']}!")

alien_0['color'] = 'yellow'
print(f"\nThe alien is {alien_0['color']}!")
"""
"""
#Removing Key-Value Pairs - we are deleting the element of the dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
"""
"""
#A Dictionary of Similar Objects - Displaying the element of the dictionary separately by assigning it to a new variable - We are getting the ELEMENT as an OBJECT separately
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
"""
#Using get() to Access Values - We are using the METHOD of get()
"""
alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points']) -> This results in a traceback, showing a KeyError:
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
"""
#Looping Through a Dictionary where we reach everything store as (KEY and VALUE) parameters -> using "for k, v in user_0.items()"
"""
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}\n")
"""
#Looping through all key-value pairs works particularly well- We are displaying the VALUE with the KEY of the parameters in the dictionary
"""
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name, programming_language in favorite_languages.items():
    print(f"\n{name.title()}'s favourite programming language is {programming_language.title()}.")
"""
#Looping Through All the Keys in a Dictionary - Reaching and displaying the NAMES and VALUES separately
"""
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in favorite_languages.keys():
    print(name.title(), "\n")
for language in favorite_languages.values():
    print(language.title(), "\n")
"""
#Looping Through All the Keys in a Dictionary - We are creating another dictionary and if name MATCHES then greeting is DISPLAYED for the matched names
"""
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
"""
#NESTING - A List of Dictionaries(Mixing the lists)
"""
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2] #Here, we are combining the all three dictionaries in one LIST
for alien in aliens:
    print(alien)
"""
#Make an empty list for storing aliens.
"""Here, we are creating an EMPTY LIST
   Then, we are assigning the values(variables) to the list by creating new VARIABLE
   Then, we are looping the filled LIST five time in range to display it with its contents(elements)
   Then, we are printing the total number(length) of the aliens assigned in the LIST    
   
aliens = []
for alien_number in range(30):
    new_alien = {'color': "green", 'point': 5, 'speed': "slow"}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"\nTotal number of aliens: {len(aliens)}!")
"""
#A List in a Dictionary - SAMPLE_1
"""Here, we are creating a list where there is a dictionary with its parameters(values)
   Then, we are printing the list with dictionary elements by reaching each value by looping it
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese', 'extra pepper'],
}
print(f"\nYou ordered a {pizza['crust']}-crust pizza with the following toppings: ")
for topping in pizza['toppings']:
    print("\t" + topping)
#A List in a Dictionary - SAMPLE_2
favourite_languages = {
    'jen': ['python', 'C#', 'C++'],
    'sarah': ['JavaScript'],
    'edward': ['IOS'],
    'phil': ['Kotlin'],
}
for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}!")
"""
#A Dictionary in a Dictionary - Here, we are declaring TWO DICTIONARIES inside of the global dictionary
"""HERE, we are displaying the inner elements of the DICTIONARIES (user1 and user2) contained inside the global DICTIONARY by splitting/assigning them to VARIABLES
users = {
    'user1': {
        'first': 'Albert',
        'last': 'Princeton',
        'location': 'New York'
    },
    'user2': {
        'first': 'Jamilia',
        'last': 'Kuzieva',
        'location': 'Tashkent' 
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\nFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
"""
#USER INPUT AND WHILE LOOPS - Basics(The usage of the "input()" function)
"""
message = input("Tell me something, and I will repeat it: ")
print(message + "\n")
#Now, we will display INPUT TEXT with clear prompts
name = input("Please enter your name: ")
print(f"\nHello there, {name}!")
"""
#Now, we will make the prompt a little difficult
"""HERE, We are assinging the displayed TEXT in a separate VARIABLE and then, we are declaring the variable inside the INPUT function
   Then, we are displaying the (prepaid/assigned to the output TEXT) variable
prompt = "Send some message"
prompt += "\nWhat is your name? "
name = input(prompt)
print(f"\nHello there, {name}!")
"""
"""
#HERE, We are using the numeric case in the loop
height = input("How tall are you, in inches? ")
tall = int(height)


if tall >= 48:
    print(f"\nYou're allowed to the rollercoaster because you're tall enough!")
else:
        print(f"\nYou're not allower to the rollercoaster because you're NOT tall enought!")
"""
"""
#The MODULO Operator -> EVEN or ODD numerations
number = input("Enter a number, I'll tell if it is odd or even: ")
num = int(number)

if num %2 == 0:
    print(f"\nThe number {num} is EVEN.")
else:
    print(f"\nThe number {num} is ODD.")
"""
#Introducing while Loops -> Using the "The while Loop in Action"
"""HERE, we are setting the initial amount for the variable such as (1) in our case and then, looping it by comparing with the number in the LOOP and coming from ONE to FIVE
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
"""
#Letting the User Choose When to Quit -> Here, we can quit from the LOOP anytime during its process. It quits automatically once it reaches the "QUIT" word
"""
text = "\nWrite something here: "
text += "\nEnter to 'quit' to the end. "
message = " "
while message != 'quit':
    message = input(text)
    print(message)
"""
#HERE, we are "Using a Flag" -> Just another alternative of quitting the LOOP using the FLAG option by setting ("Active equal to TRUE")
"""
text = "\nWrite something here: "
text += "\nEnter to 'quit' to the end. "
active = True
while active:
    message = input(text)
    if message == 'quit':
        active = False
    else:
        print(message)
"""
#HERE, we are using the "Using break to Exit a Loop" -> It quits once the break is caught at the word 'QUIT'. Otherwise, the loop is continued
"""
text = "\nWrite something here: "
text += "\nEnter to 'quit' to the end. "
while True:
    words = input(text)
    if words == 'quit':
        break
    else:
        print(f"\nI'd love to learn Python!")
"""
#HERE, we are performing an actual usage of the LOOP -> "Using CONTINUE in a Loop" - HERE, we are allowing(displaying) the ODD numbers only by moduling the numbers in the LOOP
"""
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)
"""
#HERE, we are "Avoiding Infinite Loops" -> This loop will run forever(infinitely)
""""
x = 1
while x <= 5:
    print(x)
    x += 1
"""
#Using a while Loop with Lists and Dictionaries -> Moving Items from One List to Another
"""
unconfirmed_users = ['Alica', 'Bemjamin', 'Lisa', 'Franklin']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying the user: {current_user.title()}")
    confirmed_users.append(current_user)
print(f"\nThe users are all verified now!")
"""
#Removing All Instances of Specific Values from a List -> We are removing the COPIED elements from the list using the METHOD - "REMOVE()"
"""
pets = ['dog', 'cat', 'fish', 'goldgish', 'cat', 'rabbit', 'fish']
print(f"\nYour all pets are {pets[:]}!")
print(f"\tThe total number of your pets is {len(pets)}!")
while 'cat' in pets:
    pets.remove('cat')
print(f"\nNew list of your clearly defined pets {pets[:]}")
print(f"\tThe actual number of your pets is {len(pets)}")
"""
#HERE, we are "Filling a Dictionary with User Input"
"""
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print(f"\n--- Pool Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
"""
#Functions - Defining a Function -> "Passing Information to a Function" - This is a simple FUNCTION to display the user greeting text
"""
def greet_user():
    print("Hello there!")
greet_user()

#HERE, we are Passing Information to a Function - mentioning the passed paremeter in the function and then calling in with added information(argument) later
def greet_user(username):
    print(f"\nHello, {username.title()}!")
greet_user("Anvar")

#Arguments and Parameters -> Passing Arguments
def describe_pets(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pets("Dog", "Harry")

#HERE, we are performing the "Multiple Function Calls" -> we are calling the function with different parametres in the display
def describe_pets(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pets("Dog", "Harry")
describe_pets("Cat", "Molly")

#HERE, we are performing the "Order Matters in Positional Arguments" -> The arguments in the called function are written vice-versa so they are called in reverse orders
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('harry', 'hamster')

#RETURNING FUNCTIONS -> In the DICTIONARIES | Making an Argument Optional
def get_formatted(fname, lname, mname=""):
    if mname:
        full_name = f"{fname} {mname}"
    else:
        full_name = f"{fname} {lname}"
    return full_name.title()
person = get_formatted("Anvar", "Narzulloev")
print(person)

#RETURNING THE DICTIONARY by Using a Function with a while Loop with the option to quit when 'q' is selected
def getNew_name(fname, lname, age="None"):
    full_name = f"{fname} {lname} {age}"
    return full_name.title()
while True:
    print("\nPlease tell me your full name:")
    print("\nOr enter 'q' anytime to quit, please")
    fname = input("\nFirst name: ")
    if fname == 'q':
        break
    lname = input("\nLast name: ")
    if lname == 'q':
        break
    age = input("\nAge: ")
    if age == 'q':
        break
    get_name = getNew_name(fname, lname, age)
    print(f"\nHello, {get_name}!")

#Passing a List - Here, we are setting the loop for the greeting the name(elements of the list) and below calling the LIST elements updated with greeting in the FUNCTION
def greet_users(names):
    for name in names:
        message = f"Hello, {name.title()}!"
        print (message)
usernames = ['Hannah', 'Jackie', 'Alla']
greet_users(usernames)

#Modifying a List in a Function
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Passing an Arbitrary Number of Arguments - A function that allows to collect an arbitary number of arguments from the calling statement(ahead)
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
"""
#Mixing Positional and Arbitrary Arguments
"""
def make_pizze(size, *toppings):
    print(f"\nMaking a {size}-cm pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizze(25, 'pepperoni')
make_pizze(30, 'mushrooms', 'green peppers', 'extra cheese')

#Using Arbitrary Keyword Arguments
def create_person(fname, lname, **user_info):
    user_info['first_name'] = fname
    user_info['last_name'] = lname
    return user_info
user_profile = create_person('Enver', 'Nazar', location='Tashkent', country='Uzbekistan', field='Computer Science and Software Engineering')
print(user_profile)

#Storing Your Functions in Modules - Importing an Entire Module
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-cm pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

#Classes - classes that represent real-world things and situations, and you create objects based on these classes
#HERE, we are "Creating and Using a Class" - SAMPLE: Creating the Dog Class
class Dog:
    def __init__(self, name, age, breed): #Here, we are INITIALIZING the parametres with 'SELF' in the set inside of the CLASS to use them later in the functions
        self.name = name
        self.age = age
        self.breed = breed
    def sit(self):
        print(f"{self.name} is sitting now.")
    def roll_over(self):
        print(f"{self.name} rolled over!")
    def play(self):
        print(f"{self.name} is playing")
#Making an Instance from a Class - Upper mentioned class is predefined with FUNCTIONS - We are below just setting the PARAMETERS and calling them (WE AREN'T CALLING THE FUNCTION YET)
#HERE, we are "Accessing Attributes" -> Just displaying the attributes with some additional information
myDog = Dog("Willie", 2, "Husky")
print(f"My dog's name is {myDog.name}")
print(f"My dog is {myDog.age} years old.")
print(f"My {myDog.name}'s breed is {myDog.breed}!")
#HERE, we are "Calling Methods"
myDog.sit()
myDog.roll_over()
#HERE, we are "Creating Multiple Instances"
myFriend_Dog = Dog("Jessica", 1, "Chihiauhia")
print(f"\nHer dog's name is {myFriend_Dog.name}")
print(f"Her dog is {myFriend_Dog.age} years old.")
print(f"Her {myFriend_Dog.name}'s breed is {myFriend_Dog.breed}!")
myFriend_Dog.play()

#Working with Classes and Instances - modify the attributes associated with a particular instance
#THE CAR CLASS - example
class Car:
    def __init__(self, model, brand, year):
        self.model = model
        self.brand = brand
        self.year = year
    def get_info(self):
        full_information = f"{self.model} by the brand of {self.brand} made in {self.year}"
        return full_information.title()
my_NewCar = Car("GLS 600 Maybach", "Mercedes", 2026)
print(f"My new car is {my_NewCar.get_info()}!")

#HERE, we are "Setting a Default Value for an Attribute"
class Car:
    def __init__(self, model, brand, year): #HERE, we are defining the ATTRIBUTES in the "SELF" so we can later call them in any FUNCTION
        self.model = model
        self.brand = brand
        self.year = year
        self.odometer_reading = 0 #We are setting the DEFAULT VALEU as 0 for the current ATTRIBUTE
    def get_info(self):
        full_information = f"My car is '{self.model}' by the brand of {self.brand} made in {self.year}"
        return full_information.title()
    def read_odometer(self):
        print(f"My car has {self.odometer_reading} km on it!") #We are setting the predefined ATTRIBUTE (odometer_reading) in the display when this FUNCTION IS CALLED
my_NewCar = Car("BMW i3 40L iSport", "BMW", 2025)
print(my_NewCar.get_info())
my_NewCar.read_odometer()

#HERE, WE ARE NOW - "Modifying Attribute Values"
class Car:
    def __init__(self, model, brand, year): #HERE, we are defining the ATTRIBUTES in the "SELF" so we can later call them in any FUNCTION
        self.model = model
        self.brand = brand
        self.year = year
        self.odometer_reading = 0 #We are setting the DEFAULT VALEU as 0 for the current ATTRIBUTE
    def get_info(self):
        full_information = f"My car is '{self.model}' by the brand of {self.brand} made in {self.year}"
        return full_information.title()
    def read_odometer(self):
        print(f"My car has {self.odometer_reading} km on it!") #We are setting the predefined ATTRIBUTE (odometer_reading) in the display when this FUNCTION IS CALLED
my_NewCar = Car("BMW i3 40L iSport", "BMW", 2025)
print(my_NewCar.get_info()) #HERE, we are calling the function itself along with it ASSIGNED TO the variable which is getting the VALUES by the CALLS ATTRIBUTES 
 #HERE, we are renewing the predefined in the CLASS "odometer_reading" attribute's value
my_NewCar.read_odometer()

#HERE, we are "Modifying an Attribute’s Value Through a Method"
class Car:
    def __init__(self, model, brand, year): #HERE, we are defining the ATTRIBUTES in the "SELF" so we can later call them in any FUNCTION
        self.model = model
        self.brand = brand
        self.year = year
        self.odometer_reading = 0 #We are setting the DEFAULT VALEU as 0 for the current ATTRIBUTE
    def get_info(self):
        full_information = f"My car is '{self.model}' by the brand of {self.brand} made in {self.year}"
        return full_information.title()
    def read_odometer(self):
        print(f"My car has {self.odometer_reading} km on it!") #We are setting the predefined ATTRIBUTE (odometer_reading) in the display when this FUNCTION IS CALLED
    def updated_odometer(self, mileage):
        self.odometer_reading = mileage #HERE, we are UPDATING THE ATTRIBUTE by getting and resetting the "odometer_reading" VALUE to new VARIABLE so it can be updated within the FUNCTION CALL
my_NewCar = Car("BMW i3 40L iSport", "BMW", 2025)
print(my_NewCar.get_info())
my_NewCar.read_odometer()
my_NewCar.odometer_reading = 139000
print("\nNow, the UPDATED odometer 2nd time!")
my_NewCar.updated_odometer(140000)
my_NewCar.read_odometer()

#The Modified  method
class Car:
    def __init__(self, model, brand, year): #HERE, we are defining the ATTRIBUTES in the "SELF" so we can later call them in any FUNCTION
        self.model = model
        self.brand = brand
        self.year = year
        self.odometer_reading = 0 #We are setting the DEFAULT VALEU as 0 for the current ATTRIBUTE
    def get_info(self):
        full_information = f"My car is '{self.model}' by the brand of {self.brand} made in {self.year}"
        return full_information.title()
    def read_odometer(self):
        print(f"My car has {self.odometer_reading} km on it!") #We are setting the predefined ATTRIBUTE (odometer_reading) in the display when this FUNCTION IS CALLED
    def updated_odometer(self, mileage):
        self.odometer_reading = mileage #HERE, we are UPDATING THE ATTRIBUTE by getting and resetting the "odometer_reading" VALUE to new VARIABLE so it can be updated within the FUNCTION CALL
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
my_NewCar = Car("BMW i3 40L iSport", "BMW", 2025)
print(my_NewCar.get_info())
my_NewCar.read_odometer()
my_NewCar.odometer_reading = 139000
print("\nNow, the UPDATED odometer 2nd time!")
my_NewCar.updated_odometer(140000)
my_NewCar.read_odometer()

#Inheritance - The __init__() Method for a Child Class
class Car: #This is the PARENT CLASS
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_name(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kms on it!")
    def update_odometer(self, kilometres):
        if kilometres >= self.odometer_reading:
            self.odometer_reading = kilometres
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, mileage):
        self.odometer_reading += mileage
        
class ElectricCar(Car): #This is the CHILD CLASS and Represent aspects of a car, specific to electric vehicles.
    def __init__(self, make, model, year):
        super().__init__(make, model, year) #HERE, Initialize attributes of the parent class.
my_tesla = ElectricCar('Tesla', 'Model Y', 2023)
print(my_tesla.get_name())

#Defining Attributes and Methods for the Child Class
class Car: #This is the PARENT CLASS
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_name(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kms on it!")
    def update_odometer(self, kilometres):
        if kilometres >= self.odometer_reading:
            self.odometer_reading = kilometres
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, mileage):
        self.odometer_reading += mileage
        
class ElectricCar(Car): #This is the CHILD CLASS and Represent aspects of a car, specific to electric vehicles.
    def __init__(self, make, model, year):
        super().__init__(make, model, year) #HERE, Initialize attributes of the parent class.
        self.battery_size = 75
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
my_tesla = ElectricCar('Tesla', 'Model Y', 2023)
print(my_tesla.get_name())
my_tesla.describe_battery()

#Overriding Methods from the Parent Class
class Car: #This is the PARENT CLASS
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_name(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kms on it!")
    def update_odometer(self, kilometres):
        if kilometres >= self.odometer_reading:
            self.odometer_reading = kilometres
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, mileage):
        self.odometer_reading += mileage
        
class ElectricCar(Car): #This is the CHILD CLASS and Represent aspects of a car, specific to electric vehicles.
    def __init__(self, make, model, year):
        super().__init__(make, model, year) #HERE, Initialize attributes of the parent class.
        self.battery_size = 75
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('Tesla', 'Model Y', 2023)
print(my_tesla.get_name())
my_tesla.describe_battery()

#Instances as Attribute - We can n break your large class into smaller classes that work together and "part of one class can be written as a separate class"
class Car: #This is the PARENT CLASS
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_name(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kms on it!")
    def update_odometer(self, kilometres):
        if kilometres >= self.odometer_reading:
            self.odometer_reading = kilometres
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, mileage):
        self.odometer_reading += mileage
        
class Battery: #This is another PARENT CLASS - Where we can use a "Battery instance as an attribute in the ElectricCar class"
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size} on it!")
        
class ElectricCar(Car): #This is the CHILD CLASS and Represent aspects of a car, specific to electric vehicles.
    def __init__(self, make, model, year):
        super().__init__(make, model, year) #HERE, Initialize attributes of the parent class.
        self.battery_size = 75
        self.battery = Battery()
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('Tesla', 'Model Y', 2023)
print(my_tesla.get_name())
my_tesla.battery.describe_battery()

class Car: #This is the PARENT CLASS
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_name(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kms on it!")
    def update_odometer(self, kilometres):
        if kilometres >= self.odometer_reading:
            self.odometer_reading = kilometres
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, mileage):
        self.odometer_reading += mileage
        
class Battery: #This is another PARENT CLASS - Where we can use a "Battery instance as an attribute in the ElectricCar class"
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size} on it!")
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} kilometres on a full charge!")
class ElectricCar(Car): #This is the CHILD CLASS and Represent aspects of a car, specific to electric vehicles.
    def __init__(self, make, model, year):
        super().__init__(make, model, year) #HERE, Initialize attributes of the parent class.
        self.battery_size = 75
        self.battery = Battery()
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('Tesla', 'Model Y', 2023)
print(my_tesla.get_name())
my_tesla.battery.describe_battery() #HERE, we are calling the FUNCTION out of the PARENT CLASS
my_tesla.battery.get_range()

#Importing Classes - Importing a Single Class
class Car:
    def __init__(self, model, brand, year): #HERE, we are defining the ATTRIBUTES in the "SELF" so we can later call them in any FUNCTION
        self.model = model
        self.brand = brand
        self.year = year
        self.odometer_reading = 0 #We are setting the DEFAULT VALEU as 0 for the current ATTRIBUTE
    def get_info(self):
        full_information = f"My car is '{self.model}' by the brand of {self.brand} made in {self.year}"
        return full_information.title()
    def read_odometer(self):
        print(f"My car has {self.odometer_reading} km on it!") #We are setting the predefined ATTRIBUTE (odometer_reading) in the display when this FUNCTION IS CALLED
    def updated_odometer(self, mileage):
        self.odometer_reading = mileage #HERE, we are UPDATING THE ATTRIBUTE by getting and resetting the "odometer_reading" VALUE to new VARIABLE so it can be updated within the FUNCTION CALL
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

#Storing Multiple Classes in a Module
class Car: #This is the PARENT CLASS
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_name(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kms on it!")
    def update_odometer(self, kilometres):
        if kilometres >= self.odometer_reading:
            self.odometer_reading = kilometres
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, mileage):
        self.odometer_reading += mileage
        
class ElectricCar(Car): #This is the CHILD CLASS and Represent aspects of a car, specific to electric vehicles.
    def __init__(self, make, model, year):
        super().__init__(make, model, year) #HERE, Initialize attributes of the parent class.
        self.battery_size = 75
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

#Files and Exceptions | Reading from a File - Reading an Entire File
with open('pi_digits.txt') as file_object:
    contents = file_object.read() #HERE, we are reading the TEXT and dispaying it by assigning to a VARIABLE
print(contents)

#File Paths - (with open('text_files/filename.txt') as file_object:) -> to remove the extra blank line, you can use rstrip(), lstrip() or strip() in the call to print()
with open('pi_digits.txt') as file_object:
    contents = file_object.read() #HERE, we are reading the TEXT and dispaying it by assigning to a VARIABLE
print(contents.rstrip())
print(contents.lstrip())
print(contents.strip())

#Relative paths are usually shorter than absolute paths - RELATIVE PATH
with open('text_files/filename.txt') as file_object:

#Absolute paths are usually longer than relative paths - ABSOLUTE PATH
file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
with open(file_path) as file_object:

#Reading Line by Line - This is a specific kind of formatting by examining each line from a file one at a time
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

#Making a List of Lines from a File -> Working with a File’s Contents
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines() #HERE, the "readlines() method" takes each line from the file and stores it in a list
pi_string = ''
for line in lines:
    pi_string += line.strip()
    print(pi_string)
    print(len(pi_string))

#Large Files: One Million Digits
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    print(f"{pi_string[:52]}...")
    print(len(pi_string))

#TESTING YOUR CODE - Testing a Functionm
def get_formatted_name(fname, middle, lname):
    full_name = f"{fname} {middle} {lname}"
    return full_name.title()

#A Class to TEST
class ASurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []
 
    def show_question(self):
        print(self.question)
 
    def store_response(self, new_response):
        self.responses.append(new_response)
 
    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
"""
#PART || Projects - Project #1 (Alien Invasion) -> A Ship that Fires Bullets
"""
Starting the Game Project - Creating a Pygame Window and Responding to User Input

import sys
import pygame
from sample import Settings
from test import Ship
class AlienInvasion: #Refactoring: The _check_events() and _update_screen() Methods - The _check_events() Method
#Piloting the Ship - Responding to a Keypress
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
    def _check_events(self): #Respond to keypresses and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #Move the ship to the right
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
    def _update_screen(self): #Update images on the screen, and flip to the new screen
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

def PersonName(): #Created a FUNCTION named 'PersonName' and set the arguments in it
    fname = "Anvar"
    lname = "Narzulloev"
    full_name = f"My full name is {fname} {lname}!"
    return full_name.title()
print(PersonName())

# products TYPES -> int(integer), float(decimal numbers), string(words), boolean(true,false)
a = 10.0
b = 7
c = "Enverbey"
d = True

print(type(a), type(b), type(c), type(d))

#TYPECASTING -> Implicit & Explicit products TYPES | Converting products types FUNCTIONS
#The TYPECASTING FUNCTIONS are the followings -> "ord(), hex(), oct(), tuple(), set(), list(), dict()"
a = True
b =True
c = a == b
print(c)

# THERE are different verions of LOOPS -> NestedLOOP, OuterLOOP and InnerLOOP
list1 = [1,2,3]
list2 = [4,5,6]
count = 0
for x in list1:
    count+=1
    for y in list2:
        count+=1
print(count)

num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]

count = 0  # шаг 5

for index, num in enumerate(num_list):  # шаг 4
    count += 1  # шаг 6

    if num == 36:  # шаг 4 и 8
        print("Номер найден в позиции:", index)
        break

    if num > 45:  # шаг 2 и 3
        print("Больше 45")
    else:
        print("Меньше 45")5

print("Количество итераций:", count)  # шаг 7

# user_num_1 = input('First number is: ')
# user_num_2 = input('Second number is: ')
# print(user_num_1, user_num_2)
# user_sum = int(user_num_1) + int(user_num_2)
# print(user_sum)
# products types and variables
greeting = "Hello there, I've started learning Python!" #This is the SIMPLE output of the text in the ypeof(string = str)
print(greeting)

fname = "Anvar" #HERE, we are assingning string variable and then setting it to one general variable to display with som extra text
lname = "Narzulloev"
full_n = f"My full name is {fname} {lname}"
print(full_n, "and I' learning Python to become a back-end developer!")

fname = str(input("Please enter your first name: "))
lname = str(input("Please enter your surname: "))
age = int(input("Please enter your age: "))

full_info = f"Your information is '{fname} {lname} and {age}' has been approved! You are now allowed to use our services legally. Thanks for chosing us!\n"
print(full_info)

#INTRODUCTION to the LIST - list is created using the brackets -> []
cars = ['Mercedes', 'BMW', 'AUDI']
print(cars) #PRINTING the list wholly
print(f"Our 1st car is {cars[0]} in our saloon - price tag is around $85000 - $215000") #PRINTING the 1st elements in the list
print(f"Our 2nd car is {cars[1]} in our  saloon - price tag is around $75000 - $235000") #PRINTING the 2nd elements in the list")
print(f"Our 2nd car is {cars[2]} in our  saloon - price tag is around $795000 - $245000") #PRINTING the 3rd elements in the list")
#NOW, we are Changing, Adding, and Removing Elements - modifying the LIST elements by different options - CHANGING
cars[1] = 'Toyoto' #HERE, we are changes the element of BMW in the list (updated) to TOYOTO by replacing it
print(cars)
#NOW, we are Changing, Adding, and Removing Elements - modifying the LIST elements by different options - ADDING
cars.append('BMW') #HERE, we are added the element of BMW to the list (updated) at the end of the list
print(cars)
#NOW, we are Changing, Adding, and Removing Elements - modifying the LIST elements by different options - DELETING
del cars[3] #HERE, we are deleted the element of BMW to the list (removing) at the end of the list
print(cars)

#FUNCTIONS - by video material learning
# bill = 50
# tax = 5
# total = (bill*tax)/100

# print(f"Total is {total}!")
my_global = 10
def local():
    my_enclosed = 20
    def inner_local(): #So, the inner local FUNCTION always has an access to the all(inside scopes and outside scopes)
        my_local = 5
        print("Access to the Global", my_global)
        print("Access to the Enclosed", my_enclosed)
    inner_local()
local()

#DICTIONARY -> (KEY: VALUE)
Animals = {
    'Lion': 'Cat family',
    'Wolf': 'Dog family',
    'Eagle': 'Bird family'
}

with open("animals.txt", mode='w') as file:
    file.writelines(["This is 1st line. \n This is 2nd line."])

with open("animals.txt", mode='r') as file:
    filename = file.readlines()
print(filename)

def find_sum(num):
    count = 0
    for x in range(100):
        if x == num:
            print("Total Iterations: " + count)
            return x
        count += 1
find_sum(100)

#FUNCTIONS - appending new item to the list
my_list = [1, 2, 3]
def add_to_list(item):
    my_list.append(item)
    return my_list

new_list = add_to_list(2)
print(my_list)

#FUNCTIONS - functional factorial
def find_factorial_by_looping(n):
    if n<0:
        return 0
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial = factorial * i
        return factorial
print(find_factorial_by_looping(5))

def summation(n):
       if n == 1:
           return n + summation(n-1)
       return 0
a = summation(5)
print(a)

#OOP Learning in the coursera - the main concepts | There are a lot of paradigms(Main three are Object-oriented, Procedural and Functional)
#Creating a calls with an object
class MyClass:
    myObject = 5
    def greeting(self):
        print("Hello there developer!")
myClass = MyClass()
print(MyClass.myObject)
print(myClass.myObject)
print(myClass.greeting())

products = []

n = int(input("Сколько записей? "))

# ввод данных
for i in range(n):
    name = input("Название товара: ")
    value = int(input("Количество: "))
    products.append((name, value))

# считаем по товарам
result = {}

for name, value in products:
    if name in result:
        result[name] += value
    else:
        result[name] = value

# общая сумма
total = sum(result.values())

# убираем НДС 20%
profit = total * 0.8

# вывод
print("\nПо товарам:", result)
print("Общая сумма:", total)
print("Прибыль без НДС:", profit)

class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass
house = House()

print(house.num_rooms)
print(House.num_rooms,"\n")

house.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms,"\n")

House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms,"\n")

print(house.bathrooms)
print(House.bathrooms,"\n")

#Initializing an OBJECT - AN EXAMPLE
from typing import Self
class Recipe():
    def __init__(self, dish, items, time) -> None:
            self.dish = dish
            self.items = items
            self.time = time
    def content(self):    
        print("The"+self.dish+"has"+str(self.items)+"and takes"+str(self.time)+"min to prepare!")
pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
print(pizza.dish)
print(pizza.items)
print(pizza.time)

class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"
    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)
whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")

MagicBox = ['iPhone 15 Pro', 'Samsung Galaxy S25 Ultra', 'Huawei Mate Pro 10', 'Teddy Bear', 'Kia K5']

prizes = len(MagicBox)
for i in range(prizes - 1, -1, -1):
    if range == 4:
        break
    else:
        print(MagicBox[i])
"""
#####################################################################################################################################
"""
arr = [
    [1, 2, 3, 4],
    [9, 0, 1, 5],
    [1, 10, 5, 3]
]
print(f"The massive before change: {arr[:]}!\n")


for indexOUTER in range(len(arr)):
    for indexINNER in range(len(arr[indexOUTER])):
        if arr[indexOUTER][indexINNER] >= 5:
            arr[indexOUTER][indexINNER] = 0

print(f"The massive after change: {arr[:]}!\n")

class Emplyees:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last

class Supervisors(Emplyees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password
        
class Chefs(Emplyees):
    def leave_request(self, days):
        return "May I take a leave for" + str(days) + "days?"
    
adrian = Supervisors("Adrian", "A", "apple")
emily = Chefs('Emily', "E")
adrian = Chefs("Juno", "J")

print(emily.leave_request(3))
print(adrian.password)
print(emily.name)

#Learning again from the SCRATCH- PYTHON MODULES - #SAMPLE TASK(Data Type)
first_variable = 'This is my 1st variable assigned and printed!'
print(first_variable)

repeated_variable = 'This is my 1st variable assigned and printed!'
print(repeated_variable)

repeated_variable = "This is the changed variable content now!"
print(repeated_variable)
"""
# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         # word = "Alla"
#         for x in range(x):

# for text in range(9,0,2):
#     print(text)
# number = 2526
# long = (number//100) # Определение полных чисел
# print(f"The distance in meters is {long}")

# weight =1786
# mass = (weight//1000)
# print(f"The weight in kilo is {mass}")

# bytes = 25566
# kilobytes = (bytes*0.001)
# print(kilobytes)

# A = int(input("Введите A: "))
# B = int(input("Введите B: "))

# count = A // B

# print("Количество отрезков B:", count)

#Relaod functions
# import importlib
# import test

# importlib.reload(test)

#HERE, we are displaying the PATH of the system where working in a particular directory
# import os
# contents = os.listdir(r'C:\Users\ANarzulloev\OneDrive - beeline.uz\Рабочий стол\LearnPython\alien_invasion.py')
# print(contents)
"""
import importlib
import test

def currDir():
    try:
        importlib.reload(test)
        test.current_directory()
    except:
        pass

for i in range(5):
    currDir()
    input("Hit enter to reload...")
"""
#Writing simple Pytest for Unittesting
# def add(a,b):
#     return a + b
# def sub(a, b):
#     return a - b
# def bigo(numbers):
#     for i in numbers:
#         print(numbers)

# A = int(input("Введите A: "))
# B = int(input("Введите B: "))

# count = A % B
# print(count)

#Task by learning python
# print("Please enter a value!\n")
# a = int(input("Enter 1st number: "))

# print("Finding the tens digit!")
# tens_digit = a // 10
# print(f"The tens digit of the number {a} is: {tens_digit}")

# print("\nFinding the units digit!")
# units_digit = a % 10
# print(f"The units digit of the number {a} is: {units_digit}")
"""
#Integer7. Дано двузначное число. Найти сумму и произведение его цифр.
a = int(input("Enter a two-digit number: "))    
if 10 < a < 99:
    tens_digit = a // 10
    units_digit = a % 10
    sum_digits = tens_digit + units_digit
    product_digits = tens_digit * units_digit
    print(f"The sum of the digits is: {sum_digits}")
    print(f"The product of the digits is: {product_digits}")

#Integer8. Дано двузначное число. Вывести его в виде десяти и единиц. Например, число 35 вывести как 3 и 5.
a = int(input("Enter a two-digit number: "))
if 10 < a < 99:
    tens = a // 10
    units = a % 10
    print(tens)
    print(units)
"""

# num = 246
# digit = num // 100
# print(digit)

# n = 145
# last = n % 10
# print(last)

# n = 145
# mid = (n // 10) % 10
# print(mid)
# a = 456
# hundreds = a // 100
# tens = (a // 10) % 10
# units = a % 10
# sum = hundreds + tens + units
# multiply = hundreds * tens * units
# print(sum)
# print(multiply)

# a = 246
# num = ((a // 100) % 100) + ((a // 10) % 10) + (a % 10)
# print(num)
# multiply = ((a // 100) % 100) * ((a // 10) % 10) * (a % 10)
# print(multiply)

#Integer12. Дано трехзначное число. Вывести число, полученное при прочтении исходного числа справа налево
# a = 123
# hundreds = a // 100
# tens = (a // 10) % 10
# units = a % 10
# print(a)
# print(hundreds)
# print(tens)
# print(units)
# reversed_num = (units * 100) + (tens * 10) + hundreds
# print(reversed_num)

#Integer13. Дано трехзначное число. В нем зачеркнули первую слева цифру и приписали ее справа. Вывести полученное число
# b = 451
# print(b)
# hundreds = b // 100
# print(hundreds)
# tens = (b // 10) % 10
# print(tens)
# units = b % 10
# print(units)
# changed_position = (tens * 100) + (units * 10) + hundreds
# print(changed_position)
# #Integer13. Дано трехзначное число. В нем зачеркнули первую слева цифру и приписали ее справа. Вывести полученное число.
# num = 451
# result = (num % 100)*10 + num // 100
# print(result)

"""
#HERE, we are finding the different cases of the digits in the number by using the different operations
n = 456
case1 = n // 10
case2 = n // 100
case3 = n % 10
case4 = n % 100
case5 = (n // 10) % 10
case6 = (n // 100) % 10
case7 = (n // 10) % 100
case8 = (n // 100) % 100
case9 = (n % 10) // 10
case10 = (n % 100) // 10
case11 = (n % 100) // 10
case12 = (n % 100) // 100
print(case1)
print(case2)
print(case3)
print(case4)
print(case5)
print(case6)
print(case7)
print(case8)
print(case9)
print(case10)
print(case11)
print(case12)
"""
# num = 756
# print(f"The number is: {num}!")
# print("\nNow, we have the shifted case of last digit of any given number to the left and the rest of the digits to the right!")

# hundreds = num // 100
# tens = (num // 10) % 10
# units = num % 10
# shifted_num = units * 100 + hundreds * 10 + tens
# print(shifted_num)
# print(f"The shifted number is: {shifted_num}!")

#Integer15. Дано трехзначное число. Вывести число, полученное при перестановке цифр сотен и десятков исходного числа (например, 123 перейдет в 213)
# n = 516
# print(f"The number is: {n}!")
# hundreds = n // 100
# tens = (n // 10) % 10
# digit = n % 10

# re_arranded_num = tens * 100 + hundreds * 10 + digit
# print(f"The rearranged number is: {re_arranded_num}")

#Integer16. Дано трехзначное число. Вывести число, полученное при перестановке цифр десятков и единиц исходного числа (например, 123 перейдет в 132)
# n = 786
# print(n)
# changed_num = (n // 100) * 100 + (n % 10) * 10 + (n // 10) % 10
# print(changed_num)

#Integer17. Дано целое число, большее 999. Используя одну операцию деления нацело и одну операцию взятия остатка от деления, найти цифру, соответствующую разряду сотен в записи этого числа
# n = 12345
# hundreds_digit = (n // 100) % 10
# print(f"The result of {n} is: {hundreds_digit}")

#Integer18. Дано целое число, большее 999. Используя одну операцию деления нацело и одну операцию взятия остатка от деления, найти цифру, соответствующую разряду тысяч в записи этого числа
# n = 12345
# thousand = (n // 1000) % 10
# print(thousand)

#Integer19. начала суток прошло N секунд (N — целое). Найти количество полных минут, прошедших с начала суток
# n = 86400
# min = n // 60
# print(min)

#Integer20. С начала суток прошло N секунд (N — целое). Найти количество полных часов, прошедших с начала суток
# n = 432000
# hours = n // 3600
# print(hours)

#Integer21. С начала суток прошло N секунд (N — целое). Найти количество секунд, прошедших с начала последней минуты
# n = 86400
# minute_seconds = n % 60
# print(minute_seconds)

#Integer22. С начала суток прошло N секунд (N — целое). Найти количество се-кунд, прошедших с начала последнего часа
# n = 432000
# hour_seconds = n % 3600
# print(hour_seconds)

#Integer23. С начала суток прошло N секунд (N — целое). Найти количество полных минут, прошедших с начала последнего часа
# n = 5184000
# full_minutes = (n % 3600) // 60
# print(full_minutes)

#Integer24. Дни недели пронумерованы следующим образом: 0 — воскресенье, 1 — понедельник, 2 — вторник, …, 6 — суббота. Дано целое число K, лежащее в диапазоне 1–365. Определить номер дня недели для K-го дня года, если известно, что в этом году 1 января было понедельником
# k = 235
# day_of_week = (k + 1) % 7
# print(day_of_week)

#Iterate over strings - explanation using list
#planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# while True:
#     planets = [input("Please enter a planet: ")]
#     for planet in planets: #Here, we are just displaying the elements of the list one by one by using the for loop
#         if planet == 'Earth':
#             print(f"{planet} is the only planet that has life on it!")
#         elif planet == 'Mars':
#             print(f"{planet} is the red planet!")
#         elif planet == 'Jupiter':
#             print(f"{planet} is the biggest planet in the solar system!")
#         elif planet == 'Saturn':
#             print(f"{planet} is the planet with the most beautiful rings in the solar system!")
#         elif planet == 'Uranus':
#             print(f"{planet} is the planet that rotates on its side!")
#         elif planet == 'Neptune':
#             print(f"{planet} is the farthest planet from the sun in the solar system!")
#         elif planet == 'Mercury':
#             print(f"{planet} is the closest planet to the sun in the solar system!")
#         elif planet == 'Venus':
#             print(f"{planet} is the hottest planet in the solar system!")
#         elif planet == 'Pluto':
#             print(f"{planet} is the dwarf planet in the solar system!")
#         elif planet == 'Ceres':
#             print(f"{planet} is the largest object in the asteroid belt between Mars and Jupiter!")
#         elif planet == 'Eris':
#             print(f"{planet} is the most massive dwarf planet in the solar system!")
#         elif planet == 'Haumea':
#             print(f"{planet} is the dwarf planet with the fastest rotation in the solar system!")
#         elif planet == 'Makemake':
#             print(f"{planet} is the dwarf planet that is the second brightest object in the Kuiper belt after Pluto!")
#         elif planet == 'Ganymede':
#             print(f"{planet} is the largest moon in the solar system and is even bigger than the planet Mercury!")
#         elif planet == 'Titan':
#             print(f"{planet} is the second largest moon in the solar system and is larger than the planet Mercury!")
#         elif planet == 'Callisto':
#             print(f"{planet} is the third largest moon in the solar system and is larger than the planet Mercury!")
#         elif planet == 'Io':
#             print(f"{planet} is the fourth largest moon in the solar system and is larger than the planet Mercury!")
#         elif planet == 'Europa':
#             print(f"{planet} is the fifth largest moon in the solar system and is larger than the planet Mercury!")
#         elif planet == 'Triton':
#             print(f"{planet} is the largest moon of Neptune and is larger than the planet Mercury!")
#         elif planet == 'Sun':
#             print(f"{planet} is not a planet but the star at the center of the solar system!")
#         elif planet == 'Moon':
#             print(f"{planet} is not a planet but the natural satellite of Earth!")
#         else:
#             print(f"{planet} is not a planet in the solar system!")
#     print("\nPlease enter \"Q\" or type 'exit' to quit the program!")
import tkinter as tk
import random

# Данные
questions = {
    "earth": "🌍 This planet has life.",
    "mars": "🔴 Known as the red planet.",
    "jupiter": "🟠 The biggest planet.",
    "saturn": "🪐 Has beautiful rings.",
    "uranus": "🔵 Rotates sideways.",
    "neptune": "🌊 The farthest planet.",
    "mercury": "☀️ Closest to the Sun.",
    "venus": "🔥 The hottest planet.",
    "pluto": "🧊 A dwarf planet."
}

planets = list(questions.keys())

score = 0
lives = 3
correct_answer = ""

# Новый вопрос
def next_question():
    global correct_answer

    correct_answer = random.choice(planets)
    question_text = questions[correct_answer]

    label_question.config(text=question_text)

    # генерируем варианты
    options = [correct_answer]
    while len(options) < 4:
        choice = random.choice(planets)
        if choice not in options:
            options.append(choice)

    random.shuffle(options)

    # назначаем текст кнопкам
    for i in range(4):
        buttons[i].config(text=options[i].title(), state="normal")

# Проверка ответа
def check_answer(selected):
    global score, lives

    if selected == correct_answer:
        score += 1
        label_feedback.config(text="✅ Correct!", fg="lightgreen")
    else:
        lives -= 1
        label_feedback.config(
            text=f"❌ Wrong! It was {correct_answer.title()}",
            fg="red"
        )

    label_score.config(text=f"Score: {score}")
    label_lives.config(text=f"Lives: {lives}")

    # блокируем кнопки
    for btn in buttons:
        btn.config(state="disabled")

    if lives == 0:
        game_over()
    else:
        root.after(1500, next_question)

# Game Over
def game_over():
    label_question.config(text="💀 GAME OVER")
    label_feedback.config(text=f"Final Score: {score}", fg="white")
    btn_restart.pack(pady=10)

# Рестарт
def restart_game():
    global score, lives
    score = 0
    lives = 3

    label_score.config(text="Score: 0")
    label_lives.config(text="Lives: 3")
    label_feedback.config(text="")

    btn_restart.pack_forget()
    next_question()

# GUI
root = tk.Tk()
root.title("🎮 Planet Quiz - Level 3")
root.geometry("450x350")
root.configure(bg="#0b1a2a")

title = tk.Label(root, text="🌌 Planet Quiz", font=("Arial", 16, "bold"), fg="white", bg="#0b1a2a")
title.pack(pady=10)

label_question = tk.Label(root, text="", font=("Arial", 12), fg="white", bg="#0b1a2a", wraplength=380)
label_question.pack(pady=15)

# кнопки вариантов
buttons = []
frame = tk.Frame(root, bg="#0b1a2a")
frame.pack()

for i in range(4):
    btn = tk.Button(
        frame,
        text="",
        width=15,
        bg="#1f6aa5",
        fg="white",
        command=lambda i=i: check_answer(buttons[i].cget("text").lower())
    )
    btn.grid(row=i//2, column=i%2, padx=5, pady=5)
    buttons.append(btn)

label_feedback = tk.Label(root, text="", font=("Arial", 12), bg="#0b1a2a")
label_feedback.pack(pady=5)

label_score = tk.Label(root, text="Score: 0", fg="white", bg="#0b1a2a")
label_score.pack()

label_lives = tk.Label(root, text="Lives: 3", fg="white", bg="#0b1a2a")
label_lives.pack()

btn_restart = tk.Button(root, text="🔄 Restart", command=restart_game, bg="#28a745", fg="white")

# старт
next_question()

root.mainloop()