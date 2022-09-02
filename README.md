# Python-Complete-Guide

## What is Python?
           ---> Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. 
           
           ---> Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.  
           
           ---> Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance.
           
           ---> Python supports modules and packages, which encourages program modularity and code reuse.
 

## Variables types in Python:
           ---> Python has 2 types of variables - Global and Local.
           
                ---> Global Variables: When you want to use the same variable for rest of your program or module you declare it as a global variable.
                
                ---> Local Variable: If you use the variable in a specific function or method, you use a local variable while Python variable declaration.


## Data types in Python:
           ---> Python has several data types -
           
                ---> Number: In Numbers, there are mainly 3 types which include Integer, Float, and Complex.
                
                ---> String: We can use single quotes or double quotes to represent strings. Multi-line strings can be represented using triple quotes, ”’ or “””.Strings are immutable which means once we declare a string we can’t update the already declared string.
                
                ---> List: A list can contain a series of values. Are declared by using brackets [ ]. A list is mutable, which means we can modify the list.
                
                ---> Tuple: A tuple is a sequence of Python objects separated by commas. Tuples are immutable, which means tuples once created cannot be modified. Tuples are defined using parentheses ().
                
                ---> Set: A set is an unordered collection of items. Set is defined by values separated by a comma inside braces { }.
                
                ---> Dictionary: Dictionaries are the most flexible built-in data type in python. Dictionaries items are stored and fetched by using the key. Dictionaries are used to store a huge amount of data. To retrieve the value we must know the key. In Python, dictionaries are defined within braces {}.   
               
               ---> Booleans: Logical values True or False
               
## Naming convention in Python:   
           --->A variable name must start with a letter or the underscore character.
           
           ---> A variable name cannot start with a number.
           
           ---> A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
           
           ---> Variable names are case-sensitive (age, Age and AGE are three different variables).
           
           ---> You can't use reserve keywords.
           
## Operator types in Python:   
           ---> Arithmetic operators
                      ---> Addittion:       x + y
                      ---> Substraction:    x - y
                      ---> Multiplicaion:   x * y
                      ---> Division:        x / y
                      ---> Modulus:         x % y
                      ---> Exponential:     x ** y
                      ---> Floor Dvision:   x // y
                      
           ---> Assignment operators
                      --->   =       :      x = 5
                      --->   +=      :      x += 3
                      --->   -=      :      x -= 3
                      --->   *=      :      x *= 3
                      --->   /=      :      x /= 3
                      --->   %=      :      x %= 3
                      --->  //=      :      x //= 3
                      --->  **=      :      x **= 3
                      --->   &=      :      x &= 3
                      --->   |=      :      x |= 3
                      --->   ^=      :      x ^= 3
                       --->  >>=     :      x >>= 3
                      --->   <<=     :      x <<= 3
                      
           ---> Comparison operators                          
                      ---> Equal:                        x == y
                      ---> Not equal:                    x != y
                      ---> Greater than:                 x > y
                      ---> Less than:                    x < y
                      ---> Greater than or equal to:     x >= y
                      ---> Less than or equal to:        x <= y                     

           ---> Logical operators
                      ---> and : Returns True if both statements are true :                x < 5 and  x < 10
                      ---> or  : Returns True if one of the statements is true :           x < 5 or x < 4
                      ---> not : Reverse the result, returns False if the result is true : not(x < 5 and x < 10)
 
           ---> Identity operators
                      ---> is      : Returns True if both variables are the same object     :  x is y
                      ---> is not  : Returns True if both variables are not the same object :  x is not y                     
                      
           ---> Membership operators
           
           ---> Bitwise operators

## Loop types in Python: 
           ---> For Loop
           ---> Here's the general format for a for loop in Python:
                      for item in object:
                                  statements to do stuff
           ---> Example: 
                      for num in list1:
                                 print(num)

           ---> While Loop
           ---> The general format of a while loop is:
                      while test:
                                  code statements
                      else:
                                  final code statements
           ---> Example: 
                      x = 0
                      while x < 10:
                            print('x is currently: ',x)
                            print(' x is still less than 10, adding 1 to x')
                            x+=1
    
                      else:
                            print('All Done!')
 
## break, continue, pass in Python:  
           ---> break: Breaks out of the current closest enclosing loop.
           ---> continue: Goes to the top of the closest enclosing loop.
           ---> pass: Does nothing at all.
           ---> Format:
                      while test: 
                                 code statement
                                 if test: 
                                       break
                                 if test: 
                                       continue 
                                 else:
