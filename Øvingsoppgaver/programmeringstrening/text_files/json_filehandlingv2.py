import json_module

game = {"name": "Trackmania", "genre": "Racing", "max players": 64}
fileName = "text_files/game.json"

json_module.write_json(game,fileName)

dict_from_file = json_module.load_json(fileName)
print(dict_from_file)
#sjekke om det er en dict, printer ut name variablen fra lista
print(dict_from_file["name"])