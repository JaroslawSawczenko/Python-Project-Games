import os
#from .user import User, create_or_load_user
#from ..games.logic_strategy import tic_tac_toe, game_2048

def clear_screen(): git commit -m "poprawa funkcji obsluga błędów"
    """Czyści ekran konsoli"""
    os.system('cls' if os.name == 'nt' else 'clear')

def check_menu_choice(user_input, max_option):
    """Sprawdza poprawność wyboru z menu"""
    try:
        num = int(user_input)
        if 0 <= num <= max_option:
            return num
        else:
            print(f"Wybierz numer od 0 do {max_option}")
            return None
    except ValueError:
        print("To nie jest liczba. Spróbuj ponownie.")
        return None
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")
       return None


def display_main_menu():  
    """Wyświetla główne menu gry"""
    print("""
    ╔══════════════════════════════════════╗
    ║            TERMINAL GAMES            ║
    ║              GŁÓWNE MENU             ║
    ╚══════════════════════════════════════╝
    
     Dostępne gry:
    1.  Tic-tac-toe (Kółko i krzyżyk)
    2.  2048 (Gra liczbowa)
    3.  (Wkrótce)
    4.  (Wkrótce)
    5.  Więcej gier (Wkrótce)
    
     Opcje dodatkowe:
    6.  Moje statystyki
    7.  Ranking graczy       
    8.  Lista użytkowników
    9.  Pomoc
    
    0.  Wyjście
    """)




def display_help():
    """Wyświetla pomoc dla użytkownika"""
    print("""
    ╔══════════════════════════════════════╗
    ║               POMOC                  ║
    ╚══════════════════════════════════════╝
    
     Jak grać:
    • Wybierz grę z menu głównego
    • Postępuj zgodnie z instrukcjami w grze
    • Twoje wyniki są automatycznie zapisywane

     System punktów:
    • Każda gra ma swój system punktacji
    • Zapisywane są tylko najlepsze wyniki
    • Możesz sprawdzić swoje statystyki w menu
    
     Nawigacja:
    • Używaj numerów do wyboru opcji
    • Wpisz '0' aby wrócić do menu głównego
    • Wpisz 'q' w grach aby je opuścić
    
     Wskazówki:
    • Regularnie sprawdzaj ranking
    • Próbuj pobić swoje rekordy
    • Każda gra ma swoje unikalne zasady
    """)

def run():
    """Główna funkcja menu"""
    clear_screen()
    
    print(" Witaj w Terminal Games! ")
    print("Tutaj możesz zagrać w różne gry i rywalizować z innymi!")
    
    # Pobierz dane użytkownika
    while True:
        user_name = input("\n Proszę podać swoje imię: ").strip()
        if user_name:
            break
        print("Imię nie może być puste!")
    
    # Utwórz lub załaduj użytkownika
    user = create_or_load_user(user_name)
    
    # Główna pętla menu
    while True:
        clear_screen()
        print(f" Cześć, {user.user_info['name']}!")
        display_main_menu()
        
        user_choice = input(" Wybierz opcję: ").strip()
        choice = check_menu_choice(user_choice, 9)
        
        if choice is None:
            input("Naciśnij Enter aby kontynuować...")
            continue
        
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            print("  Wkrótce dostępne!")
        elif choice == 4:
            print(" - Wkrótce dostępne!")
        elif choice == 5:
            print(" - Wkrótce dostępne!")
        elif choice == 9:
            display_help()
        
        if choice != 0:
            input("\nNaciśnij Enter aby kontynuować...")

if __name__ == "__main__":
    run()