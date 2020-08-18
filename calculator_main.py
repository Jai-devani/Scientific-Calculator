#!/usr/bin/env python3
"""
This script prompts a user to select a scientific calculator operation and enter data to get result
"""

import math

def addition(first_no=0, second_no=0):
    """Addition"""
    answer = first_no+second_no
    return answer

def subtraction(first_no=0, second_no=0):
    """Subtraction"""
    answer = first_no-second_no
    return answer

def multiplication(first_no=0, second_no=0):
    """Multiplication"""
    answer = first_no * second_no
    return answer

def division(first_no=0, second_no=0):
    """Division"""
    if first_no > 0 and second_no > 0:
        answer = first_no/second_no
    else:
        answer = "The arguments provided are invalid."
    return answer

def power(first_no=0, second_no=0):
    """Power"""
    answer = first_no**second_no
    return answer

def square_root(first_no=0):
    """Addition"""
    if first_no >= 0:
        answer = math.sqrt(first_no)
    else:
        answer = "The arguments provided are invalid."
    return answer

def modulus(first_no=0, second_no=0):
    """Modulus"""
    if first_no > 0 and second_no > 0:
        answer = first_no % second_no
    else:
        answer = "The arguments provided are invalid."
    return answer

def factorial(second_no=0):
    """Factorial"""
    if second_no >= 0:
        first_no = second_no
        second_no = 1
        while first_no > 1:
            second_no *= first_no
            first_no = first_no - 1
        answer = second_no
    else:
        answer = "The arguments provided are invalid."
    return answer

def sin(second_no=0):
    """Sine"""
    answer = round(math.sin(float(float((math.pi/180)*(float(second_no))))), 2)
    return answer

def cos(second_no=0):
    """Cosine"""
    answer = round(math.cos(float(float((math.pi/180)*(float(second_no))))), 2)
    return answer

def tan(second_no=0):
    """Tan"""
    answer = round(math.tan(float(float((math.pi/180)*(float(second_no))))), 2)
    return answer

def log(first_no=0, second_no=0):
    """Logarithim"""
    if first_no > 0 and second_no >= 2:
        answer = round(math.log(float(first_no), int(second_no)), 2)
    else:
        answer = "The arguments provided are invalid."
    return answer

if __name__ == "__main__":
    print("Scientific Calulator\n")
    print("1.Add\n2.Sub\n3.Mul\n4.Div\n5.Power\n6.Square Root")
    print("7.Modulus \n8.Factorial\n9.Sin\n10.Cos\n11.Tan\n12.Log")
    CHOICE = input(("Enter your choice:"))
    ANSWER = 0
    if CHOICE == "1":
        FIRST = float(input("Enter data:"))
        SECOND = float(input("Enter data:"))
        print(addition(FIRST, SECOND))
    elif CHOICE == "2":
        FIRST = float(input("Enter data:"))
        SECOND = float(input("Enter data:"))
        print(subtraction(FIRST, SECOND))
    elif CHOICE == "3":
        FIRST = float(input("Enter data:"))
        SECOND = float(input("Enter data:"))
        print(multiplication(FIRST, SECOND))
    elif CHOICE == "4":
        FIRST = float(input("Enter data:"))
        SECOND = float(input("Enter data:"))
        print(division(FIRST, SECOND))
    elif CHOICE == "5":
        print(power(FIRST, SECOND))
    elif CHOICE == "6":
        FIRST = float(input("Enter data:"))
        print(square_root(FIRST))
    elif CHOICE == "7":
        FIRST = float(input("Enter data:"))
        SECOND = float(input("Enter data:"))
        print(modulus(FIRST, SECOND))
    elif CHOICE == "8":
        SECOND = float(input("Enter data:"))
        print(factorial(SECOND))
    elif CHOICE == "9":
        SECOND = float(input("Enter data:"))
        print(sin(SECOND))
    elif CHOICE == "10":
        SECOND = float(input("Enter data:"))
        print(cos(SECOND))
    elif CHOICE == "11":
        SECOND = float(input("Enter data:"))
        print(tan(SECOND))
    elif CHOICE == "12":
        FIRST = float(input("Enter data:"))
        SECOND = float(input("Enter data:"))
        print(log(FIRST, SECOND))
    else:
        print("Invalid Choice. Good Bye !")
