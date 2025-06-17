def check(num):
    try:
        num = int(num)
        if num not in range(0, 13):
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
        2. 
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
        if user_choose == 0:
            break

    print("Dzięki, pa!")