# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False],
}

discount_threshold = 100

for i in (inventory):
    current_stock,min_stock,restock_amount,on_sale=inventory[i]
    while current_stock<min_stock :
        current_stock=current_stock+restock_amount
        inventory[i][0]=current_stock
    if current_stock>discount_threshold:
        inventory[i][3]=True
print(inventory)




    