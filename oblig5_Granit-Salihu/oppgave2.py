# 
WareEx = {"Name": "Example Ware","Price": "3999,-","Number in stock": 30,"Description": "A non existent ware used only for this example","ratings":1}

def print_ware_information(ware):
    for a in ware.items():
        print(a)

print_ware_information(WareEx)

def calculate_average_ware_rating(ware):
    sum = 0
    try:
        for snitt in ware.get("ratings"):
                sum += snitt
    except:
        if ware.get("ratings") == None:
            print(ZeroDivisionError)
    return round(sum / len(ware.get("ratings")),1)

calculate_average_ware_rating(WareEx)