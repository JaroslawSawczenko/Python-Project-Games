import os
from .user import User

try:
    from games import tic_tac_toe, game_2048
    TIC_TAC_TOE_AVAILABLE = True
    GAME_2048_AVAILABLE = True
except ImportError:
    TIC_TAC_TOE_AVAILABLE = False
    GAME_2048_AVAILABLE = False

try:
    from games import wordle
    WORDLE_AVAILABLE = True
except ImportError:
    WORDLE_AVAILABLE = False

try:
    from games import Guess_the_Number
    GUESS_NUMBER_AVAILABLE = True
except ImportError:
    GUESS_NUMBER_AVAILABLE = False

def clear_screen():
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
    
     Dostępne gry:""")
    
    if TIC_TAC_TOE_AVAILABLE:
        print("    1.  Tic-tac-toe (Kółko i krzyżyk)")
    else:
        print("    1.  Tic-tac-toe (Niedostępne)")
        
    if GAME_2048_AVAILABLE:
        print("    2.  2048 (Gra liczbowa)")
    else:
        print("    2.  2048 (Niedostępne)")
        
    if WORDLE_AVAILABLE:
        print("    3.  Wordle")
    else:
        print("    3.  Wordle (Niedostępne)")
    
    if GUESS_NUMBER_AVAILABLE:
        print("    4.  Zgadnij liczbę")
    else:
        print("    4.  Zgadnij liczbę (Niedostępne)")
        
    print("""    5.  Więcej gier (Wkrótce)
    
     Opcje dodatkowe:
    6.  Moje statystyki
    7.  Ranking graczy
    8.  Lista użytkowników
    9.  Pomoc
    
    0.  Wyjście
    """)

def display_user_stats(user):
    """Wyświetla statystyki użytkownika"""
    print(f"""
    ╔══════════════════════════════════════╗
    ║           TWOJE STATYSTYKI           ║
    ╚══════════════════════════════════════╝
    
    Gracz: {user.user_info['name']}
    ID: {user.user_info['id']}
    """)
    
    if user.user_info['results']:
        print("    Twoje najlepsze wyniki:")
        for game_name, score in user.user_info['results'].items():
            print(f"    • {game_name}: {score} pkt")
    else:
        print("    Nie masz jeszcze żadnych wyników.")
        print("    Zagraj w jakąś grę, aby zapisać swoje wyniki!")

def display_all_users():
    """Wyświetla listę wszystkich użytkowników"""
    from .user import read_data_user_json
    
    data = read_data_user_json()
    
    print("""
    ╔══════════════════════════════════════╗
    ║         LISTA UŻYTKOWNIKÓW           ║
    ╚══════════════════════════════════════╝
    """)
    
    if not data:
        print("    Brak zarejestrowanych użytkowników.")
        return
    
    for user in data:
        print(f"    ID: {user['id']} | Imię: {user['name']}")
        if user['results']:
            print(f"      Gry zagrane: {len(user['results'])}")
        else:
            print("      Brak wyników")
        print()

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
        print(" Imię nie może być puste!")
    
    # Utwórz lub załaduj użytkownika
    user = User()
    user = user.create_user(user_name)
    
    # Główna pętla menu
    while True:
        clear_screen()
        print(f" Cześć, {user.user_info['name']}!")
        display_main_menu()
        
        user_choice = input(" Wybierz opcję: ").strip()
        choice = check_menu_choice(user_choice, 9)
        
        if choice is None:
            input("⏎ Naciśnij Enter aby kontynuować...")
            continue
        
        if choice == 1:
            if TIC_TAC_TOE_AVAILABLE:
                print(" Uruchamianie Tic-Tac-Toe...")
                try:
                    result = tic_tac_toe.tic_tac_toe()
                    if result and result > 0:
                        user.add_results("Tic-Tac-Toe", result)
                except Exception as e:
                    print(f" Błąd podczas uruchamiania gry: {e}")
            else:
                print(" Tic-Tac-Toe nie jest dostępne!")
                
        elif choice == 2:
            if GAME_2048_AVAILABLE:
                print(" Uruchamianie 2048...")
                try:
                    game = game_2048.Game2048()
                    game.play()
                    if game.score > 0:
                        user.add_results("2048", game.score)
                except Exception as e:
                    print(f" Błąd podczas uruchamiania gry: {e}")
            else:
                print(" Gra 2048 nie jest dostępna!")
                
        elif choice == 3:
            if WORDLE_AVAILABLE:
                print(" Uruchamianie Wordle...")
                try:
                    result = wordle.wordle()
                    if result and result > 0:
                        user.add_results("Wordle", result)
                except Exception as e:
                    print(f" Błąd podczas uruchamiania gry: {e}")
            else:
                print(" Wordle nie jest dostępne!")
                
        elif choice == 4:
            if GUESS_NUMBER_AVAILABLE:
                print(" Uruchamianie Zgadnij liczbę...")
                try:
                    game = Guess_the_Number.GuessNumber()
                    result = game.play()
                    if result and result > 0:
                        user.add_results("Zgadnij liczbę", result)
                except Exception as e:
                    print(f" Błąd podczas uruchamiania gry: {e}")
            else:
                print(" Zgadnij liczbę nie jest dostępne!")
                
        elif choice == 5:
            print(" Wkrótce dostępne!")
        elif choice == 6:
            display_user_stats(user)
        elif choice == 7:
           print(" Ranking graczy w budowie!")
        elif choice == 8:
            display_all_users()
        elif choice == 9:
            display_help()
        elif choice == 0:
            break
        
        if choice != 0:
            input("\n Naciśnij Enter aby kontynuować...")

# if __name__ == "__main__":
#     run()