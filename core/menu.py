def check(num):
    try:
        num = int(num)
        if num not in range(0, 11):
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
        1. Tic-tac-toe
        2. 2048
        3. 
        4. 
        5. 
        6. 
        7. 
        8. 
        9. 
        10. 
        
        0. Zakończyć
        """)
        user_choice = input("Wpisz numer z menu: ")
        user_choice = check(user_choice)

        if user_choice == 1:
            pass
        if user_choice == 2:
            pass
        if user_choice == 3:
            pass
        if user_choice == 4:
            pass
        if user_choice == 5:
            pass
        if user_choice == 6:
            pass
        if user_choice == 7:
            pass
        if user_choice == 8:
            pass
        if user_choice == 9:
            pass
        if user_choice == 10:
            pass
        if user_choice == 11:
            pass
        if user_choice == 12:
            pass
        if user_choice == 0:
            break

    print("Dzięki, pa!")