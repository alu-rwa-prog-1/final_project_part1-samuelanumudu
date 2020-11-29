
# ------- Vehicle Parking System for Kigali Arena ------- #


# @Authors : Achille Tanwouo and Samuel Anumudu

""" Modules imported to generate random license number and time value"""
import uuid
import time


class Vehicle:
    """ This class holds all our vehicles, checks the time and license number"""
    def __init__(self):
        self.license_number = uuid.uuid1()
        self.time = time.time()
