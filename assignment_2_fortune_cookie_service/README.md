# Assignment 2 - Fortune Cookie Service

Now that we are comfortable with creating classes, objects, methods, attributes under objects, lets go a little further, and create a real service that is useful!

We will create a FortuneCookieService, capable of giving you a random fortune cookie.

Q: When would a fortune cookie service be useful?

A: There are some websites out there, that gives you random fortune cookies ya?

This is an actual implementation of how exactly they do that.

To be specific, they placed the functionality of creating a random fortune cookie under a single service; a class responsible for one thing; creating a random fortune cookie.

# Step 1: Create a class called FortuneCookieService

```python3
class FortuneCookieService:
    pass
```

# Step 2: Create a method called get_fortune_cookie

```python3
class FortuneCookieService:
    def get_fortune_cookie(self):
        pass
```

# Step 3: Add in a list of fortune cookies, and define it as an attribute called cookies

```commandline
class FortuneCookieService:
    def __init__(self, cookies: list[str]):
        self.cookies = cookies
        
    def get_fortune_cookie(self):
        pass
```

Q: Wait a minute, where do we get the fortune cookie

A: Ask chatgpt man

```python3
fortune_cookies = [
  "You will soon embark on a great adventure.",
  "A lifetime of happiness lies ahead of you.",
  "Good things come to those who wait.",
  "You will receive unexpected good news.",
  "Your hard work will pay off in the end.",
  "You will make a lifelong friend very soon.",
  "You will find success in all your endeavors.",
  "Your future looks very bright.",
  "Your creativity will lead to great success.",
  "You will find true love very soon.",
  "Your kindness will be repaid many times over.",
  "Your financial situation will greatly improve.",
  "You will achieve your dreams and goals.",
  "You will be blessed with good luck.",
  "Your future is full of promise and opportunity.",
  "Your intelligence will be recognized and rewarded.",
  "You will overcome any obstacle in your path.",
  "You will make a positive difference in the world.",
  "Your inner strength will guide you to success.",
  "You will receive a promotion or raise soon.",
  "Your talents will be put to good use.",
  "Your journey will be filled with happiness.",
  "You will meet someone very special soon.",
  "Your hard work and dedication will pay off.",
  "You will be successful in all your endeavors.",
  "Your life is full of love and happiness.",
  "You will find peace and contentment in your life.",
  "Your future is looking bright and sunny.",
  "You will make a significant impact on the world.",
]
```

# Step 4: Implement `get_fortune_cookie` to give back a random cookie from self.cookies

Hint: This is actually a leetcode easy question

Q: How do we select a random element from a list?

A: python has a library called random, and it contains functions to give you random functionality

**Method 1: Generate a random index from 0 to the length of self.cookies - 1**

If your cookies has 3 items, then the indexes it has is

0, 1 and 2

-> This means, we need to generate a random number from 0 to 2,

and pass it as the index into the list, to get a random cookie

```python3
import random

class FortuneCookieService:
    def __init__(self, cookies: list[str]):
        self.cookies = cookies
        
    def get_fortune_cookie(self) -> str:
        random_index: int = random.randint(0, len(self.cookies) - 1)
        cookie: str = self.cookies[random_index]
        return cookie
```

**Method 2: use random.choice to get a random cookie from self.cookies

```python3
import random

class FortuneCookieService:
    def __init__(self, cookies: list[str]):
        self.cookies = cookies
        
    def get_fortune_cookie(self) -> str:
        return random.choice(self.cookies)
```