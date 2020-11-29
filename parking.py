# ------- Vehicle Parking System for Kigali Arena ------- #

# @Authors : Achille Tanwouo and Samuel Anumudu

""" The ParkingSlot class to show the individual parking slots"""


class ParkingSlot:
    def __init__(self, name):
        self.name = name
        self.capacity = 10
        self.time = []
        self.lots = []

    """ This method adds vehicles in our parking slots"""
    def add_vehicle(self, vehicle):
        if len(self.lots) < self.capacity:
            self.lots.append(vehicle)
            print(f'You have parked vehicle with license number {vehicle.license_number} in parking lot {self.name}')
            print(f'This vehicle was parked by {vehicle.time}')
        else:
            print('This parking lot is full, try another one')

    """ This method helps us view details for vehicle parked and serves as accountability measure"""
    def view_details(self):
        for vehicle in self.lots:
            print(f'{vehicle.license_number}')

    """ The subclasses inheriting from the Parking Slot"""


class CarParkingSlot(ParkingSlot):
    def __init__(self, name):
        ParkingSlot.__init__(self, name)
        self.capacity = 30


class MotoParkingSlot(ParkingSlot):
    def __init__(self, name):
        ParkingSlot.__init__(self, name)
        self.capacity = 50


class TruckParkingSlot(ParkingSlot):
    def __init__(self, name):
        ParkingSlot.__init__(self, name)
        self.capacity = 20
