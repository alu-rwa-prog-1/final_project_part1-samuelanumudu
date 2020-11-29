# ------- Vehicle Parking System for Kigali Arena ------- #

# @Authors : Achille Tanwouo and Samuel Anumudu

""" The vehicle class imported here takes a super position to the Car class"""

from vehicle import Vehicle


class Car(Vehicle):
    """ Car class representing one of the vehicles we have in our vehicle class """
    def __init__(self):
        Vehicle.__init__(self)
