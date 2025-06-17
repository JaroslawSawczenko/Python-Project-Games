import json

class User:
    def __init__(self):
        self.user_info = {
            "id": None,
            "name": None,
            "results": {},
        }

    def create_user(self, name):
        with open("user_data.json", "r") as json_file:
            data = json.load(json_file)

        self.user_info["id"] = len(data)
        self.user_info["name"] = name
        data.append(self.user_info)

        with open("user_data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)



if __name__ == "__main__":

    user1 = User()
    user1.create_user("Test")


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
    with open("user_data.json", "r") as json_file:
        data_read = json.load(json_file)

    print(data_read)