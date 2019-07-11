from random import choice

questions = ["Why was Prince Hans mean?", "Why Anna punch him?", "Why did Elsa run away?"]

question = choice(questions)

answer = input(question).strip().lower

while answer !="just because":
  answer = input("but.. why? ").strip().lower()

print("Oh.. Okay")