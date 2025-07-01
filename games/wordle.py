import random
from collections import Counter

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
    def __init__(self, points = 0):
        self.word = random.choice(WORDS).upper()
        self.points = points
    
    def change_word(self):
        print("🎲 Wybierz długość słowa od 5 do 10:")
        length_str = input("👉 Długość słowa: ").strip()
        try:
            length = int(length_str)
            if length not in range(5, 11):
                print("⚠️ Tylko liczby od 5 do 10, spróbuj jeszcze raz!")
                return
            filtered = [w for w in WORDS if len(w) == length]
            if not filtered:
                print("⚠️ Brak słów o takiej długości!")
                return
            self.word = random.choice(filtered).upper()
            print(f"✅ Super! Wybrałem słowo o długości {length}.")
        except ValueError:
            print("⚠️ To nie jest liczba! Spróbuj ponownie.")


    def start(self):
        attempts = 0
        length = len(self.word)
        word_letters = list(self.word)
        print(f"🔎 Zgadnij słowo składające się z {length} liter! (Wpisz 'quit' aby wyjść)")

        while True:
            print("_ " * length)
            guess = input("👉 Twoje słowo: ").strip().upper()

            if guess.lower() == "quit":
                print("🛑 Uciekasz? Do zobaczenia przy następnej rozgrywce!")
                break

            if not guess.isalpha():
                print("⚠️ Proszę, wpisz tylko litery! Spróbuj jeszcze raz.")
                continue

            if len(guess) != length:
                print(f"⚠️ Słowo musi mieć dokładnie {length} liter, spróbuj jeszcze raz.")
                continue

            attempts += 1
            guess_letters = list(guess)

            if guess == self.word:
                print(f"🎉 Brawo! Odgadłeś słowo w {attempts} próbach!")
                if attempts <= 5:
                    self.points += 10
                    print("🔥 Mistrzowska robota! +10 punktów!")
                elif attempts <= 10:
                    self.points += 5
                    print("👍 Dobra robota! +5 punktów!")
                else:
                    self.points += 1
                    print("🙂 Udało się! +1 punkt!")
                self.word = random.choice(WORDS).upper()
                return self.points

            # Sprawdzanie liter na właściwych miejscach i obecności liter w słowie
            right_place = {i: letter for i, letter in enumerate(word_letters) if letter == guess_letters[i]}
            c_word = Counter(word_letters)
            c_guess = Counter(guess_letters)
            right_letters = {letter: min(c_word.get(letter, 0), c_guess.get(letter, 0)) for letter in c_guess}

            # Wyświetlanie podpowiedzi
            print("✅ Litery na właściwych miejscach:", end=" ")
            for i in range(length):
                print(right_place.get(i, "_"), end=" ")
            print()

            print("🔸 Litery obecne w słowie:", end=" ")
            for letter, count in right_letters.items():
                print(f"{letter} " * count, end="")
            print("\n")



# Start the game and return result
def wordle() -> int:
    session = Wordle()
    print("""
    ===========================
    Witaj w grze Wordle!
    ===========================
    """)

    while True:
        # print(session.word)
        print("""
    --- Menu ---
    1. Rozpocznij grę (losowe słowo)
    2. Wybierz długość słowa
              
    0. Opuść grę
    """)
        
        user_choice = input("Wybrano: ").strip()
        user_choice = check_menu_choice(user_choice, 2)

        if user_choice == 1:
            session.start()
            print(f"🌟 Twoje punkty: {session.points}\n")
        elif user_choice == 2:
            # print(session.word)
            session.change_word()
            # print(session.word)
        elif user_choice == 0:
            print("👋 Dzięki za grę! Do zobaczenia!")
            break

    return session.points


# if __name__ == "__main__":
#     print("Points:", wordle())