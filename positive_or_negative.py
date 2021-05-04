#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program tells the user if a number is positive or negative


def main():
    # This function tells the user if their number is positive or negative

    # Input
    print("This program checks if a number is positive or negative.")
    print("")
    integer = int(input("Enter an integer: "))

    # Process & Output
    if integer >= 1:
        print("{} is a positive number.".format(integer))
    elif integer <= -1:
        print("{} is a negative number.".format(integer))
    else:
        print("0 is just a zero!")
    print("\nDone.")


if __name__ == "__main__":
    main()
