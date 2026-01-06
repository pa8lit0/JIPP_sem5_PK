# Zapytaj użytkownika o nazwisko
name = input("What is your name?: ")

# Zapytaj użytkownika o wiek
age = input("How old are you?: ")

# Zapytaj użytkownika o miasto
city = input("Where do you live?: ")

# Zapytaj użytkownika o jego zainteresowania
interest = input("What do you love?: ")

# Utwórz tekst wyjściowy za pomocą formatowania ciągów
string = "Hi {}, you are {} years old. You live in {} and you love {}!"
output = string.format(name, age, city, interest)

# Wydrukuj tekst wyjściowy
print(output)
