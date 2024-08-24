# Author: Peyton J. Hall
"""
A main driver module to run the simulation.
This data science project aims to create a three-dimensional 
simulation of gym traffic for LifeTime Fitness in Savage Minnesota.
The simulation will dynamically display gym attendance, showing 
virtual people entering and exiting the gym facilities based on hourly traffic data.
"""

from LifeTimeSavage import lifetime_savage, hide_axes
import matplotlib.pyplot as plt

def Validate_Input(prompt):
	while True:
		user_input = input(prompt)
		if user_input == "":
			return True
		else:
			print("Please press Enter to continue.")

def Main():
	prompt = "Enter the gym.\nPress Enter to select LifeTime Savage: "
	choice = Validate_Input(prompt)
    
	if choice == 1:
		lifetime_savage()

# Call the Main function
if __name__ == "__main__":
	Main()
