import os
import sys
from pathlib import Path
from typing import Optional, Dict, Callable, Any
from .user import User

# Dodanie root directory do sys.path dla bezpiecznych importów
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

# Zunifikowane nazwy gier
GAME_NAMES = {
    1: "Kółko i krzyżyk",
    2: "2048",
    3: "Wordle", 
    4: "Zgadnij liczbę"
}

# Bezpieczne importy z lepszym error handlingiem
try:
    from games import tic_tac_toe, game_2048
    TIC_TAC_TOE_AVAILABLE = True
    GAME_2048_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Błąd importu gier strategicznych: {e}")
    TIC_TAC_TOE_AVAILABLE = False
    GAME_2048_AVAILABLE = False

try:
    from games import wordle
    WORDLE_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Błąd importu Wordle: {e}")
    WORDLE_AVAILABLE = False

try:
    from games.Guess_the_Number import GuessNumber
    GUESS_NUMBER_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Błąd importu Guess the Number: {e}")
    GUESS_NUMBER_AVAILABLE = False

def clear_screen() -> None:
    """Czyści ekran konsoli z lepszym error handlingiem"""
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except OSError as e:
        print(f"Nie można wyczyścić ekranu: {e}")
        print('\n' * 50)  # Fallback

def validate_user_name(name: str) -> bool:
    """Waliduje nazwę użytkownika"""
    name = name.strip()
    if not name:
        print("❌ Imię nie może być puste!")
        return False
    if len(name) < 2:
        print("❌ Imię musi mieć co najmniej 2 znaki!")
        return False
    if len(name) > 30:
        print("❌ Imię nie może być dłuższe niż 30 znaków!")
        return False
    if not name.replace(" ", "").replace("-", "").isalpha():
        print("❌ Imię może zawierać tylko litery, spacje i myślniki!")
        return False
    return True

def check_menu_choice(user_input: str, max_option: int) -> Optional[int]:
    """Sprawdza poprawność wyboru z menu z lepszą walidacją"""
    if not user_input or not user_input.strip():
        print("❌ Nie podano wyboru!")
        return None
        
    try:
        num = int(user_input.strip())
        if 0 <= num <= max_option:
            return num
        else:
            print(f"❌ Wybierz numer od 0 do {max_option}")
            return None
    except ValueError:
        print("❌ To nie jest liczba. Spróbuj ponownie.")
        return None
    except Exception as e:
        print(f"❌ Wystąpił nieoczekiwany błąd: {e}")
        return None

def display_main_menu() -> None:  
    """Wyświetla główne menu gry z poprawionymi nazwami"""
    print("""
    ╔══════════════════════════════════════╗
    ║            TERMINAL GAMES            ║
    ║              GŁÓWNE MENU             ║
    ╚══════════════════════════════════════╝
    
     🎮 Dostępne gry:""")
    
    games_menu = [
        (TIC_TAC_TOE_AVAILABLE, f"1.  {GAME_NAMES[1]}"),
        (GAME_2048_AVAILABLE, f"2.  {GAME_NAMES[2]}"),
        (WORDLE_AVAILABLE, f"3.  {GAME_NAMES[3]}"),
        (GUESS_NUMBER_AVAILABLE, f"4.  {GAME_NAMES[4]}")
    ]
    
    for available, text in games_menu:
        if available:
            print(f"    ✅ {text}")
        else:
            print(f"    ❌ {text} (Niedostępne)")
    
    print("""    🔮 5.  Więcej gier (Wkrótce)
    
     📊 Opcje dodatkowe:
    6.  Moje statystyki
    7.  Ranking graczy
    8.  Lista użytkowników
    9.  Pomoc
    
    0.  Wyjście""")

