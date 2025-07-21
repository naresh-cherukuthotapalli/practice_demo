
#   Python 🐍 Concepts And FastAPI ⚡ CRUD Operations

## Overview
This guide introduces you to the fundamental concepts of Python and CRUD operations using FastAPI, combining clear explanations, practical code examples, and real-world insights for Python web API development.

This guide follows a progressive flow:
- What is Python
- What is Generator
- What is Decorators
- What is Lamda Function
- What is Dictionary
- What is List
- What is FastAPI
- What are CRUD Operations
---


## Section 1: Python Definition

### what is python?
**Python** Python is a high-level, interpreted programming language used to instruct a computer to perform specific tasks. It supports object-oriented programming and is known for its simplicity, readability, and versatility.

### Example Python code
```python
# Input from user
num1 = float(input("Enter any number: "))

sum = num1 + num2

# Display the result
print("Number:", sum)
```
**Key Points:**
- Easy to read and understand
- Interpreted language
- Object-oriented programming language

## Section 2: Generators

**Generators**:Generators in Python are a special type of iterable that produce values one at a time, only when needed. Unlike lists, which store all elements in memory, generators yield values on demand, making them highly efficient for handling large datasets or infinite sequences.


### Example
```python
def char_by_char(text):
    for char in text:
        yield char

for ch in char_by_char("Python"):
    print(ch)
```
**Key Points:**
  - Processing large files: Read data line by line instead of loading the entire file.
  - Lazy computations: Evaluate data only when needed, ideal for streams or real-time data.
  - Infinite sequences: Generate endless data.

---

## Section 3: Decorators

**Decorators**: A decorator in Python is a special function that modifies or enhances the behavior of another function without altering its original code. It wraps the target function, allowing additional code to run before or after the function executes—making decorators a powerful tool for code reuse, abstraction, and cleaner program design.

### Example
```python
def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

```
### Handling Arguments
```python
def decorator_name(func):
    def wrapper(*args, **kwargs):
        # Add functionality before the original function call
        result = func(*args, **kwargs)
        # Add functionality after the original function call
        return result
    return wrapper

@decorator_name
def function_to_decorate():
    # Original function code
    pass
```

### Class-Based Decorators
```python
class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Called {self.count} times")
        return self.func(*args, **kwargs)

@CallCounter
def greet():
    print("Hello!")

```
**Key Points**
  - Logging
  - Authentication and access control
  - Timing and profiling functions.

## Section 4: Lamda Function
**Lamda**: Python Lambda Functions are anonymous functions means that the function is without a name. As we already know the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function
  - *arguments* : one or more parameters, just like a regular function.
  - *expression* : a single expression whose result will be returned automatically.

### Syntax
``` python
lambda arguments: expression
```

### Example
```python
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7

```
### Lamda function as an Argument
``` python
numbers = [1,2,3]
map(lambda x: x**2, numbers)
```

## Section 5: Dictionary
**Dictionary**: A dictionary in Python is a built-in data type used to store data in key-value pairs. Keys must be unique and immutable (such as strings, integers, or tuples), while values can be of any type and may be duplicated. Dictionaries are mutable, so you can add, modify, or remove items after creation.
### Syntax
```python
dict = {
          "key1":"value1",
          "key2":"value2",
          "key3":"value3"
       }
```

### Example
```python
person = {
    "name": "Vamsi",
    "age": 25,
    "city": "Hyderabad"
}
```
### Accessing and Modifying Values
**To access a value**
- **Syntax**
  ```python
   dictionary_name["key"]
  ````
- **Example**

  ```python
    person["name"]
  ```
**To remove a key-value pair**
- **Example**
  ```python
    del person["name"]
  ```
**To add or update a value:**
- **Example**
  ```python
   person["state"] = "telangana"
  ```
**Key Ponints**
  - Highly efficient for retrieval using keys
  - Commonly used for representing structured data (like JSON), fast lookups, and flexible data storage.

## Section 6: List
**List**: A list in Python is a built-in, mutable data structure designed to store an ordered collection of items, which can be of any type (numbers, strings, objects, even other lists). Lists are extremely versatile and are among the most commonly used data types in Python for managing collections of data
### Syntax
**Creating list**
  ```python
  list_name = ["value1","value2","value3"]
  ```
**Creating list with list() constructor**
  ```python
  empty = list()
  from_tuple = list((1, 2, 3))
  ```

### Example
```python
fruits = ["apple", "cherry", "orange", "banana"]
```
### Accessing and Modifying Values
**To access a value**
- **Syntax**

  ```python
   list_name[index_number]
  ````
