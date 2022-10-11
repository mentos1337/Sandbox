import json

game = {"name": "Gothic", "genre": "RPG", "max players": 1}

try: 
    with open("text_files/game.json", "w") as file:
        json.dump(game, file, indent=4)
except FileNotFoundError:
    print("File not found.")

try:
    with open("game.json") as file:
        dict_from_file = json.load(file)
except FileNotFoundError:
    print("File not Found.")
except json.decoder.JSONDecodeError:
    print("File content is not JSON")
else:
    print(dict_from_file)
    print(dict_from_file["name"])