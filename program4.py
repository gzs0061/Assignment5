__author__ = 'Ella Seaman'
#02/08/2021

def main():
    initial = float(input("What is the initial balance? "))
    deposits = float(input("Monthly deposits? "))
    withdrawals = float(input("Months withdrawals? "))

    initial += deposits
    initial -= withdrawals

    print("The remaining balance is:",initial)

main()
