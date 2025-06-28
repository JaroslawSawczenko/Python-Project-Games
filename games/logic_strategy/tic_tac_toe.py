import os
import time

def clear_screen():
    """Czyści ekran konsoli"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    """Wyświetla planszę gry w ładnym formacie"""
    clear_screen()
    print("\n" + "="*30)
    print("     TIC-TAC-TOE ")
    print("="*30)
    print("\n   Pozycje na planszy:")
    print("     1 | 2 | 3")
    print("    -----------")
    print("     4 | 5 | 6")
    print("    -----------")
    print("     7 | 8 | 9")
    print("\n   Aktualna plansza:")
    
    # Konwertuj pozycje na czytelne symbole
    display_board = []
    for i in range(3):
        row = []
        for j in range(3):
            cell = board[i][j]
            if cell == "X":
                row.append("X")
            elif cell == "O":
                row.append("O")
            else:
                row.append("  ")
        display_board.append(row)
    
    # Wyświetl planszę
    for i, row in enumerate(display_board):
        print(f"     {row[0]} │ {row[1]} │ {row[2]}")
        if i < 2:
            print("    ───┼───┼───")
    print()

def print_position_guide():
    """Wyświetla przewodnik pozycji"""
    print("   Pozycje na planszy:")
    print("     1 | 2 | 3")
    print("    -----------")
    print("     4 | 5 | 6")
    print("    -----------")
    print("     7 | 8 | 9")

def check_winner(board, player):
    """Sprawdza czy gracz wygrał"""
    # Sprawdzenie wierszy, kolumn i przekątnych
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # wiersze
            return True
        if all([board[j][i] == player for j in range(3)]):  # kolumny
            return True
    
    # przekątne
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    """Sprawdza czy plansza jest pełna"""
    return all(cell != " " for row in board for cell in row)

def get_move(player):
    """Pobiera ruch od gracza z walidacją"""
    while True:
        try:
            move = input(f" Gracz {player}, wybierz pozycję (1-9) lub 'q' aby wyjść: ").strip().lower()
            
            if move == 'q':
                return None, None
            
            position = int(move)
            if 1 <= position <= 9:
                # Konwertuj pozycję na współrzędne
                row = (position - 1) // 3
                col = (position - 1) % 3
                return row, col
            else:
                print(" Wybierz liczbę od 1 do 9!")
        except ValueError:
            print(" Niepoprawny format. Podaj liczbę od 1 do 9 lub 'q' aby wyjść.")

def get_player_names():
    """Pobiera imiona graczy"""
    print(" Konfiguracja graczy")
    player1 = input("Podaj imię gracza 1 (X): ").strip()
    player2 = input("Podaj imię gracza 2 (O): ").strip()
    
    if not player1:
        player1 = "Gracz 1"
    if not player2:
        player2 = "Gracz 2"
    
    return player1, player2

def calculate_score(moves_count, winner_symbol):
    """Oblicza punkty na podstawie liczby ruchów"""
    if winner_symbol:
        # Im mniej ruchów, tym więcej punktów
        base_score = 100
        bonus = max(0, (9 - moves_count) * 10)
        return base_score + bonus
    return 0  # Remis = 0 punktów

def play_again():
    """Pyta czy gracz chce zagrać ponownie"""
    while True:
        choice = input("\n Czy chcesz zagrać ponownie? (t/n): ").strip().lower()
        if choice in ['t', 'tak', 'y', 'yes']:
            return True
        elif choice in ['n', 'nie', 'no']:
            return False
        else:
            print(" Odpowiedz 't' (tak) lub 'n' (nie)")

def tic_tac_toe():
    """Główna funkcja gry Tic-Tac-Toe"""
    clear_screen()
    print(" Witamy w grze Kółko i Krzyżyk! ")
    print("\nZasady:")
    print("• Gracze na zmianę stawiają swoje znaki")
    print("• Celem jest ustawienie 3 znaków w rzędzie")
    print("• Można wygrać w poziomie, pionie lub na przekątnej")
    
    input("\n⏎ Naciśnij Enter aby kontynuować...")
    
    # Pobierz imiona graczy
    player1_name, player2_name = get_player_names()
    
    total_games = 0
    player1_wins = 0
    player2_wins = 0
    draws = 0
    best_score = 0
    
    while True:
        total_games += 1
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"
        current_name = player1_name if current_player == "X" else player2_name
        moves_count = 0
        
        print_board(board)
        print(f" Gra #{total_games}")
        print(f" {player1_name} vs  {player2_name}")
        
        # Główna pętla gry
        while True:
            current_name = player1_name if current_player == "X" else player2_name
            row, col = get_move(f"{current_name} ({current_player})")
            
            # Sprawdź czy gracz chce wyjść
            if row is None:
                print(" Dzięki za grę!")
                return best_score
            
            # Sprawdź czy pole jest wolne
            if board[row][col] != " ":
                print(" To pole jest już zajęte. Spróbuj ponownie.")
                input("⏎ Naciśnij Enter aby kontynuować...")
                print_board(board)
                continue

            # Wykonaj ruch
            board[row][col] = current_player
            moves_count += 1
            print_board(board)

            # Sprawdź wygraną
            if check_winner(board, current_player):
                print(f" {current_name} ({current_player}) wygrał! Gratulacje! ")
                
                # Oblicz punkty
                score = calculate_score(moves_count, current_player)
                if score > best_score:
                    best_score = score
                
                print(f" Wynik: {score} punktów")
                
                # Aktualizuj statystyki
                if current_player == "X":
                    player1_wins += 1
                else:
                    player2_wins += 1
                
                break

            # Sprawdź remis
            if is_board_full(board):
                print(" Remis! Nie ma zwycięzcy.")
                draws += 1
                break

            # Zmień gracza
            current_player = "O" if current_player == "X" else "X"
        
        # Wyświetl statystyki
        print(f"\n Statystyki po {total_games} grze/grach:")
        print(f" {player1_name}: {player1_wins} zwycięstw")
        print(f" {player2_name}: {player2_wins} zwycięstw")
        print(f" Remisy: {draws}")
        print(f" Najlepszy wynik: {best_score} punktów")
        
        # Zapytaj o kolejną grę
        if not play_again():
            break
    
    print(f"\n Koniec sesji! Najlepszy wynik: {best_score} punktów")
    print(" Dzięki za grę!")
    
    return best_score

if __name__ == "__main__":
    tic_tac_toe()