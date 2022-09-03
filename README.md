# Python-Complete-Guide

## What is Python?
           ---> Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. 
           
           ---> Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development,                   as well as for use as a scripting or glue language to connect existing components together.  
           
           ---> Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance.
           
           ---> Python supports modules and packages, which encourages program modularity and code reuse.
 

## Variables types in Python:
           ---> Python has 2 types of variables - Global and Local.
           
                ---> Global Variables: When you want to use the same variable for rest of your program or module you declare it as a global variable.
                
                ---> Local Variable: If you use the variable in a specific function or method, you use a local variable while Python variable declaration.


## Data types in Python:
           ---> Python has several data types -
           
                ---> Number: In Numbers, there are mainly 3 types which include Integer, Float, and Complex.
                
                ---> String: We can use single quotes or double quotes to represent strings. Multi-line strings can be represented using triple quotes, ”’ or                                “””.Strings are immutable which means once we declare a string we can’t update the already declared string.
                
                ---> List: A list can contain a series of values. Are declared by using brackets [ ]. A list is mutable, which means we can modify the list.
                
                ---> Tuple: A tuple is a sequence of Python objects separated by commas. Tuples are immutable, which means tuples once created cannot be modified.                          Tuples are defined using parentheses ().
                
                ---> Set: A set is an unordered collection of items. Set is defined by values separated by a comma inside braces { }.
                
                ---> Dictionary: Dictionaries are the most flexible built-in data type in python. Dictionaries items are stored and fetched by using the key.                                Dictionaries are used to store a huge amount of data. To retrieve the value we must know the key. In Python, dictionaries are defined within                            braces {}.   
               
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

## Methods in Python: 
           ---> Methods perform specific actions on an object and can also take arguments, just like a function.
           ---> Methods are in the form:
                     object.method(arg1,arg2,etc..
           ---> Some methods for a list are:
                                            append
                                            count
                                            extend
                                            insert
                                            pop
                                            remove
                                            reverse
                                            sort
           ---> Example: 
                      list = [1,2,3,4,5]
                      list.reverse()

## Function in Python: 
           ---> Function: 
                      --> Is a useful device that groups together a set of statements so they can be run more than once. 
                      --> They can also let us specify parameters that can serve as inputs to the functions. 
                      --> Functions will be one of most basic levels of reusing code in Python.
            
           ---> def keyword
                --> We begin with def then a space followed by the name of the function. 
                --> Try to keep names relevant, for example len() is a good name for a length() function. 
                --> Also be careful with names, you wouldn't want to call a function the same name as a built-in function in Python (such as len). 
                
           ---> Format: 
                      def name_of_function(arg1,arg2):
                           //
                           This is where the function's Document String (docstring) goes.
                           When you call help() on your function it will be printed out.
                            //
                      // Do stuff here
                      // Return desired result
           
           ---> Example:
                      def say_hello():
                      print('hello')
                      
           ---> Call the function:
                      say_hello()
                      
           ----> Using return:
                      def add_num(num1,num2):
                      return num1+num2
            
           ---> Accepting parameters (arguments)
                      def greeting(name):
                          print(f'Hello {name}')
                          greeting('Jose')
 
 ## What is the difference between return and print?
           ---> The return keyword allows you to actually save the result of the output of a function as a variable.The print() function simply displays the output to                 you, but doesn't save it for future use. 

 ## Some useful operatot in Python
           ---> Range Method: The range function allows you to quickly generate a list of integers.
           ---> Example: Notice how 11 is not included, up to but not including 11, just like slice notation!
                      list(range(0,11))
                      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                      
          ---> enumerate Method: Often, when dealing with iterators, we also get need to keep a count of iterations. Python eases the programmers’ task by providing                                    a built-in function enumerate() for this task. Enumerate() method adds a counter to an iterable and returns it in a form of                                            enumerating object. This enumerated object can then be used directly for loops or converted into a list of tuples using the list()                                      method.
          ---> Syntax: enumerate(iterable, start=0)
          
          ---> Zip Method: Python zip() method takes iterable or containers and returns a single iterator object, having mapped values from all the containers. 
          ---> Syntax :  zip(*iterators) 

## Object-Oriented Programming in Python
          ---> In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. 
          ---> It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming.
          
          ---> Main Concepts of Object-Oriented Programming:
                      Class
                      Objects
                      Polymorphism
                      Encapsulation
                      Inheritance
                      Data Abstraction
                      
           ---> Python class: 
                      --> Classes are created by keyword class.
                      --> Attributes are the variables that belong to a class.
                      --> Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute     
               
            ---> Class Definition Syntax:
                      class ClassName:
                                 # Statement-1
                                 .
                                 .
                                 .
                                  # Statement-N  
            
            ---> Self in Python class:
                      --> self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in python. 
                      --> It binds the attributes with the given arguments.
                                 ---> Points on Self:
                                            ---> Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter                                                    when we call the method, Python provides it
                                            ---> If we have a method that takes no arguments, then we still have to have one argument.
                                            ---> This is similar to this pointer in C++ and this reference in Java.  
           
            ---> init in Python:
                      __init__ is one of the reserved methods in Python. In object oriented programming, it is known as a constructor. The __init__ method can be                             called when an object is created from the class, and access is required to initialize the attributes of the class.
                      
            ---> Python Object: The object is an entity that has a state and behavior associated with it.
                      ---> An object consists of :
                                 State: It is represented by the attributes of an object. It also reflects the properties of an object.
                                 Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
                                 Identity: It gives a unique name to an object and enables one object to interact with other objects.
                      
                      ---> Object Syntax: 
                                 obj = Dog()
             
            ---> Inheritance in Python:
                      ---> Inheritance is the capability of one class to derive or inherit the properties from another class.
                      ---> Types of Inheritance – 
                                 ---> Single Inheritance:
                                            Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.

                                 ---> Multilevel Inheritance:
                                            Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits                                             properties from his parent class.

                                 ---> Hierarchical Inheritance:
                                            Hierarchical level inheritance enables more than one derived class to inherit properties from a parent class.

                                 ---> Multiple Inheritance:
                                            Multiple level inheritance enables one derived class to inherit properties from more than one base class.
                                            
             ---> Polymorphism in Python
                      ---> Polymorphism simply means having many forms. For example, we need to determine if the given species of birds fly or not, using polymorphism                            we can do this using a single function.
                      
             ---> Encapsulation in Python
                      ---> It describes the idea of wrapping data and the methods that work on data within one unit. 
                      ---> This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. 
                      ---> To prevent accidental change, an object’s variable can only be changed by an object’s method. 
                      ---> Those types of variables are known as private variables.
                     
             ---> Data Abstraction in Python
                      ---> It hides the unnecessary code details from the user. 
                      ---> Also,  when we do not want to give out sensitive parts of our code implementation and this is where data abstraction came.

        
