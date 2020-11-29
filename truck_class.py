# ------- Vehicle Parking System for Kigali Arena ------- #

# @Authors : Achille Tanwouo and Samuel Anumudu

""" The vehicle class imported here takes a super position to the truck class"""

from vehicle import Vehicle


class Truck(Vehicle):
    """ Truck class representing one of the vehicles we have in our vehicle class """
    def __init__(self):
        Vehicle.__init__(self)