def display_user_stats(user: User) -> None:
    """Wyświetla statystyki użytkownika z lepszym formatowaniem"""
    print(f"""
    ╔══════════════════════════════════════╗
    ║           TWOJE STATYSTYKI           ║
    ╚══════════════════════════════════════╝
    
    👤 Gracz: {user.user_info['name']}
    🆔 ID: {user.user_info['id']}
    """)
    
    if user.user_info['results']:
        total_score = sum(user.user_info['results'].values())
        games_played = len(user.user_info['results'])
        avg_score = total_score / games_played if games_played > 0 else 0
        
        print("    🏆 Twoje najlepsze wyniki:")
        for game_name, score in user.user_info['results'].items():
            print(f"    • {game_name}: {score} pkt")
        
        print(f"\n    📈 Podsumowanie:")
        print(f"    • Zagrane gry: {games_played}")
        print(f"    • Suma punktów: {total_score}")
        print(f"    • Średnia na grę: {avg_score:.1f} pkt")
    else:
        print("    📝 Nie masz jeszcze żadnych wyników.")
        print("    🎮 Zagraj w jakąś grę, aby zapisać swoje wyniki!")

def display_all_users() -> None:
    """Wyświetla listę wszystkich użytkowników z lepszym formatowaniem"""
    from .user import read_data_user_json
    
    try:
        data = read_data_user_json()
    except Exception as e:
        print(f"❌ Błąd podczas odczytu danych użytkowników: {e}")
        return
    
    print("""
    ╔══════════════════════════════════════╗
    ║         LISTA UŻYTKOWNIKÓW           ║
    ╚══════════════════════════════════════╝
    """)
    
    if not data:
        print("    📝 Brak zarejestrowanych użytkowników.")
        return
    
    print(f"    👥 Znaleziono {len(data)} użytkowników:\n")
    
    for user in data:
        total_score = sum(user.get('results', {}).values())
        games_count = len(user.get('results', {}))
        
        print(f"    🆔 ID: {user['id']} | 👤 Imię: {user['name']}")
        if user.get('results'):
            print(f"      🎮 Zagrane gry: {games_count} | 🏆 Suma punktów: {total_score}")
        else:
            print("      📝 Brak wyników")
        print()

def display_help() -> None:
    """Wyświetla pomoc dla użytkownika z dodatkowymi informacjami"""
    print("""
    ╔══════════════════════════════════════╗
    ║               POMOC                  ║
    ╚══════════════════════════════════════╝
    
     🎮 Jak grać:
    • Wybierz grę z menu głównego (1-4)
    • Postępuj zgodnie z instrukcjami w grze
    • Twoje wyniki są automatycznie zapisywane
    • Zapisywane są tylko najlepsze wyniki z każdej gry

     🏆 System punktów:
    • Kółko i krzyżyk: 100-180 pkt (mniej ruchów = więcej punktów)
    • 2048: Punkty za połączone kafelki
    • Wordle: 1-10 pkt (mniej prób = więcej punktów)  
    • Zgadnij liczbę: 100-300+ pkt (poziom + efektywność)
    
     ⌨️ Nawigacja:
    • Używaj numerów do wyboru opcji
    • Wpisz '0' aby wrócić do menu głównego
    • Wpisz 'q' w grach aby je opuścić
    
     💡 Wskazówki:
    • Regularnie sprawdzaj swoje statystyki (opcja 6)
    • Każda gra ma swoje unikalne zasady
    • Próbuj pobić swoje rekordy!
    • Gry są zapisywane automatycznie
    """)

def get_user_name() -> str:
    """Pobiera i waliduje nazwę użytkownika"""
    while True:
        user_name = input("\n 👤 Proszę podać swoje imię (2-30 znaków): ").strip()
        if validate_user_name(user_name):
            return user_name

