import json

def write_json(dictionary, fileName):
    try: 
        with open(fileName, "w") as file:
            json.dump(dictionary, file, indent=4)
    except FileNotFoundError:
        print("File not found.")

def load_json(fileName):
    try:
        with open(fileName) as file:
            dict_from_file = json.load(file)
    except FileNotFoundError:
        print("File not Found.")
    except json.decoder.JSONDecodeError:
        print("File content is not JSON")
    else:
        return dict_from_file