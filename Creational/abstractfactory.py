from __future__ import annotations
from abc import ABC, abstractmethod
""" 
The Abstract Factory Pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. It is particularly useful when a system needs to be independent of how its objects are created, composed, and represented.
"""
""" 
Problem Statement: Computer Parts Manufacturing System

You are tasked with designing a system for a company that manufactures computer parts. The company produces GPUs and Monitors, and these parts are branded under two different brands: MSI and ASUS. The system should allow the company to easily expand to new brands or new types of computer parts in the future without modifying existing code.

Requirements:

Product Families:
The company manufactures two types of products: GPUs and Monitors.
Each product has two variants: MSI and ASUS.
Product Interfaces:
Define an interface for each type of product:
GPU: Represents a graphics processing unit.
Monitor: Represents a computer monitor.
Concrete Products:
Implement the GPU interface for:
MsiGpu: Represents an MSI-branded GPU.
AsusGpu: Represents an ASUS-branded GPU.
Implement the Monitor interface for:
MsiMonitor: Represents an MSI-branded monitor.
AsusMonitor: Represents an ASUS-branded monitor.
Abstract Factory:
Define an abstract factory interface called Company that declares methods for creating GPUs and Monitors:
create_gpu(): Creates a GPU.
create_monitor(): Creates a Monitor.
Concrete Factories:
Implement the Company interface for each brand:
MsiManufacturer: Creates MSI-branded GPUs and Monitors.
AsusManufacturer: Creates ASUS-branded GPUs and Monitors.
Client:
The client code should be able to create and use GPUs and Monitors without knowing their concrete classes.
The client should work with any brand (MSI or ASUS) by simply switching the factory.
Scalability:
The system should be designed in such a way that adding new brands (e.g., Gigabyte) or new types of products (e.g., Keyboards) does not require modifying existing code.
Example Scenario:

The company wants to manufacture and test GPUs and Monitors for both MSI and ASUS.
The client code should be able to create a GPU and a Monitor for a specific brand and display their details.
"""





class Monitor(ABC):
    @abstractmethod
    def assemble(self) -> str:
        pass
    
class GPU(ABC):
    @abstractmethod
    def assemble(self) -> str:
        pass

class MSIMonitor(Monitor):
    def assemble(self):
        return "MSI Monitor Assembly functions"
class MSIGPU(GPU):
    def assemble(self):
        return "MSI GPU Assembly functions"
    
class AsusMonitor(Monitor):
    def assemble(self):
        return "ASUS Monitor Assembly functions"
class AsusGPU(GPU):
    def assemble(self):
        return "ASUS GPU Assembly functions"
    

class Company(ABC):
    @abstractmethod
    def create_gpu(self) -> GPU:
        pass
    @abstractmethod
    def create_monitor(self) -> Monitor:
        pass

class AsusCompany(Company):
    
    def create_gpu(self) -> GPU:
        return AsusGPU()
    
    def create_monitor(self) -> Monitor:
        return AsusMonitor()


class MSICompany(Company):
    
    def create_gpu(self) -> GPU:
        return MSIGPU()
    
    def create_monitor(self) -> Monitor:
        return MSIMonitor()


def client(factory : Company):
    gpu = factory.create_gpu()
    monitor = factory.create_monitor()
    
    print(gpu.assemble())
    print(monitor.assemble())

if __name__ == "__main__":
    print("Testing client code for MSI")
    client(MSICompany())
    
    print("Testing client code for Asus")
    client(AsusCompany())