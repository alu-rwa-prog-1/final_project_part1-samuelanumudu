# ------- Vehicle Parking System for Kigali Arena ------- #

# @Authors : Achille Tanwouo and Samuel Anumudu

# Import modules / files
import time
from moto_class import Moto
from car_class import Car
from truck_class import Truck
from controller import Controller

queue = []  # Here we wish to create an empty array for queuing vehicles for organizational purposes

for i in range(30):
    if i < 10:
        queue.append(Moto())
        time.sleep(0.05)
    elif 10 < i < 20:
        queue.append(Car())
        time.sleep(0.05)
    else:
        queue.append(Truck())
        time.sleep(0.05)

        # Checking for cars in the queue
for vehicle in queue:
    Controller.control_vehicles(vehicle)

print(queue)
