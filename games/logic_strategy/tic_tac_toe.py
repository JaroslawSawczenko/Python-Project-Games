def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()

def check_winner(board, player):
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
    return all(cell != " " for row in board for cell in row)

def get_move(player):
    while True:
        try:
            move = input(f"Gracz {player}, podaj ruch (wiersz i kolumna od 1 do 3, np. 2 3): ")
            row, col = map(int, move.split())
            if row in [1,2,3] and col in [1,2,3]:
                return row - 1, col - 1
            else:
                print("Błędne wartości – podaj dwie liczby od 1 do 3.")
        except ValueError:
            print("Niepoprawny format. Podaj dwie liczby oddzielone spacją.")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Witamy w grze Kółko i Krzyżyk!")
    print_board(board)

    while True:
        row, col = get_move(current_player)

        if board[row][col] != " ":
            print("To pole jest już zajęte. Spróbuj ponownie.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Gracz {current_player} wygrał! Gratulacje!")
            break

        if is_board_full(board):
            print("Remis! Nie ma zwycięzcy.")
            break

        # zmiana gracza
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
