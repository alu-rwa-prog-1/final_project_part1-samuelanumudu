# ------- Vehicle Parking System for Kigali Arena ------- #

# @Authors : Achille Tanwouo and Samuel Anumudu

""" The vehicle class imported here takes a super position to the Moto class"""

from vehicle import Vehicle


class Moto(Vehicle):
    """ Moto class representing one of the vehicles we have in our vehicle class """
    def __init__(self):
        Vehicle.__init__(self)
