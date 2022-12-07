import random
student = { 
    "first name" : "Ola", 
    "last name" : "Nordmann",
    "favorite course" : "Programmering 1"}

print(student["first name"], student["last name"])

student["favorite course"] = "ITF10219 Programmering 1"
print(student)

def printer():
    print(f"^^^^^^^^^^^^\n*****{random.randrange(0,101)}*****")
    
printer()