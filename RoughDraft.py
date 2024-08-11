# Author: Peyton J. Hall
"""
This data science project aims to create a three-dimensional 
simulation of gym traffic for LifeTime Fitness in Savage Minnesota.
The simulation will dynamically display gym attendance, showing 
virtual people entering and exiting the gym facilities based on hourly traffic data.
"""

# import numpy as np                  # For numerical operations
# import pandas as pd                 # For data manipulation
# import matplotlib.pyplot as plt     # For basic plotting
# from mpl_toolkits.mplot3d import Axes3D  # For 3D plotting in matplotlib
# import plotly.express as px         # For interactive 3D visualizations
# import plotly.graph_objects as go   # For detailed control over Plotly plots
# import datetime                     # For handling date and time data
# import random                       # For generating random entries/exits
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # Ensure this line is included

def Validate_Input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) == 1:
            return int(user_input)
        else:
            print("Invalid input. Please enter 1 to select LifeTime Savage.")

"""
LifeTime Savage is 80,000 square feet and rectangular shaped.
That is 7432.2432 square meters. 
It is 100 meters in length x 56.5 meters in width.
Estimate: The gym is an estimated 12 meters tall.
"""
def lifetime_savage():
	fig = plt.figure()
	ax = fig.add_subplot(111, projection="3d")

	# Building dimensions
	length = 100  # length of the building (x-axis)
	width = 56.5  # width of the building (y-axis)
	height = 12   # estimated height of the building (z-axis)

	# Shift value along the axes to put the entrance at (0,0,0)
	x_shift = -14
	y_shift = 28.25

	# Centering the rectangular prism at (0,0)
	x_offset = length / 2
	y_offset = width / 2

	# Coordinates for the vertices of the rectangular prism, centered at (0,0) and shifted by y_shift
	vertices = [
		[-x_offset + x_shift, -y_offset + y_shift, 0], 
		[x_offset + x_shift, -y_offset + y_shift, 0], 
		[x_offset + x_shift, y_offset + y_shift, 0], 
		[-x_offset + x_shift, y_offset + y_shift, 0],  # bottom vertices
		[-x_offset + x_shift, -y_offset + y_shift, height], 
		[x_offset + x_shift, -y_offset + y_shift, height], 
		[x_offset + x_shift, y_offset + y_shift, height], 
		[-x_offset + x_shift, y_offset + y_shift, height]  # top vertices
	]

    # Faces of the rectangular prism, each face is a list of indices into the vertices list
	faces = [
		[0, 1, 2, 3],  # bottom face
		[4, 5, 6, 7],  # top face
		[0, 1, 5, 4],  # side face
		[2, 3, 7, 6],  # opposite side face
		[1, 2, 6, 5],  # width face
		[3, 0, 4, 7]   # length face
	]

	# Create a 3D polygon collection
	poly3d = [[vertices[vertex] for vertex in face] for face in faces]
	ax.add_collection3d(Poly3DCollection(poly3d, facecolors = "tan", linewidths = 1, edgecolors = "black", alpha = .50))

	def savage_parking_lot():
		# Define the x and y coordinates along with conditions for each piecewise section of the parking lot
		equations = [
			(-122, 57.5, None, None, lambda x: -8 * np.ones_like(x)), # Equation 1: y = -8 {-122 <= x <= 57.5}
			(-23, -7, None, None, lambda x: -100 * np.ones_like(x)), # Equation 2: y = -100 {-23 <= x <= -7}
			# Equation 3: x = -7 {-100 <= y <= -86}
			# Equation 4: x = -23 {-100 <= y <= -86}
			# Equation 5: x = 57.5 {-8 <= y <= 55}
			# Equation 6: y = 5(x + 120.4) {-50 <= y <= -7.99}
			# Equation 7: y = 0.2[(x + 1.35)^3] - 50 {-80 <= y <= -20}
			# Equation 8: y = 0.2[(x + 17.35)^3] - 50 {-80 <= y <= -20}
			# Equation 9: y = 0.2[(x + 6.68)^3] - 50 {-80 <= y <= -20}
			# Equation 10: y = 0.2[(x + 12.01)^3] - 50 {-80 <= y <= -20}
			(-17.33, -11.99, None, None, lambda x: -80 * np.ones_like(x)), # Equation 11: y = -80 {-17.33 <= x <= -11.99}
			(-6.7, -1.36, None, None, lambda x: -20 * np.ones_like(x)), # Equation 12: y = -20 {-6.7 <= x <= -1.36}
			# Equation 13: y = -20 {-39 <= x <= -12.02}
			# Equation 14: y = [-2^(x+31.9)] - 30 {-53.6 <= y <= -30.00732}
			# Equation 15: x = .1[(y + 25)^2] - 41.5 {-30.01 <= y <= -20}
			# Equation 16: y = 15(x + 27.3) - 53 {-80 <= y <= -53.35}
			# Equation 17: y = -80 {-29.1 <= x <= -22.6}
			# Equation 18: y = -20 {3.96 <= x <= 25}
			# Equation 19: y = -SQRT[7(x + 130.4)] - 70 {x <= -93.8}
			# Equation 20: x = -130.4 {-70 <= y <= -50}
			# Equation 21: y = -86 {-93.83 <= x <= -23}
			# Equation 22: y = -86 {-7 <= x <= 57.5}
			# Equation 23: y = .2(x - 57.5) - 86 {57.5 <= x <= 111}
			# Equation 24: y = -80 {-6.68 <= x <= 21.32}
			# Equation 25: y = -5(x - 21.3) - 80 {13.37 <= x <= 21.3}
			# Equation 26: x = -.05(y + 24.5)^2 + 26 {-40.39 <= y <= -20}
			# Equation 27: y = -6(x-111) - 75.3 {-75.3 <= y <= 25}
			# Equation 28: y = .2(x - 94.3) + 24.9 {88 <= x <= 94.3}
			# Equation 29: y = -1.5(x - 88) + 23.64 {80 <= x <= 88}
			# Equation 30: y = -1.5(x - 88) + 23.64 {49.42 <= x <= 75}
			# Equation 31: y = 56.5 {-51 <= x <= -43.5}
			# Equation 32: y = -1.5(x - 57.5) + 55 {44.83 <= x <= 57.5}
			# Equation 33: x = -51 {56.5 <= y <= 74}
			# Equation 34: x = -43.5 {56.5 <= y <= 68.5}
			# Equation 35: y = 74 {-38 <= x <= 44.9}
			# Equation 36: y = 81.5 {-43.5 <= x <= 49.42667}
			# Equation 37: y = 1(x + 40) + 72 {-43.5 <= x <= -38}
			# Equation 38: y = 1(x + 45) + 80 {-51 <= x <= -43.5}
			# Equation 39: y = -1.5(x - 85) + 45 {82.33 <= x <= 87.34}
			# Equation 40: y = .8(x - 75) + 43.14 {75 <= x <= 82.34}
			# Equation 41: y = .8(x - 80) + 35.64 {80 <= x <= 87.34}
			# Equation 42: y = -98 {-17.33 <= x <= -11.99}
			# Equation 43: y = -86 {-17.33 <= x <= -11.99}
			# Equation 44: x = -17.33 {-98 <= y <= -86}
			# Equation 45: x = -12 {-98 <= y <= -86}
		]

		for (x_start, x_end, y_start, y_end, func) in equations:
			x_vals = np.linspace(x_start, x_end, 400) if x_start is not None else np.linspace(-100, 100, 400)
			if func.__name__ == "<lambda>":
				y_vals = func(x_vals)
				ax.plot(x_vals, y_vals, zs = 0, zdir = "z", label = "Parking lot", color = "gray")  # Plotting on the ground (z=0)
			else:
				y_vals = np.linspace(y_start, y_end, 400)
				x_vals = func(y_vals)
				ax.plot(x_vals, y_vals, zs = 0, zdir = "z", label = "Parking lot", color = "gray")  # Adjust accordingly for vertical lines

	savage_parking_lot()

	"""
		On the main plot, the (x,y,z) or (length, width, height) coordinates of
		the points on the triangular prism are as follows:
		Base (Ground Level): (-7,0,0), (7,0,0), (0,-8,0).
		Top (Roof Level): (-7,0,12), (7,0,12), (0,-8,12).
	"""
	def savage_atrium():
		def triangular_prism():
			# Define vertices of the triangular prism
			prism_vertices = np.array([
				[-7, 0, 0], [7, 0, 0], [0, -8, 0], [-7, 0, 13], [7, 0, 13], [0, -8, 13]
			])

			# Define faces using indices into the prism_vertices array
			prism_faces = [
				[0, 1, 2], [3, 4, 5], [0, 3, 5, 2], [0, 1, 4, 3], [1, 2, 5, 4]
			]

			# Add the prism to the plot
			poly = Poly3DCollection([prism_vertices[face] for face in prism_faces], alpha = 1, linewidths = 1, edgecolors = "black")
			poly.set_facecolor("skyblue")
			ax.add_collection3d(poly)

		def atrium_roof_base():
			def roof_rectangular_prism():
				# Define vertices of the rectangular prism
				rect_vertices = np.array([
					[-7, 0, 12], [7, 0, 12], [-7, 8, 12], [7, 8, 12],
					[-7, 0, 13], [7, 0, 13], [-7, 8, 13], [7, 8, 13]
				])

				# Define faces using indices into the rect_vertices array
				rect_faces = [
					[0, 1, 3, 2],  # Bottom face
					[4, 5, 7, 6],  # Top face
					[0, 1, 5, 4],  # Front face
					[2, 3, 7, 6],  # Back face
					[1, 3, 7, 5],  # Right face
					[0, 2, 6, 4]   # Left face
				]

				# Add the rectangular prism to the plot
				rect_poly = Poly3DCollection([rect_vertices[face] for face in rect_faces], alpha = 1, linewidths = 1, edgecolors = "black")
				rect_poly.set_facecolor("skyblue")
				ax.add_collection3d(rect_poly)

			def roof_triangular_prism_rear():
				# Define vertices of the triangular prism
				tri_vertices = np.array([
					[-7, 8, 12], [7, 8, 12], [0, 16, 12],
					[-7, 8, 13], [7, 8, 13], [0, 16, 13]
				])

				# Define faces using indices into the tri_vertices array
				tri_faces = [
					[0, 1, 2],  # Bottom face
					[3, 4, 5],  # Top face
					[0, 1, 4, 3],  # Front face
					[1, 2, 5, 4],  # Right face
					[2, 0, 3, 5]   # Left face
				]

				# Add the triangular prism to the plot
				tri_poly = Poly3DCollection([tri_vertices[face] for face in tri_faces], alpha = 1, linewidths = 1, edgecolors = "black")
				tri_poly.set_facecolor("skyblue")
				ax.add_collection3d(tri_poly)

			# Call the functions to add the prisms
			roof_rectangular_prism()
			roof_triangular_prism_rear()

		def atrium_tip():
			def middle_triangular_prism():
				# Define vertices of the middle triangular prism
				tri_vertices = np.array([
					[-7, 0, 13], [7, 0, 13], [0, 0, 16],
					[-7, 8, 13], [7, 8, 13], [0, 8, 16]
				])

				# Define faces using indices into the tri_vertices array
				tri_faces = [
					[0, 1, 2],  # Front triangular face
					[3, 4, 5],  # Back triangular face
					[0, 1, 4, 3],  # Bottom rectangular face
					[0, 2, 5, 3],  # Left trapezoidal face
					[1, 2, 5, 4]   # Right trapezoidal face
				]

				# Add the triangular prism to the plot
				tri_poly = Poly3DCollection([tri_vertices[face] for face in tri_faces], alpha = 1, linewidths = 1, edgecolors = "black")
				tri_poly.set_facecolor("skyblue")
				ax.add_collection3d(tri_poly)

			# def front_tetrahedron():
				# vetrices:
				# (-7,0,13), (7,0,13), (0,0,16), (0,-8,13)

			# def rear_tetrahedron():
				# (-7,8,12), (7,8,12), (0,8,16), (0,16,13)
			def front_tetrahedron():
				# Define vertices of the front tetrahedron
				tetra_vertices = np.array([
					[-7, 0, 13], [7, 0, 13], [0, 0, 16], [0, -8, 13]
				])

				# Define faces using indices into the tetra_vertices array
				tetra_faces = [
					[0, 1, 2],  # Base triangular face
					[0, 1, 3],  # Bottom triangular face
					[0, 2, 3],  # Left triangular face
					[1, 2, 3]   # Right triangular face
				]

				# Add the front tetrahedron to the plot
				tetra_poly = Poly3DCollection([tetra_vertices[face] for face in tetra_faces], alpha = 1, linewidths = 1, edgecolors = "black")
				tetra_poly.set_facecolor("skyblue")
				ax.add_collection3d(tetra_poly)

			def rear_tetrahedron():
				# Define vertices of the rear tetrahedron
				tetra_vertices = np.array([
					[-7, 8, 13], [7, 8, 13], [0, 8, 16], [0, 16, 13]
				])

				# Define faces using indices into the tetra_vertices array
				tetra_faces = [
					[0, 1, 2],  # Base triangular face
					[0, 1, 3],  # Bottom triangular face
					[0, 2, 3],  # Left triangular face
					[1, 2, 3]   # Right triangular face
				]

				# Add the rear tetrahedron to the plot
				tetra_poly = Poly3DCollection([tetra_vertices[face] for face in tetra_faces], alpha=1, linewidths=1, edgecolors="black")
				tetra_poly.set_facecolor("skyblue")
				ax.add_collection3d(tetra_poly)

			middle_triangular_prism()
			front_tetrahedron()
			rear_tetrahedron()

		triangular_prism()
		atrium_roof_base()
		atrium_tip()

	# Call the atrium function within the main building plot
	savage_atrium()


	# Setting the aspect of the plot to be equal, to maintain scaling on all axes
	ax.set_box_aspect([1, 1, 1])  # Ratios between width, length, and height

	# Set plot limits, labels, and title
	ax.set_xlim([-135, 135])
	ax.set_ylim([-135, 135])
	ax.set_zlim([0, 135])
	ax.set_xlabel("Length (meters)")
	ax.set_ylabel("Width (meters)")
	ax.set_zlabel("Height (meters)")
	ax.set_title("LifeTime Savage")

	# Show the plot
	plt.show()

def Main():
	prompt = "Which Gym would you like to see?\n1. LifeTime Savage\nEnter your choice: "
	choice = Validate_Input(prompt)
    
	if choice == 1:
		lifetime_savage()

# Call the Main function
if __name__ == "__main__":
	Main()

    

"""
The x, y, z Coordinate System:
Based on the Cartesian Coordinate System.
x and y: represent horizontal axes.
z: represents the vertical axis.
"""
