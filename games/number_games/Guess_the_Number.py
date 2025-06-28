import random
import os
import time

class GuessNumber:
    def __init__(self):
        self.difficulty = None
        self.number_range = None
        self.max_attempts = None
        self.secret_number = None
        self.attempts_used = 0
        self.score = 0
        self.game_over = False
        self.won = False

        # Ustawienia trudności
        self.difficulty_settings = {
            1: {"name": "Łatwy", "range": (1, 50), "attempts": 10, "base_score": 100},
            2: {"name": "Średni", "range": (1, 100), "attempts": 8, "base_score": 200},
            3: {"name": "Trudny", "range": (1, 200), "attempts": 6, "base_score": 300}
        }

    def clear_screen(self):
        """Czyści ekran konsoli"""
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
        except:
            print('\n' * 50)

    def display_header(self):
        """Wyświetla nagłówek gry"""
        print("=" * 40)
        print("        ZGADNIJ LICZBĘ")
        print("=" * 40)
        print()

    def select_difficulty(self):
        """Pozwala graczowi wybrać poziom trudności"""
        while True:
            self.clear_screen()
            self.display_header()

            print("Wybierz poziom trudności:")
            print()
            for key, value in self.difficulty_settings.items():
                range_info = f"{value['range'][0]}-{value['range'][1]}"
                print(f"{key}. {value['name']} (Zakres: {range_info}, Próby: {value['attempts']})")

            print("0. Powrót do menu głównego")
            print()

            try:
                choice = input("Twój wybór: ").strip()

                if choice == '0':
                    return False

                choice = int(choice)
                if choice in self.difficulty_settings:
                    self.difficulty = choice
                    settings = self.difficulty_settings[choice]
                    self.number_range = settings["range"]
                    self.max_attempts = settings["attempts"]
                    return True
                else:
                    print("Nieprawidłowy wybór! Wybierz liczbę od 0 do 3.")
                    time.sleep(1)

            except ValueError:
                print("Podaj prawidłową liczbę!")
                time.sleep(1)

    def start_new_game(self):
        """Rozpoczyna nową grę"""
        self.secret_number = random.randint(self.number_range[0], self.number_range[1])
        self.attempts_used = 0
        self.score = 0
        self.game_over = False
        self.won = False

    def calculate_score(self):
        """Oblicza wynik na podstawie poziomu trudności i liczby użytych prób"""
        if self.won:
            base_score = self.difficulty_settings[self.difficulty]["base_score"]
            # Im mniej prób użyto, tym wyższy wynik
            efficiency_bonus = max(0, (self.max_attempts - self.attempts_used) * 10)
            self.score = base_score + efficiency_bonus
        else:
            self.score = 0

    def display_game_info(self):
        """Wyświetla informacje o bieżącej grze"""
        settings = self.difficulty_settings[self.difficulty]
        print(f"Poziom: {settings['name']}")
        print(f"Zakres: {self.number_range[0]} - {self.number_range[1]}")
        print(f"Próby: {self.attempts_used}/{self.max_attempts}")
        print()

    def get_player_guess(self):
        """Pobiera próbę zgadnięcia od gracza"""
        while True:
            try:
                guess_input = input(
                    f"Podaj liczbę ({self.number_range[0]}-{self.number_range[1]}) lub 'q' aby wyjść: ").strip()

                if guess_input.lower() == 'q':
                    return None

                guess = int(guess_input)

                if self.number_range[0] <= guess <= self.number_range[1]:
                    return guess
                else:
                    print(f"Liczba musi być w zakresie {self.number_range[0]}-{self.number_range[1]}!")

            except ValueError:
                print("Podaj prawidłową liczbę!")

    def give_hint(self, guess):
        """Daje wskazówkę na podstawie próby gracza"""
        difference = abs(self.secret_number - guess)

        if guess < self.secret_number:
            direction = "Za mało!"
        else:
            direction = "Za dużo!"

        # Dodatkowe wskazówki w zależności od różnicy
        if difference <= 5:
            hint = "Bardzo blisko!"
        elif difference <= 15:
            hint = "Blisko!"
        elif difference <= 30:
            hint = "Daleko..."
        else:
            hint = "Bardzo daleko..."

        print(f"{direction} {hint}")

        # Specjalna wskazówka dla trudnego poziomu
        if self.difficulty == 3 and self.attempts_used >= self.max_attempts // 2:
            if self.secret_number % 2 == 0:
                print("Wskazówka: Szukana liczba jest parzysta.")
            else:
                print("Wskazówka: Szukana liczba jest nieparzysta.")

    def display_result(self):
        """Wyświetla wynik gry"""
        print("=" * 40)
        if self.won:
            print("🎉 GRATULACJE! WYGRAŁEŚ! 🎉")
            print(f"Zgadłeś liczbę {self.secret_number} w {self.attempts_used} próbach!")
            print(f"Twój wynik: {self.score} punktów")
        else:
            print(" KONIEC GRY! ")
            print(f"Nie udało się zgadnąć w {self.max_attempts} próbach.")
            print(f"Ukryta liczba to: {self.secret_number}")
        print("=" * 40)

    def play_round(self):
        """Gra jedną rundę"""
        self.start_new_game()

        while not self.game_over:
            self.clear_screen()
            self.display_header()
            self.display_game_info()

            if self.attempts_used > 0:
                print("Poprzednie próby i wskazówki:")
                print("-" * 30)

            guess = self.get_player_guess()

            if guess is None:  # Gracz chce wyjść
                return False

            self.attempts_used += 1

            if guess == self.secret_number:
                self.won = True
                self.game_over = True
                self.calculate_score()
            else:
                self.give_hint(guess)

                if self.attempts_used >= self.max_attempts:
                    self.game_over = True
                else:
                    input("\nNaciśnij Enter aby kontynuować...")

        # Wyświetl wynik
        self.clear_screen()
        self.display_header()
        self.display_result()

        return True

    def play(self):
        """Główna pętla gry"""
        while True:
            # Wybór poziomu trudności
            if not self.select_difficulty():
                print("Dzięki za grę!")
                return self.score if hasattr(self, 'score') else 0

            # Graj dopóki gracz chce
            while True:
                if not self.play_round():
                    return self.score if hasattr(self, 'score') else 0

                # Zapytaj czy grać ponownie
                while True:
                    play_again = input("\nChcesz zagrać ponownie? (t/n): ").lower().strip()
                    if play_again in ['t', 'tak', 'y', 'yes']:
                        break
                    elif play_again in ['n', 'nie', 'no']:
                        return self.score if hasattr(self, 'score') else 0
                    else:
                        print("Podaj 't' (tak) lub 'n' (nie)")

def main():
    """Funkcja główna - uruchamia grę"""
    print("Witaj w grze 'Zgadnij Liczbę'!")
    print("Komputerstarki losuje liczbę, a Ty musisz ją zgadnąć!")
    print("Im wyższy poziom trudności, tym większy zakres i mniej prób.")
    print()
    input("Naciśnij Enter aby rozpocząć...")

    game = GuessNumber()
    final_score = game.play()

    print(f"\nTwój końcowy wynik: {final_score} punktów")
    print("Do zobaczenia!")


if __name__ == "__main__":
    main()