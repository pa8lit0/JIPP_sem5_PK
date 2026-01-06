# Użyj modułu random
import random

# Stwórz listę "questions" składającą się z 3 pytań, które często zadają dzieci
questions = [
    "Why is the sky blue?\n",
    "Why is the sun round?\n",
    "Where are all the dinosaurs?\n"
]

# Pętla działa dopóki użytkownik nie wpisze hasła „to wszystko”
while True:
    # Wybierz losowe pytanie z danej listy
    question = random.choice(questions)

    # Zadaj wybrane pytanie
    answer = input(question).strip().lower()

    # Poczekaj do czasu, aż użytkownik wprowadzi hasło „to wszystko”
    if answer == "to wszystko":
        print("Dobrze, już nie pytam.")
        break
    else:
        print("Dlaczego?")
