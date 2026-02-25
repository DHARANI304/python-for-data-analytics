Python for Data Analytics – Learning Journey
This repository documents my daily progress in learning Python with a focus on
Data Analytics. It covers Python fundamentals, functional programming, and data
handling concepts through hands-on practice.

Day 1 – Python Data Types & Collections
*Learned basic Python data types: tuple, set, dictionary
*Practiced set operations and understood that sets store unique values
*Created dictionaries using zip()
* Understood mutable vs immutable data structures

Day 2 – Functions in Python
*Learned how to define functions
*Practiced:
*Functions without return values
*Functions with return values
*Understood function calling and parameter passing

Day 3 – Arguments & Control Flow
*Explored different types of function arguments:
*Positional arguments
*Keyword arguments
*Default arguments
*Variable-length arguments (*args)
*Practiced user input handling
*Wrote programs using conditional statements:
*Even/Odd check
*Vowel/Consonant
*Voting eligibility
*Leap year check
*Divisibility checks
*Learned basic use of exec() (executing user input code)

Day 4 – Math, Lambda & Functional Programming
*Used Python’s math module for mathematical operations
*Learned and practiced lambda functions
*Applied lambda with:
  map()
  filter()
  reduce()
*Implemented reduce logic using both def and lambda
*Strengthened understanding of functional programming concepts

Day 5 – Advanced Functions & Modules
*Learned higher-order functions (functions returning functions)
*Practiced table generation using lambda functions
*Implemented factorial using recursion (without built-in functions)
*Worked with string concatenation
*Used the turtle module to draw polygons
*Practiced accessing nested data structures (list, tuple, set, dictionary)

Day 6 – Python Lists & Operations
*Learned list slicing techniques
*Practiced adding, deleting, and modifying list elements
*Used list methods:
*insert(), extend(), pop(), del
*Learned list replication
*Understood shallow copy vs slicing copy
*Verified object identity using id()

Day 7 – List Manipulation & Shallow Copy
* Practiced advanced list slicing  
* Inserted and extended elements in lists  
* Deleted portions of lists using slicing and del  
* Used pop() to remove elements  
* Added multiple elements in the middle of a list  
* Replicated lists using multiplication operator  
* Copied lists using copy() and slicing  
* Compared object identities using id()  
* Understood shallow copy behavior with nested lists  

Day 8 – List Comprehension & Conditional Logic

* Learned list comprehension (important concept)  
* Generated cube of numbers using:  
  * Traditional for loop  
  * Single-line list comprehension  
* Separated even and odd numbers using loops  
* Used conditional list comprehension  
* Applied inline if-else inside list comprehension  
* Strengthened logic building using conditions  

Day 9 – List Traversal & Built-in Functions

* Accessed list elements using for loop  
* Used range(len()) to access index and value  
* Used enumerate() to get index and value together  
* Traversed nested lists  
* Reversed lists using slicing  
* Sorted lists using sorted()  
* Sorted in descending order  
* Performed membership checks using in keyword  

 Day 10 – Tuples & Tuple Operations

* Created tuples with single and multiple values  
* Practiced tuple unpacking  
* Used placeholder variable (_) during unpacking  
* Accessed tuple elements using indexing  
* Used negative indexing  
* Accessed nested tuple elements  
* Iterated through tuples using loops  
* Used enumerate() with tuples  
* Performed tuple concatenation  
* Applied tuple slicing  
* Reversed tuples using slicing  

Day 11 – Sets & Set Operations

*Created sets with unique elements
*Understood that sets do not allow duplicate values
*Performed set union using | and union()
*Performed set intersection using & and intersection()
*Used difference() to find elements present in one set but not the other
*Used symmetric difference ^ to get unique elements from both sets
*Added elements to a set using add()
*Removed elements using remove()
*Used discard() to remove elements safely (without error if not present)
*Iterated through sets using loops
*Generated new sets using set comprehension
*Applied conditional logic inside set comprehension
*Calculated squares and cubes based on even/odd conditions
*Found common elements between two sets and performed operations on them

Day 12 – Dictionaries & Dictionary Operations

*Created dictionaries with key–value pairs
*Accessed dictionary values using keys
*Used get() method to access values safely
*Added new key–value pairs
*Updated existing dictionary values
*Removed elements using pop()
*Used popitem() to remove the last inserted pair
*Used del keyword to delete specific keys
*Retrieved all keys using keys()
*Retrieved all values using values()
*Retrieved key–value pairs using items()
*Iterated through dictionaries using loops
*Used dictionary comprehension
*Created dictionaries from lists using zip()
*Checked if a key exists in a dictionary
*Nested dictionaries and accessed nested values

 Day 13 – Zip Function, Built-in Functions & Strings

*Used zip() function to combine multiple iterables
*Created a dictionary using dict(zip(keys, values))
*Iterated over zipped objects using loops
*Practiced all() function to check if all elements are True
*Practiced any() function to check if at least one element is True
*Worked with different ways of creating strings
*Used single quotes, double quotes, and triple quotes
*Checked memory reference using id() function
*Observed string immutability behavior
*Accessed individual string characters using indexing
*Performed string formatting using format() method

Day 14 – String Methods & Operations

*Practiced different string case conversion methods like upper(), lower(), title(), and capitalize()
*Used searching methods like find(), index(), and count()
*Checked string properties using isalpha(), isdigit(), isalnum(), and isspace()
*Verified starting and ending characters using startswith() and endswith()
*Performed string replacement using replace() method
*Split strings into lists using split() method
*Joined list elements into strings using join() method
*Removed extra spaces using strip(), lstrip(), and rstrip()
*Practiced combining multiple string methods together
*Improved understanding of real-time string manipulation techniques

Day 15 – Regular Expressions (RegEx)
Imported and used Python’s built-in re module
*Used re.match() to check patterns at the beginning of a string
*Used re.search() to find patterns anywhere in a string
*Used re.findall() to extract all matching patterns
*Used re.sub() to replace patterns in a string
*Learned special characters in RegEx:
    . (any character)
    ^ (starts with)
    $ (ends with)
    *, +, ? (quantifiers)
*Worked with character classes:
    [a-z], [A-Z]
    [0-9]
    \d, \w, \s
*Practiced validating:
  *Email patterns
  *Phone numbers
  *Numeric-only strings
  *Understood grouping using parentheses ()
  *Used raw strings r"" for writing patterns properly

Day 16 – Regular Expressions (Advanced Practice)

*Revised Regular Expression concepts
*Imported and used the re module
*Practiced match() to check patterns at the beginning
*Used search() to find patterns anywhere in the string
*Used findall() to extract multiple matches
*Replaced text patterns using sub()
*Worked with special symbols like ., ^, $, *, +, ?
*Used character classes like [a-z], [A-Z], [0-9]
*Practiced shorthand patterns like \d, \w, \s
*Validated email and numeric formats
*Used grouping with parentheses ()
*Applied raw strings r"" for writing regex patterns correctly
*Practiced real-time input validation examples

Day 17 – NumPy Introduction & Array Basics

NumPy

*Imported NumPy library using import numpy as np
*Created NumPy arrays using array()
*Converted Python lists into NumPy arrays
*Checked array type using type()
*Checked array dimensions using ndim
*Checked shape of array using shape
*Checked size of array using size
*Accessed elements using indexing
*Performed array slicing
*Created 1D and 2D arrays
*Understood difference between Python lists and NumPy arrays
*Performed basic arithmetic operations on arrays
*Observed vectorized operations in NumPy