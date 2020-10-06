## SDSS Computing Studies Python Assignment
### Assignment #006 Exceptions (Total Marks 12)

Objectives:
* Develop options to handle errors
* Raise exceptions if a program has an error

You may have had your programs come up with errors in the Autograder, 
for which you have been unsure why an error has occurred.  Often, it 
is because the program has quit or exited due to an error in syntax 
or some kind of semantic error.  For example, you may have tried to
convert a string to an integer, when it is really a float.  
You will get an error occur that says it is a "ValueError"
see example1.py

To have the program continue operation, we often make use of a 
code structure called the "try...except...finally".

In this code structure, you can "try" a block of code to test
for errors.  If an error is found, the "except" block of code
will be executed.  The "finally" block is optional, but 
will be executed whether the try was successful or not.
see example1b.py

### XX Tasks

##### Task 1
(x points) 

