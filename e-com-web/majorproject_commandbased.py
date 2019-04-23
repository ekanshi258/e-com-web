
cart=[]
def display():
    print("Shop from the following categories:")
    print("1. Books")
    print("2. Bags")
    print("3. Stationery")
    cat = int(input("Enter your choice number: "))
    return cat

def books():
    global total; total = 0
    print("1.The Book thief -- Rs. 600")
    print("2.Hitchhiker's Guide to the Galaxy -- Rs.750")
    print("3.Diary of a Young Girl: Anne Frank -- Rs.395 ")
    book = int(input("Enter the number of the book you want to buy: "))
    if(book == 1):
        cart.append("The book thief")
        total += 600
        return cart
    elif(book == 2):
        cart.append("Hitchhiker's Guide to the Galaxy")
        total += 750
        return cart
    elif(book == 3):
        cart.append("Diary of Anne Frank")
        total; total += 395
        return cart
    else:
        print("Invalid choice")
        return books()

    

def bags():
    global total; total = 0
    print("1.Generic -- Rs. 1600")
    print("2.Swanky -- Rs.1750")
    print("3.Cute -- Rs.1395 ")
    bag = int(input("Enter the number of the bag you want to buy: "))
    if(bag == 1):
        cart.append("Generic bag")
        total += 1600
        return cart
    elif(bag == 2):
        cart.append("Swanky bag")
        total += 1750
        return cart
    elif(bag == 3):
        cart.append("Cute bag")
        total += 1395
        return cart
    else:
        print("Invalid choice")
        return bags()

def stat():
    global total; total = 0
    print("1.Pen stand -- Rs. 300")
    print("2.Pack of pens -- Rs.150")
    print("3.Geometry box-- Rs.195 ")
    bag = int(input("Enter the number of the item you want to buy: "))
    if(bag == 1):
        cart.append("Pen stand")
        total += 300
        return cart
    elif(bag == 2):
        cart.append("Pack of pens")
        total += 150
        return cart
    elif(bag == 3):
        cart.append("Geometry box")
        total += 195
        return cart
    else:
        print("Invalid choice")
        return stat()
#Global scope


try:
    choice = display()
    if (choice<1 or choice >3):
        raise Exception("Invalid choice")

except Exception as err:
    print("Invalid choice")
    choice = display()

finally:
    if (choice == 1):
        cart = books()
    elif(choice == 2):
        cart = bags()
    elif(choice == 3):
        cart = stat()

print("You have ordered: "+ str(cart))
print("Your order has been placed for Rs.", total)
