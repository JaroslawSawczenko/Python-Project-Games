def check(num):
    try:
        num = int(num)
        if num not in range(1, 14):
            raise Exception("Taki numer nie istnieje w menu :(")
    except ValueError:
        print("To nie jest liczba.")
        return None
    except Exception as e:
        print(e)
        return None
    else:
        return num

def run():
    print("Welcome! Tutaj możesz zagrać w gry różnych gatunków."
          "\nProszę, wpisz numer na klawiaturze, aby wybrać to, co Cię interesuje.")

    while True:
        print("""
        --- Menu ---
        
        Rodzaje gier
        1. Logiczne i strategiczne
        2. Słowne
        3. Karciane
        4. Liczbowe/matematyczne
        5. Losowe/hazardowe
        6. Strategiczne
        7. Gry tekstowe RPG
        8. Symulacyjne
        9. Wieloosobowe
        10. Zręcznościowe
        11. Edukacyjne
        12. Puzzle
        
        13. Zakończyć
        """)
        user_choose = input("Wpisz numer z menu: ")
        user_choose = check(user_choose)

        if user_choose == 1:
            pass
        if user_choose == 2:
            pass
        if user_choose == 3:
            pass
        if user_choose == 4:
            pass
        if user_choose == 5:
            pass
        if user_choose == 6:
            pass
        if user_choose == 7:
            pass
        if user_choose == 8:
            pass
        if user_choose == 9:
            pass
        if user_choose == 10:
            pass
        if user_choose == 11:
            pass
        if user_choose == 12:
            pass
        if user_choose == 13:
            break

    print("Dzięki, pa!")