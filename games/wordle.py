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
    def __init__(self, result = 0):
        self.word = random.choice(WORDS).upper()
        self.result = result
    
    def change_word(self):
        # WORDS.sort(key=lambda x: len(x))
        length = input("Words from 5 to 10: ").strip()
        try:
            length = int(length)
        except ValueError:
            print("To nie jest liczba. Spróbuj ponownie.")
            length = None
        if length:
            if length not in range(5, 11):
                print("Only from 5 to 10.")
                length = None
        if length:
            filtered_words = [word for word in WORDS if len(word) == length]
            self.word = random.choice(filtered_words)

    def start(self):
        points = 0
        attempts = 0
        self.word = self.word.upper()
        length = len(self.word)
        word = list(self.word)
        guessed = False
        while not guessed:
            print("_ "*length)
            user = input("Słowo: ").strip().upper()
            user_word = list(user)
            attempts += 1

            if user.lower() == "quit":
                break
            if len(user_word) != len(word):
                print("Podaj poprawną długość słowa!")
                continue
            if user == self.word.upper():
                print("Congrats! You won in {} attempts!".format(attempts))
                guessed = True

                if attempts < 5:
                    points = 10
                elif attempts < 10:
                    points = 5
                else:
                    points = 1

                self.word = random.choice(WORDS)
                return points
            else:
                right_letters = {}
                right_place = {}

                for i in range(len(word)):
                    if word[i].upper() == user_word[i].upper():
                        right_place[i] = word[i].upper()
                
                cword = Counter(word)
                for key, val in Counter(user_word).items():
                    if key.upper() in cword.keys():
                        right_letters[key.upper()] = min(cword[key], val)
                
                print("Right place:", end=" ")
                for j in range(len(word)):
                    if j in right_place.keys():
                        print(right_place[j], end=" ")
                    else:
                        print("_", end=" ")
                print()
                print("Right letters:", end=" ")
                for let, count in right_letters.items():
                    print(f"{let} " * count, end=" ")
                print()
        self.word = random.choice(WORDS)
        return points



# Start the game and return result
def wordle() -> int:
    session = Wordle()
    result = 0
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
            result += session.start()
        elif user_choice == 2:
            # print(session.word)
            session.change_word()
            # print(session.word)
        elif user_choice == 0:
            break


    return result




if __name__ == "__main__":
    print("Points:", wordle())