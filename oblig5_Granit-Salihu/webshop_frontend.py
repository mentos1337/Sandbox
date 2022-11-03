import webshop as ws 
from wallet import Wallet 
 
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
 
 
# Filtrer ut alle varer som er på lager og skriv ut informasjonen for hver av dem 
all_wares_in_stock = ws.get_all_wares_in_stock(all_wares) 
for ware in all_wares_in_stock.values(): 
    ws.print_ware_information(ware) 
 
# Skriv ut den gjennomsnittlige ratingen for denne varen 
print(f"Average rating for the AMD Processor:{ws.calculate_average_ware_rating(all_wares['amd_processor'])}") 
print() 
 
# Oppretter en tom handlevogn 
shopping_cart = {} 
 
# Forsøker å legge til 1 amd processor, 2 playstation 5 konsoller og 3 hdmi kabler 
ws.add_number_of_ware_to_shopping_cart("amd_processor", all_wares, shopping_cart,1) 
ws.add_number_of_ware_to_shopping_cart ("playstation_5", all_wares, shopping_cart, 5) 
ws.add_number_of_ware_to_shopping_cart ("hdmi_cable", all_wares, shopping_cart, 3) 
 
# skriver ut handlevognen 
print() 
print(f"The shopping cart: {shopping_cart}") 
print() 
 
# Oppretter en lommebok som inneholder 10000 kr 
wallet = Wallet(10000) 
print(ws.calculate_shopping_cart_price(shopping_cart,all_wares))
# Forsøker å kjøpe varene i handlevognen 
ws.buy_shopping_cart(wallet,ws.calculate_shopping_cart_price(shopping_cart,all_wares)) 
print() 
 
# Skriver ut mengden penger i lommeboka etter kjøpet 
ws.buy_shopping_cart(wallet,(ws.calculate_shopping_cart_price(shopping_cart,all_wares)))
print(f"The amount in the wallet after the purchase: {wallet.get_amount()}") 