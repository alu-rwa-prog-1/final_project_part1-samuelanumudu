# ------- Vehicle Parking System for Kigali Arena ------- #

# @Authors : Achille Tanwouo and Samuel Anumudu

""" Imported files """

from parking import CarParkingSlot
from parking import MotoParkingSlot
from parking import TruckParkingSlot

from moto_class import Moto
from car_class import Car
from truck_class import Truck

# Vehicles assigned to the parking slot type
car_parking_slot_A = CarParkingSlot('A')
moto_parking_slot_A = MotoParkingSlot('A')
truck_parking_slot_A = TruckParkingSlot('A')

""" The controller class determines the type of vehicle, and sends them to the correct parking lot"""


class Controller:
    def __init__(self):
        pass

    """The static method here runs the method without instantiating it with the controller class"""

    @staticmethod
    # This method controls the vehicle type and the appropriate parking lot for it
    def control_vehicles(vehicle_type):
        if isinstance(vehicle_type, Car):
            print('vehicle is a Car, sending vehicle to car parking lot....')
            car_parking_slot_A.add_vehicle(vehicle_type)
        elif isinstance(vehicle_type, Moto):
            moto_parking_slot_A.add_vehicle(vehicle_type)
        elif isinstance(vehicle_type, Truck):
            truck_parking_slot_A.add_vehicle(vehicle_type)
        else:
            print('you are not allowed to park this kind of vehicle in the building')
