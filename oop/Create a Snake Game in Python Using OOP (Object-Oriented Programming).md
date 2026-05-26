Create a Snake Game in Python Using OOP (Object-Oriented Programming)
=====================================================================

![](https://miro.medium.com/v2/resize:fit:1260/1*X0St6mHxsAfvtDoLNqm1bw.png)

This tutorial will guide you through creating a classic Snake game using Python and its Turtle library, employing object-oriented programming (OOP) principles such as classes, inheritance, and instantiation.

---

Basic OOP Concepts in Python
----------------------------

Class
-----

A class in Python is a blueprint for creating objects. It defines a set of attributes and methods that the created objects (instances) can use.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass
```

---

Inheritance
-----------

Inheritance allows a new class to inherit attributes and methods from an existing class. This helps in code reusability and building upon existing code.

```python
class Dog(Animal):
    def speak(self):
        return "Woof!"
```

---

Instantiation
-------------

Instantiation is the creation of an instance (object) from a class. When you instantiate a class, you're creating a unique object from that blueprint.

```python
my_dog = Dog("Buddy")
print(my_dog.name)  # Output: Buddy
print(my_dog.speak())  # Output: Woof!```
```

---

Key Concepts of the Turtle Library in Python
--------------------------------------------

The Turtle library in Python is a popular way to introduce graphical programming. It is a standard Python library for drawing and creating digital art. Let's explore some key concepts that will be useful in our Snake game project.

---

Turtle Screen
-------------

The Turtle Screen is the playground for the turtles. It's where all the drawing happens

```python
import turtle
screen = turtle.Screen()
screen.title("My Turtle Game")
screen.bgcolor("black")
```

In this example, we create a screen, set its title, and background color.

Turtle Object
-------------

A Turtle object is used to draw on the screen. We can create as many turtles as we want.

```python
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("white")
```

Here, we create a Turtle object, set its shape to "turtle", and color to "white".

---

Moving the Turtle
-----------------

The Turtle can move in different directions using methods like `forward()`, `backward()`, `left()`, and `right()`.

```python
my_turtle.forward(100)
my_turtle.right(90)
```

---

Drawing Control
---------------

You can control the drawing of the turtle, like lifting the pen up or putting it down, and setting the speed of movement.

```python
my_turtle.penup()
my_turtle.goto(100, 100)
my_turtle.pendown()
```

---

Event Handling
--------------

Turtle allows you to bind functions to keypresses, making it interactive.

```python
def move_up():
    my_turtle.setheading(90)
    my_turtle.forward(10)
screen.onkey(move_up, "Up")
screen.listen()
```

This code will move the turtle up when the "Up" arrow key is pressed.

---

Project Structure
-----------------

Our Snake game will consist of four Python files:

`main.py`: The main game loop and window setup.

`snake.py`: Defines the Snake class.

`food.py`: Defines the Food class.

`scoreboard.py`: Manages the game's scoreboard

---

main.py
-------

This file sets up the game window and controls the game's main loop.

from turtle import Turtle, Screen

```python
from turtle import Turtle, Screen
# import time
from time import sleep
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
screen  = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("AliceBlue")
screen.title("my snake game")

starting_positions = [(0,0), (-20,0), (-40,0)]
serpent = Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on = True
sleep_speed = 0.1
screen.listen()
screen.onkey(serpent.up, "Up")
screen.onkey(serpent.down, "Down")
screen.onkey(serpent.left, "Left")
screen.onkey(serpent.right, "Right")

while game_is_on:
    screen.update()
    sleep(sleep_speed)
    serpent.move()
    # detect collision with food
    if serpent.segments[0].distance(food) < 15:
        food.refresh()
        serpent.extend()
        scoreboard.increase_score()
    # detect collision with wall
    if serpent.segments[0].xcor() > 280 or serpent.segments[0].xcor() < -280 or serpent.segments[0].ycor() > 280 or serpent.segments[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        scoreboard.reset()
        sleep(5)
        screen.bye()

screen.exitonclick()
```

---

# snake.py

This file defines the Snake class.

```python
from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("green")
            new_segment.goto(position)
            self.segments.append(new_segment)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        #set speed to 0 to make it move instantly
        self.segments[0].speed(0)
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("green")
        new_segment.goto(position)
        self.segments.append(new_segment)
```

---

## food.py

Here, we define the Food class.

```python
from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("khaki")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

```

---

## scoreboard.py

This file contains the Scoreboard class.

```python
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
    def reset(self):
        self.clear()
        self.update_scoreboard()
        self.score = 0
        self.update_scoreboard()
```

---
