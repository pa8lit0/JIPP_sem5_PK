# Utwórz zmienne "vowels" (samogłoski) i "consonants" (spółgłoski) i przypisz każdej z nich wartość 0
vowels = 0
consonants = 0

text = "Programowanie Pythona"

# Utwórz pętlę i przeiteruj łańcuch znaków „Programowanie Pythona”
for char in text.lower():
    # Utwórz instrukcję warunkową IF-ELSE, która wyliczy liczbę samogłosek i spółgłosek
    if char in "aeiouyąęó":
        vowels += 1
    elif char.isalpha():
        consonants += 1

# Wydrukuj łączną liczbę samogłosek i spółgłosek w danym łańcuchu znaków
print("Liczba samogłosek:", vowels)
print("Liczba spółgłosek:", consonants)