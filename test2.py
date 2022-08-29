def validate_name(name):

    if not name.isalpha():
        return "Bare lov med bokstaver, prøv igjen"
    else:
        if not 2<=len(name)<=12:
            return "Navnet må inneholde minst 2 bokstaver og maks 12"
        else: 
            return "Hello " + name
#Input name, output message

print("Hello World")
print("Hva heter du?")
name = input()
print(validate_name(name))