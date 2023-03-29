from abc import ABC, abstractmethod
"""
Simple code with absract methods

Yarema Tsar
"""


class Car(ABC):
    """Car class"""
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    @abstractmethod
    def start(self):
        """start of motor"""
        pass # pylint: disable=unnecessary-pass

    @abstractmethod
    def stop(self):
        """stop of motor"""
        pass # pylint: disable=unnecessary-pass


class GasCar(Car):
    """Car on GAS"""
    def __init__(self, name, model, year):
        super().__init__(name, model, year)
        self.fuel = 0

    def start(self):
        """Start driving"""
        if self.fuel > 0:
            return "Starting gas engine"
        else:
            return "Out of gas, cannot start engine"

    def stop(self):
        """Stop driving"""
        return "Stopping gas engine"

    def refuel(self, amount):
        """refuel in Car"""
        self.fuel += amount
