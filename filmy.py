# Utwórz słownik filmów. Niech kluczem będzie nazwa filmu, a parą wartości dwie liczby:
# kryteria wiekowe oraz liczba dostępnych biletów
movies = {
    "Finding Nemo": [5, 2],
    "Moana": [6, 3],
    "Batman": [18, 5],
    "The Lion King": [10, 4]
}

# Utwórz pętlę, która będzie działać w nieskończoność
while True:
    # Pobierz tytuł filmu od użytkownika, usuń spacje z początku i końca
    # a następnie zamień frazę na format tytułowy (pierwsza litera każdego słowa jest wielka)
    title = input("Podaj tytuł filmu (lub 'koniec' aby zakończyć): ").strip().title()

    if title == "Koniec":
        print("Zakończono.")
        break

    # Sprawdź, czy film istnieje w słowniku
    if title in movies:
        # Zapytaj użytkownika o wiek
        try:
            age = int(input("Podaj swój wiek: ").strip())
        except ValueError:
            print("Błąd: wiek musi być liczbą.")
            continue

        # Pobierz wymagany wiek i liczbę biletów
        required_age = movies[title][0]
        tickets = movies[title][1]

        # Sprawdź użytkownika pod kątem kwalifikowalności
        if age >= required_age:
            # Sprawdź dostępność miejsc
            if tickets > 0:
                movies[title][1] -= 1
                print(f"Bilet kupiony. Pozostało biletów na '{title}': {movies[title][1]}")
            else:
                print(f"Brak biletów na film '{title}'.")
        else:
            print(f"Nie spełniasz kryterium wiekowego. Film '{title}' jest od {required_age} lat.")
    else:
        print("Nie ma takiego filmu w repertuarze.")
        print("Dostępne filmy:")
        for m in movies:
            print("-", m)
