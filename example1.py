#!python3

"""
The following program exits with invalid input if a float is entered 
and an int is expected.

Notice you will get a Traceback that tells you that you have a "ValueError"
You will get a similar error if you enter a string that can not be converted
to a number

"""

entry = input("Enter an integer:").strip()

print( int(entry) )