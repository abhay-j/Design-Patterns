""" 
Factory pattern is used when we want to create objects based on a choice. 
The client just states the choice and the factory method returns the object of the choice to the client
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class ShapeFactory(ABC):
    
    @abstractmethod
    def factoryMethod(self):
        pass
    

class SquareFactory(ShapeFactory):
    def factoryMethod(self) -> Shape:
        return Square()
    

class CircleFactory(ShapeFactory):
    def factoryMethod(self) -> Shape:
        return Circle()




class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing a circle"

class Square(Shape):
    def draw(self):
        return "Drawing a square"
    
    
if __name__ == "__main__":
    squarefactory = SquareFactory()
    circlefactory = CircleFactory()
    
    squareshape = squarefactory.factoryMethod()
    msg1 = squareshape.draw()
    print(msg1)
    
    circleshape = circlefactory.factoryMethod()
    msg2 = circleshape.draw()   
    print(msg2) 
    