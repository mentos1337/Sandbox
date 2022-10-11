with open("text_files.txt", "w") as file:
    while True:
        user_input = input(": ")
        if user_input == "q":
            break
        file.write(user_input)