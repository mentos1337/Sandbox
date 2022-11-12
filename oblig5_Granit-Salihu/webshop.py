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
#oppgave1
def print_ware_information(ware):
    for a, b in ware.items():
        print(f"{a}:{b}")

#oppgave2
def calculate_average_ware_rating(ware_list):
    sum = 0
    try:
        for snitt in ware_list.get("ratings"):
                sum += snitt
    except:
        if ware_list.get("ratings") == None:
            print("denne varen har ingen ratings")
    return(round(sum / len(ware_list["ratings"]),1))


#oppgave3
def get_all_wares_in_stock(ware):
    list_of_wares_in_stock = {}
    for a,b in ware.items():
        if b["number_in_stock"]:
            list_of_wares_in_stock[a] = b
    return list_of_wares_in_stock

#oppgave 4
def is_number_of_ware_in_stock(ware,amount):
    if ware["number_in_stock"] >= amount:
        return True
    else:
        return False
        
#oppgave 5
def add_number_of_ware_to_shopping_cart(ware_key,ware_dict,shopping_cart,number_of_ware):
    instock  = is_number_of_ware_in_stock(ware_dict[ware_key],number_of_ware)
    if instock is True:
        shopping_cart[ware_key] = number_of_ware
        print("Added {} of {} to shopping cart".format(number_of_ware, ware_dict[ware_key]["name"]))
    elif instock is False:
        shopping_cart[ware_key] = ware_dict[ware_key]["number_in_stock"]
        print("Added {} of {} to shopping cart".format(ware_dict[ware_key]["number_in_stock"], ware_dict[ware_key]["name"]))
    if not instock:
        print("Sorry {} is not in stock".format(ware_dict[ware_key]["name"]))

#oppgave 6
def calculate_shopping_cart_price(shoppingkart,ware_dict,tax=1.25):
    price = 0
    for item in shoppingkart:
        if shoppingkart[item] >=1:
            price += ware_dict[item]["price"] * shoppingkart[item]
    return price * tax

#oppgave 7
def buy_shopping_cart(wallet,shoppingkart):
    if wallet.get_amount() < shoppingkart:
        print("Ikke nok penger")
    else:
        return wallet.subtract_amount(shoppingkart)