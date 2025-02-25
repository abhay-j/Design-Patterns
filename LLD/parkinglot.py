"""
You are tasked with designing a Parking Lot System that can manage vehicles parking and unparking in a multi-level parking lot. The system should handle different types of vehicles, parking spots, and payment calculations. The design should be scalable, modular, and adhere to object-oriented principles.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
################################## Parking Spot Class
class ParkingSpot(ABC):
    def __init__(self):
        self.vaccany = True
        self.vehicle = None
        self.id = None
    @abstractmethod
    def isVacant(self) -> bool:
        pass
    @abstractmethod
    def setVaccany(self, vaccancy : bool):
        pass
    @abstractmethod
    def park(self, vechicle : Vehicle) -> True:
        pass
    @abstractmethod
    def unpark(self):
        pass
    @abstractmethod
    def parkedVehicleId(self):
        pass



class SmallParkingSpot(ParkingSpot):
    def __init__(self):
        super().__init__()
           
    def isVacant(self) -> bool:
        return self.vaccany
    
    def setVaccany(self, vaccancy : bool):
        self.vaccany = vaccancy
    
    def park(self, vehicle : Vehicle) -> bool:
        if (self.isVacant() and vehicle.vehicleType() == 2):
            self.vehicle = vehicle
            self.vaccany = False
            return True
        else:
            return False
    
    def unpark(self):
        if self.vaccany == False:
            self.vaccany = True
            vehicle = self.vehicle
            self.vehicle = None
            return {"vehicle": vehicle, "slot_id": self.id}
        else:
            return "Slot is vaccant"
    
    def parkedVehicleId(self):
        if (self.vehicle):
            return self.vehicle.id
        else:
            return None
             
             

class MediumParkingSpot(ParkingSpot):
    def __init__(self):
        super().__init__()

    def isVacant(self) -> bool:
        return self.vaccany
    def setVaccany(self, vaccancy : bool):
        self.vaccany = vaccancy
        
    def park(self, vehicle : Vehicle):
        if (self.isVacant() and vehicle.vehicleType() == 4):
            self.vehicle = vehicle
            self.vaccany = False
            return True
        else:
            return False
    def unpark(self):
        if self.vaccany == False:
            self.vaccany = True
            vehicle = self.vehicle
            self.vehicle = None
            return {"vehicle": vehicle, "slot_id": self.id}
        else:
            return "Slot is vaccant"
    
    def parkedVehicleId(self):
        if (self.vehicle):
            return self.vehicle.id
        else:
            return None
    
        
       

class LargeParkingSpot(ParkingSpot): 
    def __init__(self):
        super().__init__()
    def isVacant(self) -> bool:
        return self.vaccany
    def setVaccany(self, vaccancy : bool):
        self.vaccany = vaccancy
    def park(self, vehicle : Vehicle):
        if (self.isVacant() and vehicle.vehicleType() == 6):
            self.vehicle = vehicle
            self.vaccany = False
            return True
        else:
            return False
    def unpark(self):
        if self.vaccany == False:
            self.vaccany = True
            vehicle = self.vehicle
            self.vehicle = None
            return {"vehicle": vehicle, "slot_id": self.id}
        else:
            return "Slot is vaccant"
    def parkedVehicleId(self):
        if (self.vehicle):
            return self.vehicle.id
        else:
            return None
###################################### Vehicle class
class Vehicle(ABC):
    def __init__(self, id : str):
        self.id = id

    @abstractmethod
    def vehicleType(self) -> int:
        pass

class TwoWheeler(Vehicle):
    def __init__(self, id):
        super().__init__(id)
        
    def vehicleType(self) -> int:
        return 2

class FourWheeler(Vehicle):
    def __init__(self, id):
        super().__init__(id)
        
    def vehicleType(self) -> int:
        return 4

class Truck(Vehicle):
    def __init__(self, id):
        super().__init__(id)
        
    def vehicleType(self) -> int:
        return 6

    
########################################## Level 
class Level():
    def __init__(self, level, small_spots, medium_spots, large_spots):
        self.level = level
        self.small_spots = small_spots
        self.medium_spots = medium_spots
        self.large_spots = large_spots
        self.layout = []
        self.allVehicleIds = set()
    
    def create_layout(self):
        for i in range(0,self.small_spots):
            spot = SmallParkingSpot()
            spot.id = f"{self.level}S{i+1}"
            self.layout.append(spot)
            
        for j in range(0, self.medium_spots):
            spot = MediumParkingSpot()
            spot.id = f"{self.level}M{j+1}"
            self.layout.append(spot)
        
        for k in range(0, self.large_spots):
            spot = LargeParkingSpot()
            spot.id = f"{self.level}L{k+1}"
            self.layout.append(spot)
        
        
    
    def getAllVehicleIds(self):
        for spot in self.layout:
            vehicle_id = spot.parkedVehicleId()
            if vehicle_id :
                self.allVehicleIds.add(vehicle_id)
        return self.allVehicleIds
    
    
     
########################################### Parking Manager
class ParkingManager():
    def park(self, vehicle: Vehicle, level: Level):
        allVehicleIds = level.getAllVehicleIds()
        
        # Check if vehicle is already parked
        if vehicle.id in allVehicleIds:
            return f"Vehicle with ID {vehicle.id} is already parked"
        
        vehicleType = vehicle.vehicleType()
        
        # For Two Wheeler (type 2)
        if vehicleType == 2:
            # First try to find a small spot
            for spot in level.layout:
                if isinstance(spot, SmallParkingSpot) and spot.isVacant():
                    if spot.park(vehicle):
                        return f"Vehicle with ID {vehicle.id} parked successfully at spot {spot.id}"
            
            # If no small spot, try medium spot
            for spot in level.layout:
                if isinstance(spot, MediumParkingSpot) and spot.isVacant():
                    if spot.park(vehicle):
                        return f"Vehicle with ID {vehicle.id} parked successfully at spot {spot.id}"
            
            # If no medium spot, try large spot
            for spot in level.layout:
                if isinstance(spot, LargeParkingSpot) and spot.isVacant():
                    if spot.park(vehicle):
                        return f"Vehicle with ID {vehicle.id} parked successfully at spot {spot.id}"
        
        # For Four Wheeler (type 4)
        elif vehicleType == 4:
            # First try to find a medium spot
            for spot in level.layout:
                if isinstance(spot, MediumParkingSpot) and spot.isVacant():
                    if spot.park(vehicle):
                        return f"Vehicle with ID {vehicle.id} parked successfully at spot {spot.id}"
            
            # If no medium spot, try large spot
            for spot in level.layout:
                if isinstance(spot, LargeParkingSpot) and spot.isVacant():
                    if spot.park(vehicle):
                        return f"Vehicle with ID {vehicle.id} parked successfully at spot {spot.id}"
        
        # For Truck (type 6)
        else:
            # Only try large spots
            for spot in level.layout:
                if isinstance(spot, LargeParkingSpot) and spot.isVacant():
                    if spot.park(vehicle):
                        return f"Vehicle with ID {vehicle.id} parked successfully at spot {spot.id}"
        
        # If we get here, no spot was found
        return f"No vacant spot available for vehicle with ID {vehicle.id}"        
    
    def unpark(self, vehicle_id: str, level: Level):
    # Check if vehicle exists in this level
        if vehicle_id not in level.getAllVehicleIds():
            return f"Vehicle with ID {vehicle_id} not found in this level"
        
        # Search for the vehicle in all spots
        for spot in level.layout:
            if not spot.isVacant() and spot.parkedVehicleId() == vehicle_id:
                # Found the vehicle, unpark it
                result = spot.unpark()
                
                # Update the set of parked vehicle IDs
                level.allVehicleIds.remove(vehicle_id)
                
                # Return success message with details
                return f"Vehicle with ID {vehicle_id} successfully removed from spot {result['slot_id']}"
        
        # This should not happen if getAllVehicleIds() is accurate,
        # but included as a failsafe
        return f"Vehicle with ID {vehicle_id} found in records but not in any spot"
            

if __name__ == "__main__":
    car = FourWheeler('TS!@#$8')  
    level1 = Level(1, small_spots = 10, medium_spots = 8, large_spots = 5)
    level1.create_layout()
    parkingmanager = ParkingManager()
    print(parkingmanager.park(car,level1 ))
    print(level1.getAllVehicleIds())
    print(parkingmanager.unpark(car.id, level1))
    
    
    
    