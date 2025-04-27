from sympy import *

def prime_number():
    while True:
        input_number = input("please write a number,or type quit to exit:")
        if input_number == "":
            print("please write a valid number")
            continue
        if input_number.lower() == "quit":
            break

        try:
            guessed_number = int(input_number)
            if guessed_number <= 0:
                print("the number must be positive number")
                continue
            if isprime(guessed_number):
                print("this number is a prime number,meaning it can only be divided by 1 and itself")
            else:
                print("this number is not a prime number")
        except ValueError:
            print("invalid input,please write a valid number")


prime_number()
