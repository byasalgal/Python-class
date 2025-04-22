import random

class FruitQuiz:
    def __init__(self):
        self.fruits = {
            'apple': 'red',
            'banana': 'yellow',
            'grape': 'purple',
            'orange': 'orange',
            'lemon': 'yellow'
        }

    def start_quiz(self):
        fruit = random.choice(list(self.fruits.keys()))
        print("what is the color of " + fruit + "?")
        answer = input("enter the color: ")

        if answer.lower() == self.fruits[fruit]:
            print("correct!")
        else:
            print("wrong! The color of " + fruit + " is " + self.fruits[fruit] + ".")

quiz = FruitQuiz()
quiz.start_quiz()