def handle_game_result(game_name: str, result: Any, user: User) -> None:
    """Obsługuje wynik gry z lepszą walidacją"""
    if result is None:
        print(f"    🚫 Gra {game_name} została przerwana")
        return
        
    if not isinstance(result, (int, float)) or result < 0:
        print(f"    ❌ Nieprawidłowy wynik dla gry {game_name}: {result}")
        return
        
    if result == 0:
        print(f"    📝 Brak punktów do zapisania dla gry {game_name}")
        return
        
    try:
        success = user.add_results(game_name, result)
        if not success:
            print(f"    ⚠️ Nie udało się zapisać wyniku dla gry {game_name}")
    except Exception as e:
        print(f"    ❌ Błąd podczas zapisywania wyniku: {e}")

def handle_2048_game() -> Optional[int]:
    """Specjalna obsługa gry 2048 z error handlingiem"""
    try:
        game = game_2048.Game2048()
        game.play()
        return game.score if hasattr(game, 'score') else 0
    except Exception as e:
        print(f"❌ Błąd w grze 2048: {e}")
        return None

def run() -> None:
    """Główna funkcja menu z ulepszoną obsługą błędów"""
    clear_screen()
    
    print(" 🎮 Witaj w Terminal Games! ")
    print("Tutaj możesz zagrać w różne gry i rywalizować z innymi!")
    
    # Pobierz dane użytkownika z walidacją
    user_name = get_user_name()
    
    try:
        user = User()
        user = user.create_user(user_name)
    except Exception as e:
        print(f"❌ Błąd podczas tworzenia/ładowania użytkownika: {e}")
        input("Naciśnij Enter aby zakończyć...")
        return
    
    # Definicja handlerów gier
    game_handlers: Dict[int, Dict[str, Any]] = {
        1: {
            "name": GAME_NAMES[1], 
            "available": TIC_TAC_TOE_AVAILABLE, 
            "function": lambda: tic_tac_toe.tic_tac_toe()
        },
        2: {
            "name": GAME_NAMES[2], 
            "available": GAME_2048_AVAILABLE, 
            "function": handle_2048_game
        },
        3: {
            "name": GAME_NAMES[3], 
            "available": WORDLE_AVAILABLE, 
            "function": lambda: wordle.wordle()
        },
        4: {
            "name": GAME_NAMES[4], 
            "available": GUESS_NUMBER_AVAILABLE, 
            "function": lambda: GuessNumber().play()
        }
    }
    
    while True:
        clear_screen()
        print(f" 👋 Cześć, {user.user_info['name']}!")
        display_main_menu()
        
        user_choice = input(" 🎯 Wybierz opcję: ").strip()
        choice = check_menu_choice(user_choice, 9)
        
        if choice is None:
            input("⏎ Naciśnij Enter aby kontynuować...")
            continue
        
        # Obsługa gier (1-4)
        if choice in game_handlers:
            handler = game_handlers[choice]
            game_name = handler["name"]
            
            if handler["available"]:
                print(f" 🎮 Uruchamianie {game_name}...")
                try:
                    result = handler["function"]()
                    handle_game_result(game_name, result, user)
                except Exception as e:
                    print(f" ❌ Błąd podczas uruchamiania gry {game_name}: {e}")
            else:
                print(f" ❌ {game_name} nie jest dostępne!")
                
        # Pozostałe opcje menu
        elif choice == 5:
            print(" 🔮 Więcej gier będzie dostępne wkrótce!")
            print(" 💡 Sugestie: Snake, Tetris, Sudoku...")
        elif choice == 6:
            display_user_stats(user)
        elif choice == 7:
            print(" 🏆 Globalny ranking graczy w budowie!")
            print(" 📊 Wkrótce będziesz mógł porównać się z innymi!")
        elif choice == 8:
            display_all_users()
        elif choice == 9:
            display_help()
        elif choice == 0:
            print(" 👋 Dziękujemy za grę! Do zobaczenia!")
            break
        
        if choice != 0:
            input("\n ⏎ Naciśnij Enter aby kontynuować...")

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\n\n 👋 Gra przerwana przez użytkownika. Do zobaczenia!")
    except Exception as e:
        print(f"\n\n ❌ Nieoczekiwany błąd: {e}")
        input("Naciśnij Enter aby zakończyć...")