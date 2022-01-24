__author__ = 'Ella Seaman'
#02/08/2021


def main():
    value = int(input("What is the total number of months? "))
    months = value % 12
    years = value // 12

    print("The total time for", value,"months is: Total years:", years,"Total months:", months,)
main()