"""
#Importing Specific Functions -> (from module_name import function_name)
import index
#HERE, we are importing the WHOLE MODULE of "index.py" and calling the FUNCTION of that module (make_pizza) by the prefixing the module name such as INDEX
index.make_pizza(25, "pepperoni")
index.make_pizza(30, "red chillies")

#Using as to Give a Function an Alias -> Here we give the function make_pizza() an alias, mp(), by importing "make_pizza as mp"
from index import make_pizza as mp
mp(25, 'pepperoni')
mp(35, 'extra cheese')

#HERE, as well, we are using Using as to Give a Module an Alias -> You can also provide an alias for a module name. Giving a module a short alias, like p for pizza, allows you to call the module’s functions more quickly. Calling p.make_pizza() is more concise than calling "pizza.make_pizza()""
import index as p
p.make_pizza(25, 'pepperoni')
p.make_pizza(35, 'extra cheese')

#Importing All Functions in a Module
from index import *
make_pizza(16, 'pepperoni')
"""
#Styling Functions - Functions should have descriptive names, and these names should use lowercase letters and underscores
#def function_name(
#    parameter_0, parameter_1, parameter_2,
#    parameter_3, parameter_4, parameter_5):
#function body
#ALL TYPES OF "Imports"
"""
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *

from index import Car #HERE, we are importing the CLASS and calling the FUNCTIONS in a new FILE
my_NewCar = Car("BMW i3 40L iSport", "BMW", 2025)
print(my_NewCar.get_info())
my_NewCar.read_odometer()
my_NewCar.odometer_reading = 139000
print("\nNow, the UPDATED odometer 2nd time!")
my_NewCar.updated_odometer(140000)
my_NewCar.read_odometer()

from index import ElectricCar #HERE, we are importing the CLASS(CHILD CLASS) allocated to the PARENT CLASS in one file and calling the FUNCTIONS in a new file
my_tesla = ElectricCar('Tesla', 'Model Y', 2023)
print(my_tesla.get_name())
my_tesla.describe_battery()

#Importing Multiple Classes from a Module
from index import Car, ElectricCar #HERE, we are importing both/multiple PARENT CLASS and CHILD CLASS at the same time
my_tesla = ElectricCar('Tesla', 'Model Y', 2023)
print(my_tesla.get_name())
my_tesla.describe_battery()

#Importing the Entire Module
import index
my_tesla = index.ElectricCar('Tesla', 'Model Y', 2023) #HERE, we are importing all from the FILE by adding the FILE's NAME in the FUNCTION
print(my_tesla.get_name())
my_tesla.describe_battery()

import unittest
from index import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
formatted_name = get_formatted_name(first, last)
print(f"\tNeatly formatted name: {formatted_name}.")
#We perform testing using - "Unit Tests and Test Cases" -> PASSING a TEST
class NameTestCase(unittest.TestCase):
    def Test_first_last_Names(self):
        formatted_name = get_formatted_name("Anvar", "Narzulloev")
        self.assertEqual(formatted_name, "Anvar Narzulloev")
if __name__ == '__main__':
    unittest.main()

#We perform testing using - "Unit Tests and Test Cases" -> FAILING a TEST
import unittest
from index import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
formatted_name = get_formatted_name(first, last)
print(f"\tNeatly formatted name: {formatted_name}.")
#We perform testing using - "Unit Tests and Test Cases" -> PASSING a TEST
class NameTestCase(unittest.TestCase):
    def Test_first_last_Names(self):
        formatted_name = get_formatted_name("Anvar", "Narzulloev")
        self.assertEqual(formatted_name, "Anvar Narzulloev")
if __name__ == '__main__':
    unittest.main()
"""
#We perform testing using - "Unit Tests and Test Cases" -> ADDING NEW TESTS
"""Now that we know get_formatted_name() works for simple names again, let us 
write a second test for people who include a middle name. We do this by 
adding another method to the class NamesTestCase:

import unittest
from index import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
formatted_name = get_formatted_name(first, last)
print(f"\tNeatly formatted name: {formatted_name}.")
#We perform testing using - "Unit Tests and Test Cases" -> PASSING a TEST
class NameTestCase(unittest.TestCase):
    def Test_first_last_Names(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
if __name__ == '__main__':
    unittest.main()
"""
#Testing a Class -> A Variety of Assert Methods - "Assert Methods Available from the unittest Module"
"""
assertEqual(a, b)       | Verify that a == b
assertNotEqual(a, b)    | Verify that a != b
assertTrue(x)           | Verify that x is True
assertFalse(x)          | Verify that x is False
assertIn(item, list)    | Verify that item is in list
assertNotIn(item, list) | Verify that item is not in list

from index import ASurvey
# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = ASurvey(question)
# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

#Creating a Settings Class
class Settings: #A class to store all settings for Alien Invasion
    def __init__(self): #Initialize the game's settings - Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
#Adjusting the Ship’s Speed
        self.ship_speed = 1.5
"""
import tkinter as tk
import random
from PIL import Image, ImageTk
from playsound import playsound
import threading
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # для .exe
    except:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# ---------------- DATA ----------------
