#!python3
"""
format:

try:
    # block of code to be tried out
    # that might throw an error
except:
    # This is the block of code to be run if an error occurs
finally:
    # this block will be executed regardless of whether an error occurs or not
    # optional, not really necessary
"""
positive = False

try:
    a = input("Enter a number:").strip()
    if a > 0:
        positive = True
        print("The number is positive")
except:
    print("There was an error. Did you remember to turn a into a float?")
    positive = False
