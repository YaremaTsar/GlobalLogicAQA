import unittest
from car import Car, GasCar


class TestCar(unittest.TestCase):
    def test_car_is_abstract(self):
        with self.assertRaises(TypeError):
            car = Car("Renault", "Kangoo", 2022)

    def test_gas_car_refuel(self):
        gas_car = GasCar("Mazda", "5", 2017)
        gas_car.refuel(5)
        self.assertEqual(gas_car.fuel, 5)

    def test_gas_car_start_stop(self):
        gas_car = GasCar("Toyota", "Corolla", 2023)
        gas_car.refuel(10)
        self.assertEqual(gas_car.start(), "Starting gas engine")
        self.assertEqual(gas_car.stop(), "Stopping gas engine")
