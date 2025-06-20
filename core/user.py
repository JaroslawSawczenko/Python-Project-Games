import json
import os

def read_data_user_json():
    """
    Czyta dane użytkowników z pliku JSON.
    Tworzy katalog ./data/ jeśli nie istnieje.
    Zwraca pustą listę, jeśli plik nie istnieje lub jest uszkodzony.
    """
    file_path = "./data/user_data.json"

    # Tworzy katalog, jeśli nie istnieje
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        # Brak pliku — zwracamy pustą listę
        return []
    except json.JSONDecodeError:
        # Uszkodzony JSON — informujemy i zwracamy pustą listę
        print("Plik danych użytkowników jest uszkodzony. Tworzę nowy.")
        return []

def write_data_user_json(data):
    """
    Zapisuje dane użytkowników do pliku JSON.
    Tworzy katalog ./data/ jeśli nie istnieje.
    Obsługuje poprawnie polskie znaki i zachowuje czytelny format.
    """
    file_path = "./data/user_data.json"
    
    # Tworzy katalog, jeśli nie istnieje
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Zapis danych z odpowiednim kodowaniem i formatowaniem
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

class User:
    def __init__(self, name):
        self.user_info = {
            "id": None,
            "name": name,
            "results": {},
        }


    def create_user(self):
        """
            Tworzy nowego użytkownika lub ładuje istniejącego na podstawie imienia.
            Gwarantuje brak duplikatów i automatyczne przypisanie ID.
        """
        data = read_data_user_json()
        
        # Sprawdź czy użytkownik już istnieje
        for user in data:
            if user["name"] == self.user_info["name"]:
                self.user_info = user
                print(f"Witaj ponownie, {self.user_info['name']}!")
                return
        
        # Jeśli użytkownik nie istnieje, utwórz nowego
        self.user_info["id"] = len(data)
        data.append(self.user_info)
        write_data_user_json(data)
        print(f"Utworzono nowego użytkownika: {self.user_info['name']}")



    def add_results(self, game_name, score):
        self.user_info["results"][game_name] = score
        data = read_data_user_json() # czytamy plik

        data[self.user_info["id"]]["results"] = self.user_info["results"]

        write_data_user_json(data) # zapis pliku

    # Wywiad wyników dla użytkownika.

    def __str__(self):
        user_info = f"Statystyka dla {self.user_info['name']:}\n"
        game_info = ""
        for game_name, result in self.user_info["results"].items():
            game_info += f"-\t{game_name}:\t{result}p."
        return user_info + game_info


if __name__ == "__main__":

    user1 = User()
    user1.create_user("Test")

    user1.add_results("sudoku", 100)
    user1.add_results("2048", 512)

    print(user1)
    print(user1.user_info["id"])

    data_read = read_data_user_json() # czytamy plik
    print(data_read)


    data = {
        "name": "Test",
        "id": 0,
    }
    data1 = {
        "name": "Tes1",
        "id": 1,
    }
    data_read = []
    data_read.append(data)
    data_read.append(data1)
    with open("user_data.json", "w") as json_file:
        json.dump(data_read, json_file, indent=4)
    
