# PCAP-31-03-Preparation

## NOTE: THIS IS NOT A REPLACEMENT FOR THE OFFICIAL PCAP-31-03 EXAM PREPARATION GUIDE PROVIDED BY THE PYTHON INSTITUTE. THIS IS A PERSONAL REPOSITORY OF NOTES, CODE, AND RESOURCES USED TO PREPARE FOR THE PCAP-31-03 EXAM.

## [PCAP-31-03 EXAM SYLLABUS](https://pythoninstitute.org/assets/627e61fa6fe27591613128.pdf)

# Learning Path: Advanced Python Modules and Packages

## 1.1 Import and Use Modules and Packages

- [Official Python Documentation on Modules](https://docs.python.org/3/tutorial/modules.html)
- [Importing in Python: A Complete Guide](https://realpython.com/absolute-vs-relative-python-imports/)
- [The import system on Python](https://docs.python.org/3/reference/import.html)

### Learning Resources

- [Python Institute’s Official Page](https://edube.org/study/pe2) - This page provides a comprehensive overview of the PCAP certification, including the exam format and the topics covered.
- [KDnuggets Article](https://www.kdnuggets.com/2021/09/python-pcap-certification-roadmap-resources.html) - This article provides a roadmap, resources, and tips for success based on the author’s personal experience.
- [iSecPrep Article](https://www.isecprep.com/2021/12/11/python-institute-pcap/) - This article suggests starting on the Python Institute’s page dedicated to the exam, where you’ll find learning resources such as the instructor-led training course, exam prep video, and the official practice test.
- [GitHub Repository](https://github.com/BCutkelvin/PCAP-Preperation) - This repository contains notes, code, and resources used to prepare for the PCAP exam.

## Advanced Qualifying for Nested Modules

- [Python - Packages](https://www.tutorialspoint.com/python/python_modules.htm)
- [Understanding Python's Import](https://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html)

## The `dir()` Function

- [Python dir() Function](https://www.w3schools.com/python/ref_func_dir.asp)
- [Exploring Python Through Its Internals: The `dir()` Function](https://realpython.com/courses/exploring-python-internals-dir-function/)

## The `sys.path` Variable

- [Understanding sys.path for Absolute Beginners](https://realpython.com/courses/sys-path-python/)
- [Python sys.path](https://www.tutorialspoint.com/python/os_sys_path.htm)

## Create and Use User-Defined Modules and Packages

- [Creating and Using Python Packages](https://realpython.com/courses/creating-and-using-python-packages/)
- [Python Modules and Packages – An Introduction](https://www.learnpython.org/en/Modules_and_Packages)

## Nested Packages vs. Directory Trees

- [Structuring Your Project](https://docs.python-guide.org/writing/structure/)
- [PEP 420 - Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420/)

## 1.2 Perform evaluations using the math module ceil(), floor(), trunc(), factorial(), hypot(), sqrt()

- **`ceil()`, `floor()`, `trunc()`, `factorial()`, `hypot()`, `sqrt()`**
  - [Python Documentation on math Module](https://docs.python.org/3/library/math.html)
  - [Real Python - Python's math Module: Everything You Need to Know](https://realpython.com/courses/pythons-math-module/)

## 1.3 Generate Random Values using the `random` Module

The `random` module in Python provides various functions for generating random numbers and values. Here are resources specifically covering the functions `random()`, `seed()`, `choice()`, and `sample()`:

- [Python Documentation on `random` Module](https://docs.python.org/3/library/random.html)

  - The official documentation provides detailed information about the `random()` function and its usage.

- [GeeksforGeeks - Random module in Python](https://www.geeksforgeeks.org/python-random-module/)

  - This GeeksforGeeks article covers the basics of the `random()` function and provides examples of usage.

- `choice()` and `sample()` Functions
- `seed()` and `sample()` Functions

Explore these resources to gain a comprehensive understanding of the `random()` module's key functions for generating random values in Python.

## 1.4 – Discover host platform properties using the platform module

- [Python Documentation on `platform` Module](https://docs.python.org/3/library/platform.html)
- Functions:
  [`platform()`](https://www.geeksforgeeks.org/python-platform-module/)
  [`machine()`](https://docs.python.org/3/library/platform.html#platform.machine)
  [`processor()`](https://docs.python.org/3/library/platform.html#platform.processor)
  [`version()`](https://docs.python.org/3/library/platform.html#platform.processor)
  [`system()`](https://docs.python.org/3/library/platform.html#platform.system)

## 1.5 Create and use user-defined modules and packages

- [Understanding Python's **init**.py](https://www.udacity.com/blog/2021/11/__init__-in-python-an-overview.html)
- [What is **init**.py?](https://stackoverflow.com/questions/448271/what-is-init-py-for)
- [What's the **pycache** folder?](https://stackoverflow.com/questions/16869024/what-is-pycache)
- [Official PEP 3147 -- PYC Repository Directories](https://www.python.org/dev/peps/pep-3147/)
- [Official PEP 420 -- Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420/)
- [What does the if **name** == “**main**”: do?](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/)

# 2 Handle Errors using Python-Defined Exceptions

- **`except`, `except:-except`, `except:-else:`, `except (e1, e2)`**

  - [Python Documentation on Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
  - [Python Exception Handling]()
  - [Real Python - Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)

- **Hierarchy of Exceptions**

  - [Python Exception Hierarchy](https://docs.python.org/3/library/exceptions.html)

- **`raise`, `raise ex`**

  - [Python raise Statement](https://www.w3schools.com/python/ref_keyword_raise.asp)
  - [Real Python - The Python return Statement and Exceptions]()

- **`assert`**

  - [Python assert Statement](https://realpython.com/python-assert-statement/)

- **`except E as e`**

  - [Understanding Python Exception Handling](https://stackabuse.com/python-exception-handling/)

- **Extend the Python Exceptions Hierarchy with Self-Defined Exceptions**
  - [Creating Custom Exceptions in Python](https://realpython.com/lessons/creating-exceptions-python/)
  - [Python Custom Exceptions](https://www.programiz.com/python-programming/user-defined-exception)

# 3 Strings

## 3.1 Understand machine representation of characters

#### **`How encoding in python works`**

- [How to Encode and Decode Strings in Python](https://realpython.com/python-encodings-guide/)
- [Python String encode() Method](https://www.w3schools.com/python/ref_string_encode.asp)
- [How to Unicode](https://docs.python.org/3/howto/unicode.html)

## 3.2 Operate on strings

- [ord](https://www.w3shools.com/python/ref_func_ord.asp)
- [chr](https://docs.python.org/3/library/functions.html#chr)
- **`String indexing, slicing,immutability`**
  - [Python String Indexing](https://www.w3schools.com/python/python_strings_index.asp)
  - [Python String Slicing](https://www.w3schools.com/python/python_strings_slicing.asp)
  - [Python String Immutability](https://www.w3schools.com/python/gloss_python_string_immutable.asp)
  - [A Good explanation of String Immutability](https://stackoverflow.com/questions/9097994/arent-python-strings-immutable-then-why-does-a-b-work/40702094#40702094)

# 4 Object-Oriented Programming

### Introduction

    Learn the basic concepts and terminology of OOP, such as abstraction, encapsulation, inheritance, and polymorphism.
    Understand the benefits and drawbacks of using OOP in Python.

### Resources:

[Object-Oriented Programming (OOP) With Python Learning Path – Real Python](https://realpython.com/learning-pathsobject-oriented-programming-oop-python/)

- Go to Python Institute’s and take [Python Essentials 2 (Free – Edube Interactive™, an OpenEDG Education Platform)](https://edube.org/study/pe2)
- Also is a good idea look for [PCAP Programming Essentials in Python (Cisco Networking Academy, Part 2, Modules 1-4)](https://www.netacad.com/courses/programming/pcap-programming-essentials-python)

## Classes and Objects

    Learn how to create and use classes and objects in Python, as well as their attributes and methods.
    Learn how to use constructors, destructors, and special methods to customize your classes and objects.
    Learn how to use class variables, instance variables, and class methods to manage data and behavior at different levels.

### Resources:

- [Using Python Class Constructors (Course) – Real Python](https://realpython.com/learning-paths/object-oriented-programming-oop-python/)
- [Providing Multiple Constructors in Your Python Classes (Course) – Real Python](https://realpython.com/learning-paths/object-oriented-programming-oop-python/)
- [Supercharge Your Classes With Python super() (Course) – Real Python](https://realpython.com/learning-paths/object-oriented-programming-oop-python/)
- [Managing Attributes With Python’s property() (Course) – Real Python](https://realpython.com/learning-paths/object-oriented-programming-oop-python/)
- [Python Descriptors: An Introduction (Tutorial) – Real Python](https://realpython.com/python-descriptors/)

### Inheritance and Composition

    Learn how to use multiple inheritance, abstract classes, and interfaces to design complex and flexible hierarchies.
    Learn how to use the diamond problem, method resolution order, and mixins to resolve conflicts and enhance your classes.

### Resources:

- [Inheritance and Composition: A Python OOP Guide (Course) – Real Python](https://realpython.com/inheritance-composition-python/)
- Python 3 Multiple Inheritance (Article) – Programiz
### Polymorphism and Overloading

    Learn how to use polymorphism and overloading to make your classes and objects more adaptable and versatile.
    Learn how to use duck typing, operator overloading, and function overloading to change the behavior of your classes and objects based on different contexts and inputs.
    Learn how to use magic methods, decorators, and descriptors to implement advanced overloading techniques and customize your classes and objects.

### Resources:

### Understand the Object-Oriented approach

### Resources:

- `class, object, property, method, encapsulation,
inheritance, superclass, subclass, identifying class components`

1. [Python Official Documentation on Classes](https://docs.python.org/3/tutorial/classes.html)
2. [Real Python - Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)
3. [GeeksforGeeks - Python Classes and Objects](https://www.geeksforgeeks.org/python-classes-and-objects/)
4. [TutorialsPoint - Python Object-Oriented](https://www.tutorialspoint.com/python/python_classes_objects.htm)
5. [Corey Schafer's YouTube - Python OOP Tutorial](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)

#### introspection and the hasattr() function (objects vs classes)

- a really good explanation of the difference between using hasattr() with an object and a class itself (https://stackoverflow.com/questions/29900715/hasattr-on-class-names)
- [`__name__`](https://docs.python.org/3/library/stdtypes.html#definition.__name__)
- [`__module__`](https://peps.python.org/pep-3130/#rationale-for-module)
- [`__bases__`](https://docs.python.org/3/library/stdtypes.html#definition.__name__)
- [`__dict__`](https://docs.python.org/3/library/stdtypes.html#definition.__name__)
- [`__doc__`](https://docs.python.org/3/library/stdtypes.html#definition.__name__)

### Miscellaneous
- [List Comprehensions](https://www.python.org/dev/peps/pep-0202/#rationale)
- [Lambdas](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
- [Lambdas](https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/)
- [Self-defined-functions](https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/)
- [map(),filter()](https://www.geeksforgeeks.org/python-map-function/?ref=gcse)
- [filter()](https://www.geeksforgeeks.org/filter-in-python/?ref=lbp)
