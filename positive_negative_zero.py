#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: March 2022
# This program tell user if the number positive or negative


def main():

    number = int(input("Enter the number:"))
    print("")

    if number == 0:
        print("Zero")
    elif number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("No idea")


if __name__ == "__main__":
    main()
