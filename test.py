"""
import unittest
from index import ASurvey

class TestASurvey(unittest.TestCase):
    def test_store_response(self):
        question = "What language did you first learn to speak?"
        my_survey = ASurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
if __name__ == '__main__':
    unittest.main()

#The setUp() method -> a setUp() method that allows you to create these objects once and then use them in each of your test methods
import unittest
from index import ASurvey
class TestASurvey(unittest.TestCase):
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = ASurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    def test_store_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
if __name__ == '__main__':
 unittest.main()

#Creating the Ship Class
import pygame
class Ship: #A class to manage the ship
    def __init__(self, ai_game): #Initialize the ship and set its starting position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom #Start each new ship at the bottom center of the screen. Allowing Continuous Movement
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
    def update(self): #Moving Both Left and Right
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
    def blitme(self): #Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
"""
#print("Hello reload function!")
# import os
# def current_directory():
#     contents = os.listdir(r'C:\Users\ANarzulloev\OneDrive - beeline.uz\Рабочий стол\LearnPython\alien_invasion.py')
#     print("This is the display of the current directory: ")
#     print(contents)
# import index
# import pytest

# def test_add():
#     assert True
#     assert index.add(4, 5) == 9
    
# def test_sub():
#     pass
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

score = 0
lives = 3
current_answer = ""

# Новый вопрос
def next_question():
    global current_answer

    current_answer = random.choice(list(questions.keys()))
    label_question.config(text=questions[current_answer])
    entry.delete(0, tk.END)
    label_feedback.config(text="")

# Проверка ответа
def check_answer():
    global score, lives

    user_answer = entry.get().strip().lower()

    if not user_answer:
        label_feedback.config(text="⚠️ Enter something!", fg="yellow")
        return

    if user_answer == current_answer:
        score += 1
        label_feedback.config(text="✅ Correct!", fg="lightgreen")
    else:
        lives -= 1
        label_feedback.config(
            text=f"❌ Wrong! It was {current_answer.title()}",
            fg="red"
        )

    label_score.config(text=f"Score: {score}")
    label_lives.config(text=f"Lives: {lives}")

    if lives == 0:
        game_over()
    else:
        root.after(1500, next_question)

# Game Over
def game_over():
    label_question.config(text="💀 GAME OVER")
    label_feedback.config(text=f"Final Score: {score}", fg="white")
    entry.config(state="disabled")
    btn_submit.config(state="disabled")
    btn_restart.pack(pady=10)

# Рестарт
def restart_game():
    global score, lives
    score = 0
    lives = 3

    label_score.config(text="Score: 0")
    label_lives.config(text="Lives: 3")

    entry.config(state="normal")
    btn_submit.config(state="normal")
    btn_restart.pack_forget()

    next_question()

# GUI
root = tk.Tk()
root.title("🎮 Guess the Planet - Level 2")
root.geometry("420x320")
root.configure(bg="#0b1a2a")

title = tk.Label(root, text="🌌 Guess the Planet", font=("Arial", 16, "bold"), fg="white", bg="#0b1a2a")
title.pack(pady=10)

label_question = tk.Label(root, text="", font=("Arial", 12), fg="white", bg="#0b1a2a", wraplength=350)
label_question.pack(pady=15)

entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack()

btn_submit = tk.Button(root, text="Submit", command=check_answer, bg="#1f6aa5", fg="white")
btn_submit.pack(pady=5)

label_feedback = tk.Label(root, text="", font=("Arial", 12), bg="#0b1a2a")
label_feedback.pack(pady=5)

label_score = tk.Label(root, text="Score: 0", font=("Arial", 12), fg="white", bg="#0b1a2a")
label_score.pack()

label_lives = tk.Label(root, text="Lives: 3", font=("Arial", 12), fg="white", bg="#0b1a2a")
label_lives.pack()

# Кнопка рестарта (появится только при проигрыше)
btn_restart = tk.Button(root, text="🔄 Restart", command=restart_game, bg="#28a745", fg="white")

entry.bind("<Return>", lambda e: check_answer())

# старт
next_question()

root.mainloop()