- **Example**

  ```python
    fruits[0]
  ```
**To remove a key-value pair:**
- **Example**
  ```python
    fruits.remove("banana")  # Removes first Occurence of banana
    fruits.pop()   # Removes last item
    fruits.clear() # Removes all items
  ```
**To add a value:**
- **Example**
  ```python
   fruits.append("orange")   # Adds to end
   fruits.insert(1, "kiwi")  # Inserts at index 1
   fruits.extend(["pear", "melon"])  # Appends multiple items
  ```
- **To Update a value:**
- **Example**
  ```python
    fruits[0] = "grape"
  ```
**To Slice LIst:**
- **Example**
  ```python
    print(fruits[1:3])       # Returns a sublist with elements at index 1 and 2
  ```
---
**Key Points:**
  - Ordered: Elements retain the order in which they are added; order is preserved when you iterate over the list
  - Mutable: You can modify, add, or remove elements after creation.

## Section 7: FastAPI
**FastAPI**: FastAPI is a modern and high-performance Python web framework used to build APIs quickly and efficiently. Designed with simplicity it allows developers to create RESTful APIs using Python's type hints which also enable automatic validation and error handling
### Example FastAPI
from fastapi import FastAPI
app = FastAPI()
```python
@app.get("/")
async def home():
  return {"Wlcome"}
```
## Section 8: Setup and Install
To Include FastAPI library in your project install fastapi
```python
     pip install fastapi uvicorn
 ```

## Section 9: CRUD operations in Fastapi
- CRUD refers to the basic operations that can be performed on data in a database. It stands for Create, Read, Update, and Delete, and it represents the fundamental functionalities that are essential for managing data in most applications.
  - CREATE: It involves adding new data to the database. In FastAPI, we can create data by sending a POST request to the appropriate endpoint.
  - READ: It involves retrieving existing data from the database. In FastAPI, we can perform Read operations using GET requests.
  - UPDATE: It involves updating existing data in the database. In FastAPI we can perform an Update operation using PUT/PATCH, PUT allows us to update the entire database whereas PATCH allows us to modify specific fields in the database.
  - DELETE: It involves deleting existing data from the database. In FastAPI we can perform a Delete Operation using DELETE requests.
### Example FastAPI with post method
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    branch: str
    id_no: float
    gender: str

@app.post("/items/")
async def register_student(item: Student):
    return item

```
## Section 10: Operation Mapping
- Create: POST /items/
- Read (List): GET /items/
- Read (Single): GET /items/{item_id}
- Update: PUT /items/{item_id}
- Delete: DELETE /items/{item_id}
## Section 11: Knowledge Check - Interview Questions

1. What is Python?
2. What is Dynamic Programming?
3. What is a generator in Python? Why are they used?
4. How do you create a generator in Python?
5. What is the difference between a generator and a list in Python?
6. How do decorators differ from regular functions?
7. How do you write a decorator that accepts arguments?
8. Can decorators be used for methods as well as functions?
9. How do lambda functions differ from regular functions?
10. Can a lambda function be defined inside another function?
11. How do you access values in a dictionary?
12. Are Python dictionaries mutable?
13. How do you add or update key-value pairs in a dictionary?
14. Can lists store different data types?
15. How do you create an empty list?
16. How do you check if a value exists in a list?
17. What is slicing in Python?
18. What does CRUD stand for and how is it represented in FastAPI?
19. Describe how Pydantic models are used in CRUD operations?
20. Which HTTP methods are used for each CRUD operation in FastAPI?
## Conclusion
- This guide provides you with both conceptual understanding and practical coding experience, enabling you to confidently apply Python fundamentals and build APIs using FastAPI.