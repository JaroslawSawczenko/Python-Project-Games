import json
import os
from typing import Dict, List, Optional, Union

def read_data_user_json() -> List[Dict]:
    """
    Czyta dane użytkowników z pliku JSON.
    Zwraca pustą listę, jeśli plik nie istnieje lub jest uszkodzony.
    """
    file_path = "./core/data/user_data.json"  

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        print("Tworzę nowy plik danych użytkowników...")
        return []
    except json.JSONDecodeError as e:
        print(f"Plik danych użytkowników jest uszkodzony: {e}. Tworzę nowy.")
        return []
    except Exception as e:
        print(f"Wystąpił błąd podczas odczytu pliku: {e}")
        return []

def write_data_user_json(data: List[Dict]) -> bool:
    """
    Zapisuje dane użytkowników do pliku JSON.
    Zwraca True jeśli sukces, False jeśli błąd.
    """
    file_path = "./core/data/user_data.json" 

    try:
        # Tworzy katalog, jeśli nie istnieje
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Zapis danych z odpowiednim kodowaniem i formatowaniem
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Błąd podczas zapisu pliku: {e}")
        return False

class User:
    """Klasa zarządzająca użytkownikami i ich wynikami."""
    
    def __init__(self):
        self.user_info = {
            "id": None,
            "name": None,
            "results": {},
        }

    def create_user(self, name: str) -> 'User':
        """
        Tworzy nowego użytkownika lub ładuje istniejącego na podstawie imienia.
        """
        if not name or not name.strip():
            raise ValueError("Imię użytkownika nie może być puste")
            
        name = name.strip()
        data = read_data_user_json()

        # Sprawdź czy użytkownik już istnieje
        for user in data:
            if user.get('name') == name:
                self.user_info = user
                print(f"Witaj ponownie, {self.user_info['name']}!")
                return self
        
        # Jeśli użytkownik nie istnieje, utwórz nowego
        self.user_info["id"] = len(data)
        self.user_info["name"] = name
        data.append(self.user_info.copy())
        
        if write_data_user_json(data):
            print(f"Utworzono nowego użytkownika: {self.user_info['name']}")
        else:
            print("Błąd podczas zapisywania nowego użytkownika")
            
        return self

    def add_results(self, game_name: str, score: Union[int, float]) -> bool:
        """
        Dodaje wynik gry dla użytkownika, zapisuje tylko jeśli to nowy rekord.
        Zwraca True jeśli zapisano nowy rekord.
        """
        if not isinstance(score, (int, float)) or score < 0:
            print(f"Nieprawidłowy wynik: {score}")
            return False
            
        previous_score = self.user_info["results"].get(game_name)

        # Sprawdzenie czy to pierwszy wynik lub lepszy niż dotychczasowy
        if previous_score is None or score > previous_score:
            self.user_info["results"][game_name] = score

            # Wczytaj aktualną bazę użytkowników
            data = read_data_user_json()

            # Walidacja ID i aktualizacja rekordu
            user_id = self.user_info.get("id")
            if isinstance(user_id, int) and 0 <= user_id < len(data):
                data[user_id]["results"] = self.user_info["results"]
                if write_data_user_json(data):
                    print(f"🎉 Nowy rekord w grze '{game_name}'! Wynik: {score}")
                    return True
                else:
                    print("Błąd podczas zapisywania wyniku")
                    return False
            else:
                print("Błąd: nieprawidłowy identyfikator użytkownika.")
                return False
        else:
            print(f"Nie pobiłeś rekordu. Twój najlepszy wynik w '{game_name}' to {previous_score}.")
            return False

    def get_total_score(self) -> Union[int, float]:
        """Zwraca sumę wszystkich wyników użytkownika."""
        return sum(self.user_info["results"].values())

    def get_games_played(self) -> int:
        """Zwraca liczbę gier w które grał użytkownik."""
        return len(self.user_info["results"])

    def __str__(self) -> str:
        """String reprezentacja użytkownika."""
        user_info = f"Użytkownik: {self.user_info['name']} (ID: {self.user_info['id']})\n"
        
        if not self.user_info["results"]:
            return user_info + "Brak wyników"
            
        game_info = "Wyniki:\n"
        for game_name, result in self.user_info["results"].items():
            game_info += f"  • {game_name}: {result} pkt\n"
        
        game_info += f"Suma punktów: {self.get_total_score()}"
        return user_info + game_info