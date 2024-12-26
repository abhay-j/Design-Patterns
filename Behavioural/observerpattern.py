from __future__ import annotations
from abc import ABC, abstractmethod

from typing import List
""" 
Design a "Notify Me" feature for an e-commerce platform with the following requirements:
Users should be able to click a "Notify Me" button for out-of-stock products.
The system should store user requests for notifications.
When a product becomes available, the system should send notifications to interested users.
The notification process should be efficient and scalable.
Users should be able to unsubscribe from notifications.
"""

""" 
Observer Pattern : 
We will use "Observer Design Pattern" to implement this feature. 
In the Observer Design Pattern we have an "Observable" entity, the change in which will be notified to the "Observer" entity 

The Observable interface will have a "register" function that will register observers, who will be notified upon the change in the Observable. 
It will also have "remove" function which will remove the observer from the registry. 
We will have a "notify" method which will be called to notify all the registered observer. 
we will have a "setState" and "getState" methods to update the state, retrive the state of our observable respectively 

Interface Observable : 
    # The Observable interface will have a "register" function that will register observers, who will be notified upon the change in the Observable.
    register ()  
    
    #It will also have "remove" function which will remove the observer from the registry. 
    remove() 
    
    #We will have a "notify" method which will be called to notify all the registered observer. 
    notify()
    
    #we will have a "setState" and "getState" methods to update the state, retrive the state of our observable respectively 
    setState()
    getState()



Interface Observer():
    # has a relationship with the observable
    # implements an "update()" method that uses the updated state of the "Observable"
    update():

"""


#Observer Interface
class UserObserverInterface(ABC):
    
    @abstractmethod
    def update(self):
        pass
    
#Observable Interface
class OOS_ObservableInterface(ABC):
    @abstractmethod
    def register(self, userObserver : UserObserverInterface):
        pass
    
    @abstractmethod
    def deregister(self, userObserver : UserObserverInterface):
        pass
    
    @abstractmethod
    def notify(self):
        pass
    
    @abstractmethod
    def setStatus(self, val : bool):
        """ 
        changes the status of data that is being observed.
        """
        pass
    
    @abstractmethod
    def getStatus(self):
        """
        recieves the current status of the data
        """
        pass

#concrete class (USER AKA Observer)
class User(UserObserverInterface):
    def __init__(self,OOS_Observable, name, email):
        self.OOS_Observable = OOS_Observable
        self.name = name 
        self.email = email
          
    def update(self):
        print(f"notified Item status to {self.name} as {self.OOS_Observable.getStatus()}")
    
        

#concrete class (OutOfStock AKA Observalbe)
class OutOfStock(OOS_ObservableInterface):
    _state: bool = False
    _users: list[User] = []
    
    def register(self, user : User):
        self._users.append(user)
        print(f"{user.name} registered for updates")
    
    def deregister(self, user: User):
        self._users.remove(user)
        
    def notify(self):
        for user in self._users:
            user.update()
    def setStatus(self, val : bool):
        self._state = val
    def getStatus(self):
        return self._state

outOfStockNotifier = OutOfStock()
# Instantiate actual User objects
user1 = User(outOfStockNotifier, "Abhay", "jabhay2023@gmail.com")
user2 = User(outOfStockNotifier, "Rishabh", "rishabh@gmail.com")
# users registered for updates 
outOfStockNotifier.register(user1)
outOfStockNotifier.register(user2)

#print initial status of the product
print(f"Initial Status: {outOfStockNotifier.getStatus()}")

#updated the status of the prodcut
outOfStockNotifier.setStatus(val=True)

#current status of the product
print(f"Updated Status: {outOfStockNotifier.getStatus()}")

#send out notifications to the registered users
outOfStockNotifier.notify()



    
    
    
         
        
        
    
    
    

    


