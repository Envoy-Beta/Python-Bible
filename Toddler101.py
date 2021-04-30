from random import choice

questions = [
    "Why is the sky blue?: ", 
    "Why do I have to go to sleep?: ", 
    "Why does it rain?: ", 
    "Why can't I have ice cream for dinner?: "
    ]

question = choice(questions)
answer = input(question).strip().capitalize()

while answer != "Just because":
    answer = input("Why?: ").strip().capitalize()

print("Oh...okay.")