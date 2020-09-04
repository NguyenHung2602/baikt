# baikt

Q1. What is the difference between list and tuples in Python?
Danh sách không cần phải luôn đồng nhất.
danh sách là một loại vùng chứa trong Cấu trúc dữ liệu, được sử dụng để lưu trữ nhiều dữ liệu cùng một lúc
Tuple cũng là một kiểu dữ liệu trình tự có thể chứa các phần tử của các kiểu dữ liệu khác nhau, 
nhưng chúng là bất biến về bản chất
Tuple là một tập hợp các đối tượng Python được phân tách bằng dấu phẩy

Q2. What are the key features of Python?
  1. Easy to code
  2. Free and Open Source
  3. Object-Oriented Language
  4. GUI Programming Support
  5. High-Level Language
  6. Extensible feature
  7. Python is Portable language
  8. Python is Integrated language
  9. Interpreted Language
  10. Large Standard Library
  11. Dynamically Typed Language

Q3. What type of language is python?
 Python is an interpreted, high-level and general-purpose programming language
 Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code 
 readability with its notable use of significant whitespace.

Q4. How is Python an interpreted language?
Python is called an interpreted language because it goes through an interpreter, 
which turns code you write into the language understood by your computer's processor. ... 
Python is an “interpreted” language. 
This means it uses an interpreter. An interpreter is very different from the compiler.

Q5. What is pep 8?
 is a document that provides guidelines and best practices on how to write Python code. 
 It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. ... 
 PEP stands for Python Enhancement Proposal, and there are several of them.

Q6. How is memory managed in Python?
The Python memory manager manages chunks of memory called “Blocks”. 
A collection of blocks of the same size makes up the “Pool”. 
Pools are created on Arenas, chunks of 256kB memory allocated on heap=64 pools. 
If the objects get destroyed, the memory manager fills this space with a new object of the same size

Q7. What is name space in Python?
 A namespace is a system to have a unique name for each and every object in Python. 
 An object might be a variable or a method. Python itself maintains a namespace in the form of a Python dictionary. ... 
 Its Name (which means name, an unique identifier) + Space(which talks something related to scope)

Q8. What is PYTHON PATH?
PYTHONPATH is an environment variable which you can set to add additional directories where 
python will look for modules and packages. For most installations, you should not set these 
variables since they are not needed for Python to run. 
Python knows where to find its standard library.

Q9. What are python modules?
A module is a Python object with arbitrarily named attributes that you can bind and reference. ... 
Simply, a module is a file consisting of Python code. 
A module can define functions, classes and variables. A module can also include runnable code.

Q10. What are local variables and global variables in Python? Please give an exam
Local variables can only be reached within their scope(like func() above).
exam :def sum(x,y):
      sum = x + y
      return sum
      print(sum(5, 10))  

A global variable can be used anywhere in the program as its scope is the entire program.
exam: z = 25
      def func():
        global z
        print(z)
        z=20
        func()
        print(z)
        
Q11. What is __init__?
 "__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts.
  This method called when an object is created from the class and it allow the class to initialize the 
  attributes of a class

Q12. What is self in Python?
The self is used to represent the instance of the class. With this keyword, 
you can access the attributes and methods of the class in python. 
It binds the attributes with the given arguments. ... 
In Python, we have methods that make the instance to be passed automatically, but not received automatically.
