# 
all_wares = { 
    "amd_processor": { 
        "name": "AMD Ryzen 9 5900X Processor", 
        "price": 5590.0, 
        "number_in_stock": 50, 
        "ratings": [4.5, 4.0, 5.0, 5.0, 4.5, 3.0], 
        "description": "All the cores and threads you'll need!", 
    }, 
 
    "playstation_5": { 
        "name": "PlayStation 5", 
        "price": 5999.0, 
        "number_in_stock": 0, 
        "ratings": [5.0, 5.0, 4.5, 2.0, 5.0, 4.5, 4.0], 
        "description": "Next generation console, never in stock!", 
    }, 
 
    "hdmi_cable": { 
        "name": "Belkin Ultra High Speed HDMI Cable - 2m", 
        "price": 349.0, 
        "number_in_stock": 3, 
        "ratings": [5.0, 5.0, 4.5, 5.0, 5.0, 5.0], 
        "description": "A high speed overprices HDMI cable!", 
    } 
} 

def print_ware_information(ware):
    for a, b in ware.items():
        print(f"{a}:{b}")


def calculate_average_ware_rating(ware):
    sum = 0
    try:
        for snitt in ware.get("ratings"):
                sum += snitt
    except:
        if ware.get("ratings") == None:
            print(ZeroDivisionError)
    print(round(sum / len(ware["ratings"]),1))

def get_all_wares_in_stock(ware):
    list_of_wares_in_stock = {}
    for a,b in ware.items():
        if b["number_in_stock"]:
            list_of_wares_in_stock[a] = b
    return list_of_wares_in_stock

print(get_all_wares_in_stock(all_wares))