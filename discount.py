def get_discount(price, count):
    total = price * count
    if total < 50:
        return total * 0.9
    else:
        return total

while True:
    try:
        price = float(input("Enter the prcie of your item: "))
        count = int(input("Enter how many items you brought: "))
        print(f"Final price: SAR{get_discount(price, count):.2f}")
        break
    except ValueError as ex:
        print("Invalid number. The error is ", ex)
    except:
        print("Wrong input")
    else:
        print("You followed our instruction very carefully and succeded!")
    finally:
        print("=============================")
        print("Your bill!: ")
        print("\nItems Bought: ", count)
        print("Price of Items: ", price)
        print("Have a Great Day!!!")
        print("=============================")