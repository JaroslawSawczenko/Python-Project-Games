import json

def read_data_user_json():
    with open("../data/user_data.json", "r") as json_file:
        data = json.load(json_file)
    return data

def write_data_user_json(data):
    with open("../data/user_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

class User:
    def __init__(self):
        self.user_info = {
            "id": None,
            "name": None,
            "results": {},
        }

    # Stworzenie użytkownika. Potrzebuje tylko imię.

    def create_user(self, name):
        data = read_data_user_json() # czytamy plik

        self.user_info["id"] = len(data)
        self.user_info["name"] = name
        data.append(self.user_info)

        write_data_user_json(data) # zapis pliku

    # Dodawanie wyników. Potrzebuje nazwę gry i wynik.

    def add_results(self, game_name, score):
        self.user_info["results"][game_name] = score
        data = read_data_user_json() # czytamy plik

        data[self.user_info["id"]]["results"] = self.user_info["results"]

        write_data_user_json(data) # zapis pliku


if __name__ == "__main__":

    user1 = User()
    user1.create_user("Test")

    user1.add_results("sudoku", 100)


    # data = {
    #     "name": "Test",
    #     "id": 0,
    # }
    # data1 = {
    #     "name": "Tes1",
    #     "id": 1,
    # }
    # data_read = []
    # data_read.append(data)
    # data_read.append(data1)
    # with open("user_data.json", "w") as json_file:
    #     json.dump(data_read, json_file, indent=4)
    #
    data_read = read_data_user_json() # czytamy plik

    print(data_read)