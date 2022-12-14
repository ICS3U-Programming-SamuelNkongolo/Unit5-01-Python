#!/usr/bin/env python3
# Created By: Samuel Nkongolo
# Date: Nov. 26, 2022
# This program converts celsius to fahrenheit


# Using "def" to define a function.
def fahrenheit():
    # The try catch in this case allows decimals because temperature can be a decimal.
    try:
        celsius_temp = float(input("What is the temperature? (C): "))

        # The celsius to fahrenheit formula.
        fahrenheit_temp = (1.8 * celsius_temp) + 32
        print("{}(C) = {:.2f}(F)".format(celsius_temp, fahrenheit_temp))
    except:
        print("Your input is not a number.")


def main():
    # This function calls the fahrenheit function.
    fahrenheit()


# Calling the function that calls the fahrenheit function.
if __name__ == "__main__":
    main()
