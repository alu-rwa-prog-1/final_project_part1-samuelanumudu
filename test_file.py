# ------- Vehicle Parking System for Kigali Arena ------- #

# @Authors : Achille Tanwouo and Samuel Anumudu

# Test our program with Unittest Module
import unittest
from unittest import TestCase
from car_class import Car
from controller import Controller
from moto_class import Moto
from parking import CarParkingSlot, ParkingSlot
from truck_class import Truck


# Test Moto Class datatype of time ---------       TEST 1
class TestMoto(TestCase):
    def test_time_for_moto(self):
        moto_1 = Moto()
        self.assertEqual(type(moto_1.time), float)


# Test Car Class datatype of time ---------       TEST 2
class TestCar(TestCase):
    def test_time_for_car(self):
        car_1 = Car()
        self.assertEqual(type(car_1.time), float)


# Test Truck Class datatype of time ---------       TEST 3
class TestTruck(TestCase):
    def test_time_for_truck(self):
        truck_1 = Truck()
        self.assertEqual(type(truck_1.time), float)


# Test if Parking Slot capacity is 30 for all types vehicles--------      TEST 4
class TestParkingSlot(TestCase):
    def test_capacity(self):
        car_parking_slot_1 = CarParkingSlot('A')
        self.assertEqual(car_parking_slot_1.capacity, 30)


# Test default length of ParkingSlot ----------     TEST 5
class TestParkingSlot(TestCase):
    def test_initial_parkingSlot(self):
        parkingSlot = ParkingSlot("ParkingSlot_A")
        self.assertEqual(len(parkingSlot.lots), 0)

    def test_add_vehicle(self):
        parkingSlot_1 = ParkingSlot("A")
        parkingSlot_1.add_vehicle(Moto())
        parkingSlot_1.add_vehicle(Moto())
        parkingSlot_1.add_vehicle(Moto())
        self.assertEqual(len(parkingSlot_1.lots), 3)

    def test_view_details(self):
        parkingSlot_1 = ParkingSlot('A')
        parkingSlot_1.lots
        self.assertEqual(type(parkingSlot_1.lots), list)


# Test if Car class is an instance of Vehicle -------- TEST 6
class TestCar(TestCase):
    def test_is_instance(self):
        self.assertIsInstance(Car(), Car)


# Test if Truck class is an instance of Vehicle -------- TEST 7
class TestTruck(TestCase):
    def test_is_instance(self):
        self.assertIsInstance(Truck(), Truck)


# Test if Truck class is an instance of Vehicle -------- TEST 8
class TestMoto(TestCase):
    def test_is_instance(self):
        self.assertIsInstance(Moto(), Moto)


# This test assert True that Controller is a class-object ----- TEST 9
class TestController(TestCase):
    def test_class(self):
        controller_class = Controller()
        self.assertTrue(type(controller_class), True)


if __name__ == '__main__':
    unittest.main()
