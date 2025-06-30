import random

WORDS = [
    "skarb", "piesi", "drzewo", "żabka", "koszt", "szklany", "karta",
    "rzeka", "mucha", "koala", "zegar", "miasto", "lampa", "czapa",
    "lódka", "ciastko", "kwiat", "grupa", "kotki", "krzesło", "rowerek",
    "zabawka", "ogródek", "samolot", "ogłoszenie", "komputer", "człowiek",
    "przyjaciel", "telewizor", "szkoła", "uczelnia", "zabawa", "deszcz",
    "śnieg", "herbata", "książka", "piosenka", "muzyka", "zakupy"
]

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


class Wordle:
    def __init__(self, result = 0):
        self.word = random.choice(WORDS)
        self.result = result
    
    def change_word(self, length):
        pass

    def start(self):
        pass



# Start the game and return result
def wordle() -> int:

    result = 0
    print("""
    ===========================
    Witaj w grze Wordle!
    ===========================
    """)

    while True:
        session = Wordle()
        print("""
    --- Menu ---
    1. Rozpocznij grę (losowe słowo)
    2. Wybierz długość słowa
              
    0. Opuść grę
    """)
        
        user_choice = input("Wybrano: ").strip()
        user_choice = check_menu_choice(user_choice, 2)

        if user_choice == 1:
            pass
        elif user_choice == 2:
            pass
        elif user_choice == 0:
            break


    return result




if __name__ == "__main__":
    wordle()