questions = {
    "earth": "This planet has life.",
    "mars": "Known as the red planet.",
    "jupiter": "The biggest planet.",
    "saturn": "Has beautiful rings.",
    "uranus": "Rotates sideways.",
    "neptune": "The farthest planet.",
    "mercury": "Closest to the Sun.",
    "venus": "The hottest planet.",
    "pluto": "A dwarf planet."
}

planets = list(questions.keys())

score = 0
lives = 3
correct_answer = ""
time_left = 10
timer_id = None

# ---------------- SOUND ----------------
def play_sound(file):
    def run():
        try:
            playsound(resource_path(file))
        except:
            pass
    threading.Thread(target=run, daemon=True).start()

# ---------------- IMAGE ----------------
def load_image(name):
    try:
        path = f"images/{name}.jpg"
        img = Image.open(path)
        img = img.resize((180, 180))
        return ImageTk.PhotoImage(img)
    except:
        return None

# ---------------- TIMER ----------------
def update_timer():
    global time_left, timer_id

    label_timer.config(text=f"Time: {time_left}")

    if time_left <= 0:
        check_answer(None)
        return

    time_left -= 1
    timer_id = root.after(1000, update_timer)

# ---------------- GAME ----------------
def next_question():
    global correct_answer, time_left

    correct_answer = random.choice(planets)

    # вопрос
    label_question.config(text=questions[correct_answer])

    # картинка
    img = load_image(correct_answer)
    if img:
        image_label.config(image=img)
        image_label.image = img

    # варианты
    options = [correct_answer]
    while len(options) < 4:
        choice = random.choice(planets)
        if choice not in options:
            options.append(choice)

    random.shuffle(options)

    for i in range(4):
        buttons[i].config(text=options[i].title(), state="normal")

    # таймер
    time_left = 10
    update_timer()

def check_answer(selected):
    global score, lives

    if timer_id:
        root.after_cancel(timer_id)

    for btn in buttons:
        btn.config(state="disabled")

    if selected == correct_answer:
        score += 1
        label_feedback.config(text="✅ Correct!", fg="lightgreen")
        play_sound("sounds/correct.mp3")
    else:
        lives -= 1
        label_feedback.config(
            text=f"❌ Wrong! It was {correct_answer.title()}",
            fg="red"
        )
        play_sound("sounds/wrong.mp3")

    label_score.config(text=f"Score: {score}")
    label_lives.config(text=f"Lives: {lives}")

    if lives == 0:
        game_over()
    else:
        root.after(1500, next_question)

# ---------------- SCORE SAVE ----------------
def save_highscore():
    try:
        with open("highscore.txt", "r") as f:
            high = int(f.read())
    except:
        high = 0

    if score > high:
        with open("highscore.txt", "w") as f:
            f.write(str(score))
        return score
    return high

# ---------------- GAME OVER ----------------
def game_over():
    high = save_highscore()

    label_question.config(text="💀 GAME OVER")
    label_feedback.config(text=f"Score: {score} | Highscore: {high}")
    label_timer.config(text="")

    btn_restart.pack(pady=10)

# ---------------- RESTART ----------------
def restart_game():
    global score, lives
    score = 0
    lives = 3

    label_score.config(text="Score: 0")
    label_lives.config(text="Lives: 3")
    label_feedback.config(text="")

    btn_restart.pack_forget()
    next_question()

# ---------------- GUI ----------------
root = tk.Tk()
root.title("🚀 Planet Quiz PRO")
root.geometry("500x500")
root.configure(bg="#0b1a2a")

title = tk.Label(root, text="🌌 Planet Quiz PRO", font=("Arial", 18, "bold"), fg="white", bg="#0b1a2a")
title.pack(pady=10)

label_question = tk.Label(root, text="", font=("Arial", 12), fg="white", bg="#0b1a2a", wraplength=400)
label_question.pack()

image_label = tk.Label(root, bg="#0b1a2a")
image_label.pack(pady=10)

label_timer = tk.Label(root, text="", fg="yellow", bg="#0b1a2a")
label_timer.pack()

frame = tk.Frame(root, bg="#0b1a2a")
frame.pack()

buttons = []
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

label_feedback = tk.Label(root, text="", bg="#0b1a2a")
label_feedback.pack(pady=5)

label_score = tk.Label(root, text="Score: 0", fg="white", bg="#0b1a2a")
label_score.pack()

label_lives = tk.Label(root, text="Lives: 3", fg="white", bg="#0b1a2a")
label_lives.pack()

btn_restart = tk.Button(root, text="🔄 Restart", command=restart_game, bg="#28a745", fg="white")

# старт
next_question()

root.mainloop()