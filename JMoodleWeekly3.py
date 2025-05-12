# Code in english becuase is part of the reqs
# The lambda is not mine 
# All the jokes are with intetion to keep my code personality
# That is the reason why This code is a little informal+
# Welcome

Inventory = {
    "popcorn": {"Price": 5.10, "Quantity": 10},
    "coke": {"Price": 20.30, "Quantity": 3},
    "chocoramo": {"Price": 15.40, "Quantity": 10},
}

#AddProducts
def AddProducts(Inventory, Product, Price, Quantity):
    while True:
        Product = input("Enter the Product name: ").lower().strip()
        if Product in ["exit", "salir", "end"]:
            print("----------")
            print("Exiting...")
            return
        if not Product:
            print("Product name cannot be empty")
        elif Product in Inventory:
            print("Product already exists")
        else:
            print("----------------------------------------------------")
            print(f"Product {Product.title()} added")
            break
    while True:
        Price = input("Enter the Product Price: ").strip()
        if Price.lower() in ["exit", "salir", "end"]:
            print("Exiting...")
            return
        if not Price:
            print("Price cannot be empty")
            continue
        elif Price.isalpha():
            print("Price must be a number")
        else:
            Price = float(Price)
            if Price <= 0:
                print("Price must be greater than 0")
            else:
                print(f"Price of {Product.title()} added")
                break
        
    while True:
        Quantity = input("Enter the Product quantity: ").strip()
        if Quantity in ["exit", "salir", "end"]:
            print("----------")           
            print("Exiting...")
            return
        if not Quantity:
            print("Quantity cannot be empty")
        elif Quantity.isdigit():
            Quantity = int(Quantity)
            if Quantity <= 0:
                print("Quantity must be greater than 0")
            else:
                print(f"Quantity of {Product.title()} added")
                break
        else:
            print("Quantity must be a numbers")
    Inventory[Product] = ({"Price": Price, "Quantity": Quantity})
    print("----------------------------------------------------")
    print(f"Product {Product.title()} added with Price ${Price:.2f} and quantity: {Quantity}")
    return Inventory

#SearchProducts 
def SearchProducts(Product, Inventory):
    print("Enter the name of the Product to search or type 'exit' to return to the menu: ")
    while True:
        Product = input("Enter the name of the Product to search: ").lower().strip()
        if Product in ["exit", "salir", "end"]:
            print("----------")           
            print("Exiting...")
            return
        if not Product:
            print("Product name cannot be empty")
        elif Product in Inventory:
            Details = Inventory[Product]
            print("-------------------------------------------")
            print(f"Product: {Product.title()} | Price: ${Details['Price']:.2f} | Quantity: {Details['Quantity']}")
            print("-------------------------------------------")
            break
        else:
            print(f"The Product {Product.title()} is not in the inventory. Please try again or exit")

#UpdateInfo
def UpdateInfo():
    InventoryList()
    while True:
        LookForProduct = input("Enter the name of the product to update or type 'exit' to return to the menu: ").strip().lower()
        if LookForProduct in ["salir", "exit", "end"]:
            print("----------")           
            print("Exiting...")
            return
        if not LookForProduct:
            print("The name cannot be empty.")
        elif LookForProduct in Inventory:
            while True:
                WhatYouWantToChange = input("What do you want to change? Price/Quantity: ").strip().lower()
                if WhatYouWantToChange in ["salir", "exit", "end"]:
                    print("----------")           
                    print("Exiting...")
                    return  
                elif WhatYouWantToChange in ["price", "precio", "value", "valor"]:
                    while True:
                        ChangePrice = input("What is the new price? ").strip()
                        if ChangePrice.isdigit():
                            ChangePrice = float(ChangePrice)
                            if ChangePrice < 0:
                                print("The price cannot be less than 0, or are you giving it away?")
                            else:
                                Inventory[LookForProduct]['Price'] = ChangePrice
                                print("----------------------------------------------------")
                                print(f"The price of {LookForProduct.title()} has been updated to {ChangePrice:.2f}.")
                                return
                        else:
                            print("Please follow instructions and enter a number")
                elif WhatYouWantToChange in ["quantity", "cantidad", "stock"]:
                    while True:
                        ChangeQuantity = input("What is the new quantity? ").strip()
                        if ChangeQuantity.isdigit():
                            ChangeQuantity = int(ChangeQuantity)
                            if ChangeQuantity < -1:
                                print("The quantity cannot be less than 0, or are you giving it away?")
                            else:
                                Inventory[LookForProduct]['Quantity'] = ChangeQuantity
                                print("----------------------------------------------------")
                                print(f"The quantity of {LookForProduct.title()} has been updated to {ChangeQuantity}.")
                                return
                        else:
                            print("Please follow instructions a number integer")
                else:
                    print("Please follow instructions and enter a option")
        else:
            print(f"The product {LookForProduct.title()} is not in the inventory.")
            
#TotalValue of the inventory
def TotalValue(Inventory):
    print("----------------------------------------------------")
    if not Inventory:
        print("No products in the inventory")
        return 0.0
    TotalValue = lambda items: sum(details["Price"] * details["Quantity"] for details in items.values())
    value = TotalValue(Inventory)
    print(f"Total value of the inventory: ${value:.2f}")
    return value

#Delete Products :B
def DeleteProducts(Inventory):
    if Inventory:
        print("------------")
        print("Inventory:")
        print("------------")
        for Product in Inventory:
            print(f"-> {Product.title()}")
        print("------------")
        while True:
            Eliminar = input("Enter the name of the product to delete or type exit to return to the menu: ").strip().lower()
            if Eliminar in ["salir", "exit"]:
                print("----------")
                print("Exiting...")
                break
            elif Eliminar in Inventory:
                del Inventory[Eliminar]
                print("-------------------")
                print(f"Product {Eliminar.title()} removed")
                break
            elif not Eliminar:
                print("The name cannot be empty.")
            else:
                print("The product is not in the inventory. Please try again")
    else:
        print("The inventory is empty")

#I think this is necesary because you need to know the status of the stock
#Hole inventory
def InventoryList():
    if not Inventory:
        print("-----------------------------")
        print("No products in the inventory")
        print("-----------------------------")
    else:
        print("This is the list of products in the inventory")
        print("-------------------------------------------------")
        for Product, details in Inventory.items():
            print(f"Product: {Product.title()} | Price: ${details['Price']:.2f} | Quantity: {details['Quantity']}")

# #Menu(English)
def Menu():
    while True:
        print("----------------------------------------------------")
        print("Welcome to the inventory management system")
        print("1. Add products")
        print("2. Search products")
        print("3. Update info")
        print("4. Total value of the stock")
        print("5. Delete Products")
        print("6. Inventory list")
        print("7. Salir | Exit | Cerrar | Close | End | Finish")
        print("----------------------------------------------------")
        option = input("What you wantxd: ").lower()
        match option:
            case "1" | "add products" | "add" | "addproducts":
                AddProducts(Inventory, "", 0, 0)
            case "2" | "search products" | "search" | "search products":
                SearchProducts("", Inventory)
            case "3" | "update info" | "update" | "update info":
                UpdateInfo()
            case "4" | "total value of the stock" | "total" | "total value of the stock":
                TotalValue(Inventory)
            case "5" | "delete products" | "delete" | "delete products":
                DeleteProducts(Inventory)
            case "6" | "inventory list" | "list" | "inventory list":
                InventoryList()
            case "" | "salir" | "exit" | "cerrar" | "close" | "end" | "finish":
                break
            case _:
                print("Invalid option, please try again.")   

Menu()
