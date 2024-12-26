from __future__ import annotations
from abc import ABC, abstractmethod
""" 
The Decorator Pattern is a structural design pattern that lets you attach new behaviors to objects by placing them inside wrapper objects that contain these behaviors.

Key Components:

1. Component Interface:
   - Defines the interface for objects that can have responsibilities added to them dynamically

2. Concrete Component:
   - Defines the basic object that can have responsibilities added to it
   - Implements the Component interface

3. Decorator Base Class:
   - Maintains a reference to a Component object
   - Implements the same interface as Component
   - Delegates all work to the wrapped component

4. Concrete Decorators:
   - Add responsibilities to the component
   - Override methods from the Decorator base class
   - Execute their behavior before or after calling the parent method

Main Benefits:
- Provides more flexibility than static inheritance
- Supports Single Responsibility Principle
- Allows behaviors to be added at runtime
- Avoids feature-laden classes high up in the hierarchy

Common Use Cases:
- Adding optional features to objects
- Data manipulation (compression, encryption)
- UI component enhancement
- Cross-cutting concerns (logging, validation)

Drawbacks to Remember:
- Can create many small objects
- Order of decorators can matter
- Complex to debug due to layers of wrapping

This pattern follows the Open/Closed Principle: open for extension (new behaviors) but closed for modification (existing code).
"""

""" 
LLD : 
Objective
Create a system that calculates the price of a pizza based on its ingredients. This system will be used to support a pizza restaurant by computing the cost dynamically.

Pizza Composition
A pizza is composed of the following components:

Base: The crust type (e.g., thin, regular, cheesy crust)

Size: The pizza size (e.g., small, medium, large)

Toppings: A list of zero or more toppings (e.g., olives, cheese, pepperoni)

Price Formula
Price=(Base Price + Sum of Topping Prices) × Size Multiplier

Pricing Details
Bases:
Thin crust: $8
(Other bases can be added later.)

Toppings:
Cheese topping: $2
(Additional toppings can be added later.)

Sizes (multipliers):
Small: 0.75
Medium: 1.0
(Other sizes can be added later.)

Example Calculations
Small Thin Crust Cheese Pizza:
Price=($8+$2)×0.75=$7.50
Price=($8+$2)×0.75=$7.50

Medium Thin Crust Cheese Pizza:
Price=($8+$2)×1.0=$10.00
Price=($8+$2)×1.0=$10.00


"""

#Base class interface
class BasePizza(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass 
    

# concrete base clasas
class ThinCrust(BasePizza):
    def cost(self) -> float:
        return 8.0

#concrete base class
class RegularCrust(BasePizza):
    def cost(self) -> float:
        return 9.0


#decorator base class for size
class PizzaDecorator(BasePizza):
    _basePizza = None
    def __init__(self, basePizza) -> None:
        self._basePizza = basePizza
    
    def cost(self) -> float:
        return self._basePizza.cost()

#concrete decorator for small size
class SmallSize(PizzaDecorator):
    def cost(self) -> float:
        return super().cost()  * 0.75

#concrete decorator for medium size 
class MediumSize(PizzaDecorator):
    def cost(self) -> float:
        return super().cost() * 1.0



#concrete decorator for Toppings 
class CheeseTopping(PizzaDecorator):
    def cost(self) -> float:
        return super().cost() + 2.0


#order : Small thin crust pizza with cheese topping 
order_1 = SmallSize(CheeseTopping(ThinCrust()))
print(f"Your order total is: ${order_1.cost()}")

#order : Medium thin crust pizza with cheese topping 
order_2  = MediumSize(CheeseTopping(ThinCrust()))
print(f"Your order total is: ${order_2.cost()}")










        


    


