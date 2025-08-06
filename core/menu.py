import os
from .user import User

try:
    from games import tic_tac_toe, game_2048
    TIC_TAC_TOE_AVAILABLE = True
    GAME_2048_AVAILABLE = True
except ImportError as e:
    print(f"Błąd importu gier strategicznych: {e}")
    TIC_TAC_TOE_AVAILABLE = False
    GAME_2048_AVAILABLE = False

try:
    from games import wordle
    WORDLE_AVAILABLE = True
except ImportError as e:
    print(f"Błąd importu Wordle: {e}")
    WORDLE_AVAILABLE = False

try:
    from games.Guess_the_Number import GuessNumber
    GUESS_NUMBER_AVAILABLE = True
except ImportError as e:
    print(f"Błąd importu Guess the Number: {e}")
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
    
    # Konsystentne nazewnictwo i obsługa wszystkich gier
    games_menu = [
        (TIC_TAC_TOE_AVAILABLE, "1.  Tic-Tac-Toe (Kółko i krzyżyk)"),
        (GAME_2048_AVAILABLE, "2.  2048 (Gra liczbowa)"),
        (WORDLE_AVAILABLE, "3.  Wordle (Zgadywanie słów)"),
        (GUESS_NUMBER_AVAILABLE, "4.  Zgadnij liczbę")
    ]
    
    for available, text in games_menu:
        if available:
            print(f"    {text}")
        else:
            print(f"    {text} (Niedostępne)")
    
    print("""    5.  Więcej gier (Wkrótce)
    
     Opcje dodatkowe:
    6.  Moje statystyki
    7.  Ranking graczy
    8.  Lista użytkowników
    9.  Pomoc
    
    0.  Wyjście""")

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
    
    user = User()
    user = user.create_user(user_name)
    
    while True:
        clear_screen()
        print(f" Cześć, {user.user_info['name']}!")
        display_main_menu()
        
        user_choice = input(" Wybierz opcję: ").strip()
        choice = check_menu_choice(user_choice, 9)
        
        if choice is None:
            input("⏎ Naciśnij Enter aby kontynuować...")
            continue
        
        game_handlers = {
            1: ("Tic-Tac-Toe", TIC_TAC_TOE_AVAILABLE, lambda: tic_tac_toe.tic_tac_toe()),
            2: ("2048", GAME_2048_AVAILABLE, lambda: handle_2048_game()),
            3: ("Wordle", WORDLE_AVAILABLE, lambda: wordle.wordle()),
            4: ("Zgadnij liczbę", GUESS_NUMBER_AVAILABLE, lambda: GuessNumber().play())
        }
        
        if choice in game_handlers:
            game_name, available, game_func = game_handlers[choice]
            
            if available:
                print(f" Uruchamianie {game_name}...")
                try:
                    result = game_func()
                    if result and result > 0:
                        user.add_results(game_name, result)
                    else:
                        print(f" Nie zapisano wyniku dla gry {game_name}")
                except Exception as e:
                    print(f" Błąd podczas uruchamiania gry {game_name}: {e}")
            else:
                print(f" {game_name} nie jest dostępne!")
                
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
            print(" Dziękujemy za grę! Do zobaczenia!")
            break
        
        if choice != 0:
            input("\n Naciśnij Enter aby kontynuować...")

def handle_2048_game():
    """Specjalna obsługa gry 2048"""
    game = game_2048.Game2048()
    game.play()
    return game.score

# if __name__ == "__main__":
#     run()