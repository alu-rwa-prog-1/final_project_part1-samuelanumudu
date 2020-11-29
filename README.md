# final_project_part1_2020

# WHAT WE ARE WORKING 
Our project is about creating an efficient parking system for Kigali Arena during its forthcoming sporting events / carnival in 2021.
We assume this is going to be one of the biggest sporting events in East Africa and expect to have a huge number of attendance.

We have created a VEHICLE CLASS which is the super class in our program that shares its attributes and behavior with other sub classes: 
Car Class, Moto Class, and Truck Class. The sub classes are all inheriting from the VEHICLE super class.
Here we imagine there would be three types of vehicles that are going to be parked in our slots, hence, we have created a designated parking slots for all the threee types of vehicles. 

We also have the CONTROLLER class which serves the 'functionality class' for our vehicle. In real life, there are security personnel who direct vehicles to the right parking slot, registers the time the vehicles come in and go out of the parking slots, and maintains the parking slot. 
Here our CONTROLLER class performs similar function in the program. Basically, the controller controls and moves vehicles to their right parking slots.
There is also a QUEUE created which is a list (or array) to organize cars that are not in the parking slots. The QUEUE program appends vehicles whilst considering the parking slot capacity.

N.B: We have made this project as simple and straightforward as possible. However, it can be further improved and can accept more functionalities and flexibilities for users

# MODULES USED IN THE PROGRAM
1. The UUID generator: This module generates a unique ID for our vehicles representing each vehicles' license number. 
(ref: https://docs.python.org/3/library/uuid.html)

2. The Time Module: The Python time module provides many ways of representing time in code, such as objects, numbers, and strings. It also provides functionality other than representing time, like waiting during code execution and measuring the efficiency of your code.
(ref: https://docs.python.org/3/library/time.html)

3. The Unit Testing Framework: We used the test case to check individual unit of of our program. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.
(ref: https://docs.python.org/3/library/unittest.html)
