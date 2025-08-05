import random
import os

class Game2048:
    def __init__(self):
        self.size = 4
        self.board = [[0] * self.size for _ in range(self.size)]
        self.score = 0
        self.game_over = False
        self.won = False
        
        # Dodaj dwa losowe kafelki na start
        self.add_random_tile()
        if not self.add_random_tile(): 
            # Bardzo nieprawdopodobne, ale zabezpieczenie
            pass
    
    def add_random_tile(self):
        """Dodaje losowy kafelek (2 lub 4) na pustym miejscu"""
        empty_cells = [(i, j) for i in range(self.size) 
                       for j in range(self.size) if self.board[i][j] == 0]
        
        if not empty_cells:
            return False  # Brak miejsca na nowy kafelek
            
        i, j = random.choice(empty_cells)
        # 90% szans na 2, 10% szans na 4
        self.board[i][j] = 2 if random.random() < 0.9 else 4
        return True
    
    def display_board(self):
        """Wyświetla plansze gry"""
        # Bezpieczne czyszczenie ekranu - działa w większości środowisk
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
        except:
            # Jeśli nie można wyczyścić, po prostu dodaj odstęp
            print('\n' * 50)
        
        print("=" * 25)
        print(f"    GEJA 2048    ")
        print(f"   WYNIK: {self.score}")
        print("=" * 25)
        print()
        
        # Górna ramka
        print("┌" + "─" * 6 + "┬" + "─" * 6 + "┬" + "─" * 6 + "┬" + "─" * 6 + "┐")
        
        for i in range(self.size):
            # Wiersz z liczbami
            row_str = "│"
            for j in range(self.size):
                if self.board[i][j] == 0:
                    cell = "      "
                else:
                    cell = f"{self.board[i][j]:^6}"
                row_str += cell + "│"
            print(row_str)
            
            # Separator między wierszami (oprócz ostatniego)
            if i < self.size - 1:
                print("├" + "─" * 6 + "┼" + "─" * 6 + "┼" + "─" * 6 + "┼" + "─" * 6 + "┤")
        
        # Dolna ramka
        print("└" + "─" * 6 + "┴" + "─" * 6 + "┴" + "─" * 6 + "┴" + "─" * 6 + "┘")
        print()
        
        if self.won and not self.game_over:
            print(" GRATULACJE! Osiągnąłeś 2048! Możesz grać dalej lub wcisnąć 'q' aby zakończyć.")
        elif self.game_over:
            print(" KONIEC GRY! Brak możliwych ruchów.")
        
        print("Sterowanie: W/A/S/D (góra/lewo/dół/prawo), Q - wyjście, R - restart")
    
    def move_left(self):
        """Przesuwa kafelki w lewo i łączy je"""
        moved = False
        new_board = [row[:] for row in self.board]
        
        for i in range(self.size):
            # Usuń zera (przesuń wszystko w lewo)
            row = [x for x in new_board[i] if x != 0]
            
            # Połącz sąsiadujące identyczne liczby
            j = 0
            while j < len(row) - 1:
                if row[j] == row[j + 1]:
                    row[j] *= 2
                    self.score += row[j]
                    if row[j] == 2048 and not self.won:
                        self.won = True
                    row.pop(j + 1)
                j += 1
            
            # Dopełnij zerami do pełnej długości
            row.extend([0] * (self.size - len(row)))
            
            # Sprawdź czy coś się zmieniło
            if row != self.board[i]:
                moved = True
            
            new_board[i] = row
        
        self.board = new_board
        return moved
    
    def move_right(self):
        """Przesuwa kafelki w prawo"""
        # Odwróć plansze, przesuń w lewo, odwróć z powrotem
        self.board = [row[::-1] for row in self.board]
        moved = self.move_left()
        self.board = [row[::-1] for row in self.board]
        return moved
    
    def move_up(self):
        """Przesuwa kafelki w górę"""
        # Transponuj, przesuń w lewo, transponuj z powrotem
        self.transpose()
        moved = self.move_left()
        self.transpose()
        return moved
    
    def move_down(self):
        """Przesuwa kafelki w dół"""
        # Transponuj, przesuń w prawo, transponuj z powrotem
        self.transpose()
        moved = self.move_right()
        self.transpose()
        return moved
    
    def transpose(self):
        """Transponuje plansze (zamienia wiersze z kolumnami)"""
        self.board = [[self.board[j][i] for j in range(self.size)] 
                      for i in range(self.size)]
    
    def can_move(self):
        """Sprawdza czy możliwy jest jakikolwiek ruch"""
        # Sprawdź czy są puste pola
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return True
        
        # Sprawdź czy można połączyć kafelki poziomo
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.board[i][j] == self.board[i][j + 1]:
                    return True
        
        # Sprawdź czy można połączyć kafelki pionowo
        for i in range(self.size - 1):
            for j in range(self.size):
                if self.board[i][j] == self.board[i + 1][j]:
                    return True
        
        return False
    
    def reset_game(self):
        """Resetuje grę do stanu początkowego"""
        self.board = [[0] * self.size for _ in range(self.size)]
        self.score = 0
        self.game_over = False
        self.won = False
        self.add_random_tile()
        self.add_random_tile()
    
    def play(self):
        """Główna pętla gry"""
        self.display_board()
        
        while not self.game_over:
            try:
                move = input("Twój ruch: ").lower().strip()
                
                if move == 'q':
                    print("Dzięki za grę! ")
                    break
                elif move == 'r':
                    self.reset_game()
                    self.display_board()
                    continue
                
                moved = False
                if move == 'w':
                    moved = self.move_up()
                elif move == 's':
                    moved = self.move_down()
                elif move == 'a':
                    moved = self.move_left()
                elif move == 'd':
                    moved = self.move_right()
                else:
                    print("Nieprawidłowy ruch! Użyj W/A/S/D, Q lub R")
                    continue
                
                if moved:
                    # Dodaj nowy kafelek tylko jeśli jest miejsce
                    if not self.add_random_tile():
                        # Jeśli nie można dodać kafelka, sprawdź czy koniec gry
                        if not self.can_move():
                            self.game_over = True
                    elif not self.can_move():
                        self.game_over = True
                
                self.display_board()
                
            except KeyboardInterrupt:
                print("\nGra przerwana. Do zobaczenia! ")
                break
            except EOFError:
                print("\nGra zakończona. Do zobaczenia! ")
                break

def main():
    """Funkcja główna - uruchamia grę"""
    print("Witaj w grze 2048! ")
    print("Celem jest osiągnięcie kafelka o wartości 2048.")
    print("Łącz identyczne liczby przesuwając je w tym samym kierunku!")
    print()
    input("Naciśnij Enter aby rozpocząć...")
    
    game = Game2048()
    game.play()

if __name__ == "__main__":
    main()