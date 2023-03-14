# Assignment 1 - Creating a Calculator Service in Python

Classes are commonly used for two purposes in software engineering:

1. Classes as Data Models. We use classes to model how data should look like.
2. Classes as Services. We use classes to package methods which do one thing and do it well 

Now you smart parrots might ask:

Q: Gimme an example of a Data Model!

Here you go! Here is a simple class `ParrotModel` which represents the attributes of a Parrot.

```python3
class ParrotModel:
    def __init__(self, name: str, age: int, color: str):
        """
        Define a special function called the Constructor
        This constructor is called when we create a Parrot object 
        
        To create the object, we call the class name as if it were a function
        ```
        polly: ParrotModel = ParrotModel(name="Polly", age=2, color="Green")
        ```
        """
        self.name = name
        self.age = age
        self.color = color

if __name__ == "__main__":
    polly: ParrotModel = ParrotModel(name="Polly", age=2, color="Green")
    # print the attributes of the parrot
    print(polly.name)
    print(polly.age)
    print(polly.color)
```

Q: How about a service? Gimme an example of a service!

Here you go! Here is a simple service class `SeedStorageService` which helps us store and count seeds!

```python3
class SeedStorageService:
    def __init__(self):
        self.seeds = 0
    
    def save_seeds(self, seeds: int):
        """
        This method takes in a number of seeds, and adds them to the storage
        """
        self.seeds += seeds

    def count_seeds(self) -> int:
        """
        This method returns the number of seeds in the storage
        """
        return self.seeds

if __name__ == "__main__":
    seed_storage_service: SeedStorageService = SeedStorageService()
    seed_storage_service.save_seeds(10)
    seed_storage_service.save_seeds(20)
    seed_storage_service.save_seeds(30)
    total_seeds: int = seed_storage_service.count_seeds()
    # prints 60
    print(total_seeds)
```

In this first assignment, we will reinforce our understanding of 

- Classes as Services
- Defining Methods in Services

## Create a Calculator Service

We define a class like this

```python3
class YourClassName:
    # continue from here
    pass
```

and create a constructor (`__init__`) like this:

```python3
class YourClassName:
    def __init__(self):
        # continue your implementation here
        pass
```

The calculator will be able to perform the following operations:

1. Addition

```python3
def add(a: int, b: int) -> int:
    """
    adding two numbers give back an int    
    """
    pass
```

2. Subtraction

```python3
def subtract(a: int, b: int) -> int:
    """
    subtracting a with b gives back an int
    """
    pass
```

3. Multiplication

```python3
def multiply(a: int, b: int) -> int:
    """
    multiplying two numbers gives back an int
    """
    pass
```

4. Division

```python3
def divide(a: int, b: int) -> float:
    """
    dividing two numbers in python gives back a float
    """
    pass
```

Complete this implementation of the `CalculatorService` class and create a `main.py` file to test your implementation.

## Bonus: Understanding @staticmethod

We can define a method in a class as a `staticmethod` like this:

```python3
class YourClassName:
    @staticmethod
    def your_method_name():
        pass
```

This means that the method does not need to be called on an instance of the class. It can be called directly on the class name.

```python3
YourClassName.your_method_name()
```

Now you smart parrots might ask:

**Q: When exactly should we mark a method with the @staticmethod decorator?**

A: Great question! We do that when a method doesn't rely on any attributes of the object!

As the add, subtract, multiply and divide methods do not need to be called on an instance of the `CalculatorService` class, we can define them as `staticmethod`.

Decorate your methods in the `CalculatorService` class with the `@staticmethod` decorator.

and create a `main.py` file to test your implementation.
