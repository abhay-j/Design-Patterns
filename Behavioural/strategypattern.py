

from abc import ABC, abstractmethod

"""
Create a basic drive strategy that can be used to derive further drive strategies such as "NormalStrategy" or "SportStrategy"
"""

class Drive(ABC):
    @abstractmethod
    def drive(self):
        pass


""" 
The Following are the concrete implmentations of this strategy
Eg. NormalStrategy , SportStrategy 
"""

class NormalStrategy(Drive):
    def drive(self):
        return "This is a normal drive strategy"

class SportStrategy(Drive):
    def drive(self):
        return "This is a sport strategy"

#lets have the base class "Vehicle"
class Vehicle:
    def __init__(self, drive_strategy):
        self.drive_strategy = drive_strategy
    
    def drive(self):
        return self.drive_strategy.drive()
        
    
# creating vehicles 

class GoodsVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalStrategy())

class OffRoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(SportStrategy())

class SportsVehicle(Vehicle):
    pass

# instances 

offy = OffRoadVehicle()
normy = GoodsVehicle()
print(normy.drive())