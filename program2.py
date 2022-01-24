__author__ = 'Ella Seaman'
#02/08/2021


def main():
    o_price = float(input("What is the price per pound of oranges? "))
    o_pounds = float(input("How many pounds of oranges are being purchased? "))
    total_orange = o_price * o_pounds
    print("Total price of oranges ", total_orange, ".")
    a_price = float(input("What is the price per pound of apples? "))
    a_pounds = float(input("How many pounds of apples are being purchased? "))
    total_apple = a_price * a_pounds
    print("Total price of apples ", total_apple, ".")
    final_total = total_orange + total_apple
    print("Total price of groceries ", final_total, ".")

main()




