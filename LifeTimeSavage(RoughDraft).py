# Author: Peyton J. Hall
"""
A module to represent the infrastructure of LifeTime in Savage, Minnesota.
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

""" Hides all the axes and labels """
def hide_axes(ax):
    ax.set_axis_off()

"""
LifeTime Savage is 80,000 square feet and rectangular shaped.
That is 7432.2432 square meters. 
It is 100 meters in length x 56.5 meters in width.
Estimate: The gym is an estimated 12 meters tall.
"""
def lifetime_savage():
	fig = plt.figure()
	ax = fig.add_subplot(111, projection = "3d")

	def view():
		# Adjust the camera view
		ax.view_init(elev = 20, azim = 270)
		ax.dist = 8 # Smaller values zoom in; larger values zoom out.
	view()

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
		# Equation 1: y = -8 {-122 <= x <= 57.5}
		def equation_1():
			x1 = np.linspace(-122, 57.5, 400)
			y1 = -8 * np.ones(x1.shape)
			z1 = np.zeros(x1.shape)
			ax.plot(x1, y1, z1, color = "gray")
		equation_1()

		# Equation 2: y = -100 {-23 <= x <= -7}
		def equation_2():
			x2 = np.linspace(-23, -7, 400)
			y2 = -100 * np.ones(x2.shape)
			z2 = np.zeros(x2.shape)
			ax.plot(x2, y2, z2, color = "gray", alpha = 0.5)
		equation_2()

		# Equation 3: x = -7 {-100 <= y <= -86}
		def equation_3():
			y3 = np.linspace(-100, -86, 400)
			x3 = -7 * np.ones(y3.shape)
			z3 = np.zeros(y3.shape)
			ax.plot(x3, y3, z3, color = "gray")
		equation_3()

		# Equation 4: x = -23 {-100 <= y <= -86}
		def equation_4():
			y4 = np.linspace(-100, -86, 400)
			x4 = -23 * np.ones(y4.shape)
			z4 = np.zeros(y4.shape)
			ax.plot(x4, y4, z4, color = "gray")
		equation_4()

		# Equation 5: x = 57.5 {-8 <= y <= 55}
		def equation_5():
			y5 = np.linspace(-8, 55, 400)
			x5 = 57.5 * np.ones(y5.shape)
			z5 = np.zeros(y5.shape)
			ax.plot(x5, y5, z5, color = "gray")
		equation_5()

		# Equation 6: y = 5(x + 120.4) {-50 <= y <= -7.99}
		def equation_6():
			# Solving for x when y = -50 and y = -7.99
			x_start = (-50 - 602) / 5  # This will give the start value for x
			x_end = (-7.99 - 602) / 5  # This will give the end value for x

			# Create a range of x values between x_start and x_end
			x6 = np.linspace(x_start, x_end, 400)
			y6 = 5 * x6 + 602
			z6 = np.zeros(x6.shape)  # z-axis is always 0 as per your setting

			# Plotting the line on the 3D graph
			ax.plot(x6, y6, z6, color = "gray")
		equation_6()

		# Equation 7: y = 0.2[(x + 1.35)^3] - 50 {-6.664 <= x <= 3.964}
		def equation_7():
			x7 = np.linspace(-6.664, 3.964, 400)
			y7 = 0.2 * (x7 + 1.35)**3 - 50
			z7 = np.zeros_like(x7)
			ax.plot(x7, y7, z7, color = "gray")
		equation_7()

		# Equation 8: y = 0.2[(x + 17.35)^3] - 50 {-22.67 <= x <= -12.036}
		def equation_8():
			x8 = np.linspace(-22.67, -12.036, 400)
			y8 = 0.2 * (x8 + 17.35)**3 - 50
			z8 = np.zeros_like(x8)
			ax.plot(x8, y8, z8, color = "gray")
		equation_8()

		# Equation 9: y = 0.2[(x + 6.68)^3] - 50 {-11.994 <= x <= -1.3667}
		def equation_9():
			x9 = np.linspace(-11.994, -1.3667, 400)
			y9 = 0.2 * (x9 + 6.68)**3 - 50
			z9 = np.zeros_like(x9)
			ax.plot(x9, y9, z9, color = "gray")
		equation_9()

		# Equation 10: y = 0.2[(x + 12.01)^3] - 50 {-17.324 <= x <= -6.696}
		def equation_10():
			x10 = np.linspace(-17.324, -6.696, 400)
			y10 = 0.2 * (x10 + 12.01)**3 - 50
			z10 = np.zeros_like(x10)
			ax.plot(x10, y10, z10, color = "gray")
		equation_10()

		# Equation 11: y = -80 {-17.33 <= x <= -11.99}
		def equation_11():
			x11 = np.linspace(-17.33, -11.99, 400)
			y11 = -80 * np.ones(x11.shape)
			z11 = np.zeros(x11.shape)
			ax.plot(x11, y11, z11, color = "gray")
		equation_11()

		# Equation 12: y = -20 {-6.7 <= x <= -1.36}
		def equation_12():
			x12 = np.linspace(-6.7, -1.36, 400)
			y12 = -20 * np.ones(x12.shape)
			z12 = np.zeros(x12.shape)
			ax.plot(x12, y12, z12, color = "gray")
		equation_12()

		# Equation 13: y = -20 {-39 <= x <= -12.02}
		def equation_13():
			x13 = np.linspace(-39, -12.02, 400)
			y13 = -20 * np.ones(x13.shape)
			z13 = np.zeros(x13.shape)
			ax.plot(x13, y13, z13, color = "gray")
		equation_13()

		# Equation 14: y = [-2^(x + 31.9)] - 30 {-38.99267 <= x <= -27.339}
		def equation_14():
			x14 = np.linspace(-38.99267, -27.339, 400)
			y14 = -2 ** (x14 + 31.9) - 30
			z14 = np.zeros_like(x14)
			ax.plot(x14, y14, z14, color = "gray")
		equation_14()

		# Equation 15: x = .1[(y + 25)^2] - 41.5 {-30.01 <= y <= -20}
		def equation_15():
			y15 = np.linspace(-30.01, -20, 400)
			x15 = 0.1 * ((y15 + 25)**2) - 41.5
			z15 = np.zeros(x15.shape)
			ax.plot(x15, y15, z15, color = "gray")
		equation_15()

		# Equation 16: y = 15(x + 27.3) - 53 {-29.1 <= x <= -27.339}
		def equation_16():
			x16 = np.linspace(-29.1, -27.339, 400)
			y16 = 15 * (x16 + 27.3) - 53
			z16 = np.zeros_like(x16)
			ax.plot(x16, y16, z16, color = "gray")
		equation_16()

		# Equation 17: y = -80 {-29.1 <= x <= -22.6}
		def equation_17():
			x17 = np.linspace(-29.1, -22.6, 400)
			y17 = -80 * np.ones(x17.shape)
			z17 = np.zeros(x17.shape)
			ax.plot(x17, y17, z17, color = "gray")
		equation_17()

		# Equation 18: y = -20 {3.96 <= x <= 25}
		def equation_18():
			x18 = np.linspace(3.96, 25, 400)
			y18 = -20 * np.ones(x18.shape)
			z18 = np.zeros(x18.shape)
			ax.plot(x18, y18, z18, color = "gray")
		equation_18()

		# Equation 19: y = -SQRT[7(x + 130.4)] - 70 {x <= -93.8}
		def equation_19():
			x19 = np.linspace(-130.4, -93.82857, 400)
			y19 = -np.sqrt(7 * (x19 + 130.4)) - 70
			z19 = np.zeros(x19.shape)
			ax.plot(x19, y19, z19, color = "gray")
		equation_19()

		# Equation 20: x = -130.4 {-70 <= y <= -50}
		def equation_20():
			y20 = np.linspace(-70, -50, 400)
			x20 = -130.4 * np.ones(y20.shape)
			z20 = np.zeros(y20.shape)
			ax.plot(x20, y20, z20, color = "gray")
		equation_20()

		# Equation 21: y = -86 {-93.83 <= x <= -23}
		def equation_21():
			x21 = np.linspace(-93.83, -23, 400)
			y21 = -86 * np.ones_like(x21)
			z21 = np.zeros_like(x21)
			ax.plot(x21, y21, z21, color = "gray")
		equation_21()

		# Equation 22: y = -86 {-7 <= x <= 57.5}
		def equation_22():
			x22 = np.linspace(-7, 57.5, 400)
			y22 = -86 * np.ones_like(x22)
			z22 = np.zeros_like(x22)
			ax.plot(x22, y22, z22, color = "gray")
		equation_22()

		# Equation 23: y = .2(x - 57.5) - 86 {57.5 <= x <= 111}
		def equation_23():
			x23 = np.linspace(57.5, 111, 400)
			y23 = 0.2 * (x23 - 57.5) - 86
			z23 = np.zeros_like(x23)
			ax.plot(x23, y23, z23, color = "gray")
		equation_23()

		# Equation 24: y = -80 {-6.68 <= x <= 21.32}
		def equation_24():
			x24 = np.linspace(-6.68, 21.32, 400)
			y24 = -80 * np.ones_like(x24)
			z24 = np.zeros_like(x24)
			ax.plot(x24, y24, z24, color = "gray")
		equation_24()

		# Equation 25: y = -5(x - 21.3) - 80 {13.37 <= x <= 21.3}
		def equation_25():
			x25 = np.linspace(13.37, 21.3, 400)
			y25 = -5 * (x25 - 21.3) - 80
			z25 = np.zeros_like(x25)
			ax.plot(x25, y25, z25, color = "gray")
		equation_25()

		# Equation 26: x = -.05(y + 24.5)^2 + 26 {-40.39 <= y <= -20}
		def equation_26():
			y26 = np.linspace(-40.39, -20, 400)
			x26 = -0.05 * (y26 + 24.5)**2 + 26
			z26 = np.zeros_like(y26)
			ax.plot(x26, y26, z26, color = "gray")
		equation_26()

		# Equation 27: y = -6(x-111) - 75.3 {-75.3 <= y <= 25}
		def equation_27():
			y27 = np.linspace(-75.3, 25, 400)
			x27 = 111 - (y27 + 75.3) / 6
			z27 = np.zeros_like(x27)
			ax.plot(x27, y27, z27, color = "gray")
		equation_27()

		# Equation 28: y = .2(x - 94.3) + 24.9 {88 <= x <= 94.3}
		def equation_28():
			x28 = np.linspace(88, 94.3, 400)
			y28 = 0.2 * (x28 - 94.3) + 24.9
			z28 = np.zeros_like(x28)
			ax.plot(x28, y28, z28, color = "gray")
		equation_28()

		# Equation 29: y = -1.5(x - 88) + 23.64 {80 <= x <= 88}
		def equation_29():
			x29 = np.linspace(80, 88, 400)
			y29 = -1.5 * (x29 - 88) + 23.64
			z29 = np.zeros_like(x29)
			ax.plot(x29, y29, z29, color = "gray")
		equation_29()

		# Equation 30: y = -1.5(x - 88) + 23.64 {49.42 <= x <= 75}
		def equation_30():
			x30 = np.linspace(49.42, 75, 400)
			y30 = -1.5 * (x30 - 88) + 23.64
			z30 = np.zeros_like(x30)
			ax.plot(x30, y30, z30, color = "gray")
		equation_30()

		# Equation 31: y = 56.5 {-51 <= x <= -43.5}
		def equation_31():
			x31 = np.linspace(-51, -43.5, 400)
			y31 = 56.5 * np.ones_like(x31)
			z31 = np.zeros_like(x31)
			ax.plot(x31, y31, z31, color = "gray")
		equation_31()

		# Equation 32: y = -1.5(x - 57.5) + 55 {44.83 <= x <= 57.5}
		def equation_32():
			x32 = np.linspace(44.83, 57.5, 400)
			y32 = -1.5 * (x32 - 57.5) + 55
			z32 = np.zeros_like(x32)
			ax.plot(x32, y32, z32, color = "gray")
		equation_32()

		# Equation 33: x = -51 {56.5 <= y <= 74}
		def equation_33():
			y33 = np.linspace(56.5, 74, 400)
			x33 = -51 * np.ones_like(y33)
			z33 = np.zeros_like(y33)
			ax.plot(x33, y33, z33, color = "gray")
		equation_33()

		# Equation 34: x = -43.5 {56.5 <= y <= 68.5}
		def equation_34():
			y34 = np.linspace(56.5, 68.5, 400)
			x34 = -43.5 * np.ones_like(y34)
			z34 = np.zeros_like(y34)
			ax.plot(x34, y34, z34, color = "gray")
		equation_34()

		# Equation 35: y = 74 {-38 <= x <= 44.9}
		def equation_35():
			x35 = np.linspace(-38, 44.9, 400)
			y35 = 74 * np.ones_like(x35)
			z35 = np.zeros_like(x35)
			ax.plot(x35, y35, z35, color = "gray")
		equation_35()

		# Equation 36: y = 81.5 {-43.5 <= x <= 49.42667}
		def equation_36():
			x36 = np.linspace(-43.5, 49.42667, 400)
			y36 = 81.5 * np.ones_like(x36)
			z36 = np.zeros_like(x36)
			ax.plot(x36, y36, z36, color = "gray")
		equation_36()

		# Equation 37: y = 1(x + 40) + 72 {-43.5 <= x <= -38}
		def equation_37():
			x37 = np.linspace(-43.5, -38, 400)
			y37 = 1 * (x37 + 40) + 72
			z37 = np.zeros_like(x37)
			ax.plot(x37, y37, z37, color = "gray")
		equation_37()

		# Equation 38: y = 1(x + 45) + 80 {-51 <= x <= -43.5}
		def equation_38():
			x38 = np.linspace(-51, -43.5, 400)
			y38 = 1 * (x38 + 45) + 80
			z38 = np.zeros_like(x38)
			ax.plot(x38, y38, z38, color = "gray")
		equation_38()

		# Equation 39: y = -1.5(x - 85) + 45 {82.33 <= x <= 87.34}
		def equation_39():
			x39 = np.linspace(82.33, 87.34, 400)
			y39 = -1.5 * (x39 - 85) + 45
			z39 = np.zeros_like(x39)
			ax.plot(x39, y39, z39, color = "gray", alpha = 0.5)
		equation_39()

		# Equation 40: y = .8(x - 75) + 43.14 {75 <= x <= 82.34}
		def equation_40():
			x40 = np.linspace(75, 82.34, 400)
			y40 = 0.8 * (x40 - 75) + 43.14
			z40 = np.zeros_like(x40)
			ax.plot(x40, y40, z40, color = "gray")
		equation_40()

		# Equation 41: y = .8(x - 80) + 35.64 {80 <= x <= 87.34}
		def equation_41():
			x41 = np.linspace(80, 87.34, 400)
			y41 = 0.8 * (x41 - 80) + 35.64
			z41 = np.zeros_like(x41)
			ax.plot(x41, y41, z41, color = "gray")
		equation_41()

		# Equation 42: y = -98 {-17.33 <= x <= -11.99}
		def equation_42():
			x42 = np.linspace(-17.33, -11.99, 400)
			y42 = -98 * np.ones_like(x42)
			z42 = np.zeros_like(x42)
			ax.plot(x42, y42, z42, color = "gray")
		equation_42()

		# Equation 43: y = -86 {-17.33 <= x <= -11.99}
		def equation_43():
			x43 = np.linspace(-17.33, -11.99, 400)
			y43 = -86 * np.ones_like(x43)
			z43 = np.zeros_like(x43)
			ax.plot(x43, y43, z43, color = "gray")
		equation_43()

		# Equation 44: x = -17.33 {-98 <= y <= -86}
		def equation_44():
			y44 = np.linspace(-98, -86, 400)
			x44 = -17.33 * np.ones_like(y44)
			z44 = np.zeros_like(y44)
			ax.plot(x44, y44, z44, color = "gray")
		equation_44()

		# Equation 45: x = -12 {-98 <= y <= -86}
		def equation_45():
			y45 = np.linspace(-98, -86, 400)
			x45 = -12 * np.ones_like(y45)
			z45 = np.zeros_like(y45)
			ax.plot(x45, y45, z45, color = "gray")
		equation_45()

		# Equation 46: y = -1.5(x - 85) + 45 {25 <= x <= 82.22043}
		def equation_46():
			x46 = np.linspace(25, 82.22043, 400)
			y46 = -1.5 * (x46 - 85) + 45
			z46 = np.zeros_like(x46)
			ax.plot(x46, y46, z46, color = "gray")
		equation_46()

		# Equation 47: y = -1.5(x - 97) + 45 {37 <= x <= 90}
		def equation_47():
			x47 = np.linspace(37, 90, 400)
			y47 = -1.5 * (x47 - 97) + 45
			z47 = np.zeros_like(x47)
			ax.plot(x47, y47, z47, color = "gray")
		equation_47()

		# Equation 48: y = .01(x - 134)^2 + 36.15 {89.983866 <= x <= 135}
		def equation_48():
			x48 = np.linspace(89.983866, 135, 400)
			y48 = .01 * (x48 - 134)**2 + 36.15
			z48 = np.zeros_like(x48)
			ax.plot(x48, y48, z48, color = "gray")
		equation_48()

		# Equation 49: y = -1.5(x - 85) + 45 {87.33043 <= x <= 90.00333}
		def equation_49():
			x49 = np.linspace(87.33043, 90.00333, 400)
			y49 = -1.5 * (x49 - 85) + 45
			z49 = np.zeros_like(x49)
			ax.plot(x49, y49, z49, color = "gray")
		equation_49()

		# Equation 50: y = -SQRT[6(x - 87.33)] + 41.5 {90.00332 <= x <= 135}
		def equation_50():
			x50 = np.linspace(90.00332, 135, 400)
			y50 = -np.sqrt(6 * (x50 - 87.33)) + 41.5
			z50 = np.zeros_like(x50)
			ax.plot(x50, y50, z50, color = "gray")
		equation_50()

		# Equation 51: y = -100 {-135 <= x <= -23}
		def equation_51():
			x51 = np.linspace(-135, -23, 400)
			y51 = -100 * np.ones_like(x51)
			z51 = np.zeros_like(x51)
			ax.plot(x51, y51, z51, color = "gray")
		equation_51()

		# Equation 52: y = -100 {-7 <= x <= 135}
		def equation_52():
			x52 = np.linspace(-7, 135, 400)
			y52 = -100 * np.ones_like(x52)
			z52 = np.zeros_like(x52)
			ax.plot(x52, y52, z52, color = "gray")
		equation_52()

		# Equation 53: y = -111 {-135 <= x <= 135}
		def equation_53():
			x53 = np.linspace(-135, 135, 400)
			y53 = -111 * np.ones_like(x53)
			z53 = np.zeros_like(x53)
			ax.plot(x53, y53, z53, color = "gray")
		equation_53()

		def fill_colour():
			# Defining a polygon's verticies
			parking_lot_concrete = np.array([
				[57.5, -8, 0], [57.5, 55, 0], [44.83, 74, 0], 
				[-38, 74, 0], [-43.5, 68.5, 0], [-43.5, 56.5, 0], 
				[-51, 56.5, 0], [-51, 74, 0], [-43.5, 81.5, 0], 
				[49.43, 81.5, 0], [75, 43.14, 0], [82.33, 49.00, 0], 
				[87.33, 41.50, 0], [80, 35.64, 0], [88, 23.64, 0], 
				[94.3, 24.9, 0], [111, -75.3, 0], [57.5, -86, 0],
				[-7, -86, 0], [-7, -100, 0], [-23, -100, 0], [-23, -86, 0],
				[-93.83, -86, 0], [-130.4, -70, 0], [-130.4, -50, 0], [-122, -8, 0]
			])
			# Creating a polygon collection
			parking_lot_concrete = Poly3DCollection([parking_lot_concrete], facecolors = "gray", alpha = 0.5)
			ax.add_collection3d(parking_lot_concrete)

			parking_lot_concrete_part_2 = np.array([
				[-93.82857, -86, 0], [-100, -84.58767, 0], 
				[-104, -83.59412, 0], [-107, -82.79844, 0], [-110, -81.9499, 0],
				[-112, -81.34901, 0], [-114, -80.71448, 0], [-116, -80.03992, 0],
				[-118, -79.31665, 0], [-120, -78.53229, 0], [-122, -77.66812, 0],
				[-124, -76.69328, 0], [-126, -75.54977, 0], [-128, -74.09878, 0],
				[-129, -73.1305, 0], [-130, -71.67332, 0],
				[-130.4, -70, 0]
			])
			parking_lot_concrete_part_2 = Poly3DCollection([parking_lot_concrete_part_2], facecolors = "gray", alpha = 0.5)
			ax.add_collection3d(parking_lot_concrete_part_2)

			landscape_curb_southeast = np.array([
				[-12, -86, .2], [-12,-98, .2],
				[-17.33, -98, .2], [-17.33, -86, .2]
			])
			# Creating another polygon collection
			landscape_curb_southeast = Poly3DCollection([landscape_curb_southeast], facecolors = "green", alpha = 0.5)
			ax.add_collection3d(landscape_curb_southeast)

			landscape_curb_east = np.array([
				[3.96329, -20, .2], [24.9875, -20, .2], [25.3875, -21, .2], 
				[25.6875, -22, .2], [25.8875, -23, .2], [25.9875, -24, .2], 
				[25.9875, -25, .2], [25.8875, -26, .2], [25.8875, -27, .2], 
				[25.3875, -28, .2], [24.9875, -29, .2], [24.4875, -30, .2], 
				[23.8875, -31, .2], [23.1875, -32, .2], [22.3875, -33, .2], 
				[21.4875, -34, .2], [20.4875, -35, .2], [19.3875, -36, .2], 
				[18.1875, -37, .2], [16.8875, -38, .2], [15.4875, -39, .2], 
				[13.9875, -40, .2], [13.37771, -40.38854, .2], [21.3, -80, .2], 
				[-6.66329, -80, .2], [-6.60359, -79, .2], [-6.54249, -78, .2], 
				[-6.47993, -77, .2], [-6.4158, -76, .2], [-6.35, -75, .2], 
				[-6.28242, -74, .2], [-6.21294, -73, .2], [-6.14142, -72, .2], 
				[-6.06769, -71, .2], [-5.99159, -70, .2], [-5.9129, -69, .2], 
				[-5.8314, -68, .2], [-5.74683, -67, .2], [-5.65887, -66, .2], 
				[-5.56716, -65, .2], [-5.47129, -64, .2], [-5.37073, -63, .2], 
				[-5.26487, -62, .2], [-5.15295, -61, .2], [-5.03403, -60, .2], 
				[-4.90689, -59, .2], [-4.76995, -58, .2], [-4.62107, -57, .2], 
				[-4.45723, -56, .2], [-4.27402, -55, .2], [-4.06442, -54, .2], 
				[-3.81621, -53, .2], [-3.50443, -52, .2], [-3.30743, -51.5, .2], 
				[-3.05998, -51, .2], [-2.70721, -50.5, .2], [-2.42722, -50.25, .2], 
				[-2.20499, -50.125, .2], [-1.35, -50, .2], [-0.49501, -49.875, .2], 
				[-0.27278, -49.75, .2], [0, -49.5, .2], [0.35998, -49, .2], 
				[0.60743, -48.5, .2], [0.80443, -48, .2], [1.11621, -47, .2], 
				[1.36442, -46, .2], [1.57402, -45, .2], [1.75723, -44, .2], 
				[1.92107, -43, .2], [2.06995, -42, .2], [2.20689, -41, .2], 
				[2.33403, -40, .2], [2.45295, -39, .2], [2.56487, -38, .2], 
				[2.67073, -37, .2], [2.77129, -36, .2], [2.86716, -35, .2], 
				[2.95887, -34, .2], [3.04683, -33, .2], [3.1314, -32, .2], 
				[3.2129, -31, .2], [3.29159, -30, .2], [3.36769, -29, .2], 
				[3.44142, -28, .2], [3.51294, -27, .2], [3.58242, -26, .2], 
				[3.65, -25, .2], [3.7158, -24, .2], [3.77993, -23, .2], 
				[3.84249, -22, .2], [3.90359, -21, .2] 
			])
			landscape_curb_east = Poly3DCollection([landscape_curb_east], facecolors = "green", alpha = 0.5)
			ax.add_collection3d(landscape_curb_east)

			landscape_curb_center = np.array([
				[-6.69671, -20, .2], [-1.36671, -20, .2], [-1.42641, -21, .2], 
				[-1.48751, -22, .2], [-1.55007, -23, .2], [-1.6142, -24, .2],
				[-1.68, -25, .2], [-1.74758, -26, .2], [-1.81706, -27, .2], 
				[-1.88858, -28, .2], [-1.96231, -29, .2], [-2.03841, -30, .2], 
				[-2.1171, -31, .2], [-2.1986, -32, .2], [-2.28317, -33, .2], 
				[-2.37113, -34, .2], [-2.46284, -35, .2], [-2.55871, -36, .2], 
				[-2.65927, -37, .2], [-2.76513, -38, .2], [-2.87705, -39, .2], 
				[-2.99597, -40, .2], [-3.12311, -41, .2], [-3.26005, -42, .2], 
				[-3.40893, -43, .2], [-3.57277, -44, .2], [-3.75598, -45, .2], 
				[-3.96558, -46, .2], [-4.21379, -47, .2], [-4.52557, -48, .2], 
				[-4.72257, -48.5, .2], [-4.97002, -49, .2], [-5.33, -49.5, .2], 
				[-5.60278, -49.75, .2], [-5.82501, -49.875, .2], [-6.68, -50, .2], 
				[-7.53499, -50.125, .2], [-7.75722, -50.25, .2], [-8.03721, -50.5, .2], 
				[-8.38998, -51, .2], [-8.63743, -51.5, .2], [-8.83443, -52, .2], 
				[-9.14621, -53, .2], [-9.39442, -54, .2], [-9.60402, -55, .2], 
				[-9.78723, -56, .2], [-9.95107, -57, .2], [-10.09995, -58, .2],
				[-10.23689, -59, .2], [-10.36403, -60, .2], [-10.48295, -61, .2],
				[-10.59487, -62, .2], [-10.70073, -63, .2], [-10.80129, -64, .2],
				[-10.89716, -65, .2], [-10.98887, -66, .2], [-11.07683, -67, .2],
				[-11.1614, -68, .2], [-11.2429, -69, .2], [-11.32159, -70, .2],
				[-11.39769, -71, .2], [-11.47142, -72, .2], [-11.54294, -73, .2],
				[-11.61242, -74, .2], [-11.68, -75, .2], [-11.7458, -76, .2],
				[-11.80993, -77, .2], [-11.87249, -78, .2], [-11.93359, -79, .2],
				[-11.99329, -80, .2], [-11.99329, -80, .2], [-17.26359, -79, .2],
				[-17.20249, -78, .2], [-17.13993, -77, .2], [-17.0758, -76, .2],
				[-17.01, -75, .2], [-16.94242, -74, .2], [-16.87294, -73, .2],
				[-16.80142, -72, .2], [-16.72769, -71, .2], [-16.65159, -70, .2],
				[-16.5729, -69, .2], [-16.4914, -68, .2], [-16.40683, -67, .2],
				[-16.31887, -66, .2], [-16.22716, -65, .2], [-16.13129, -64, .2],
				[-16.03073, -63, .2], [-15.92487, -62, .2], [-15.81295, -61, .2],
				[-15.69403, -60, .2], [-15.56689, -59, .2], [-15.42995, -58, .2],
				[-15.28107, -57, .2], [-15.11723, -56, .2], [-14.93402, -55, .2],
				[-14.72442, -54, .2], [-14.47621, -53, .2], [-14.16443, -52, .2],
				[-13.96743, -51.5, .2], [-13.71998, -51, .2], [-13.36721, -50.5, .2],
				[-13.08722, -50.25, .2], [-12.86499, -50.125, .2], [-12.01, -50, .2],
				[-11.15501, -49.875, .2], [-10.93278, -49.75, .2], [-10.66, -49.5, .2],
				[-10.30002, -49, .2], [-10.05257, -48.5, .2], [-9.85557, -48, .2],
				[-9.54379, -47, .2], [-9.29558, -46, .2], [-9.08598, -45, .2],
				[-8.90277, -44, .2], [-8.73893, -43, .2], [-8.59005, -42, .2],
				[-8.45311, -41, .2], [-8.32597, -40, .2], [-8.20705, -39, .2],
				[-8.09513, -38, .2], [-7.98927, -37, .2], [-7.88871, -36, .2],
				[-7.79284, -35, .2], [-7.70113, -34, .2], [-7.61317, -33, .2],
				[-7.5286, -32, .2], [-7.4471, -31, .2], [-7.36841, -30, .2],
				[-7.29231, -29, .2], [-7.21858, -28, .2], [-7.14706, -27, .2],
				[-7.07758, -26, .2], [-7.01, -25, .2], [-6.9442, -24, .2], 
				[-6.88007, -23, .2], [-6.81751, -22, .2], [-6.75641, -21, .2]
			])
			landscape_curb_center = Poly3DCollection([landscape_curb_center], facecolors = "green", alpha = 0.5)
			ax.add_collection3d(landscape_curb_center)

			landscape_curb_west = np.array([
				[-39, -20, .2], [-12.03671, -20, .2], [-12.09641, -21, .2], 
				[-12.15751, -22, .2], [-12.22007, -23, .2], [-12.2842, -24, .2], 
				[-12.35, -25, .2], [-12.41758, -26, .2], [-12.48706, -27, .2], 
				[-12.55858, -28, .2], [-12.63231, -29, .2], [-12.70841, -30, .2], 
				[-12.7871, -31, .2], [-12.8686, -32, .2], [-12.95317, -33, .2], 
				[-13.04113, -34, .2], [-13.13284, -35, .2], [-13.22871, -36, .2], 
				[-13.32927, -37, .2], [-13.43513, -38, .2], [-13.54705, -39, .2], 
				[-13.66597, -40, .2], [-13.79311, -41, .2], [-13.93005, -42, .2], 
				[-14.07893, -43, .2], [-14.24277, -44, .2], [-14.42598, -45, .2], 
				[-14.63558, -46, .2], [-14.88379, -47, .2], [-15.19557, -48, .2], 
				[-15.39257, -48.5, .2], [-15.64002, -49, .2], [-15.99279, -49.5, .2], 
				[-16.27278, -49.75, .2], [-16.49501, -49.875, .2], [-17.35, -50, .2], 
				[-18.20499, -50.125, .2], [-18.42722, -50.25, .2], [-18.70721, -50.5, .2], 
				[-19.05998, -51, .2], [-19.30743, -51.5, .2], [-19.50443, -52, .2], 
				[-19.81621, -53, .2], [-20.06442, -54, .2], [-20.27402, -55, .2], 
				[-20.45723, -56, .2], [-20.62107, -57, .2], [-20.76995, -58, .2],
				[-20.90689, -59, .2], [-21.03403, -60, .2], [-21.15295, -61, .2],
				[-21.26487, -62, .2], [-21.37073, -63, .2], [-21.47129, -64, .2],
				[-21.56716, -65, .2], [-21.65887, -66, .2], [-21.74683, -67, .2],
				[-21.8314, -68, .2], [-21.9129, -69, .2], [-21.99159, -70, .2],
				[-22.06769, -71, .2], [-22.14142, -72, .2], [-22.21294, -73, .2],
				[-22.28242, -74, .2], [-22.35, -75, .2], [-22.4158, -76, .2],
				[-22.47993, -77, .2], [-22.54249, -78, .2], [-22.60359, -79, .2],
				[-22.66329, -80, .2], [-29.1, -80, .2], [-27.33963, -53.59441, .2],
				[-27.44057, -52, .2], [-27.50768, -51, .2], [-27.57807, -50, .2],
				[-27.65207, -49, .2], [-27.73007, -48, .2], [-27.81254, -47, .2],
				[-27.9, -46, .2], [-27.99311, -45, .2], [-28.09265, -44, .2],
				[-28.19956, -43, .2], [-28.31504, -42, .2], [-28.44057, -41, .2],
				[-28.57807, -40, .2], [-28.73007, -39, .2], [-28.9, -38, .2],
				[-29.09265, -37, .2], [-29.31504, -36, .2], [-29.57807, -35, .2],
				[-29.73007, -34.5, .2], [-29.9, -34, .2], [-30.09265, -33.5, .2],
				[-30.31504, -33, .2], [-30.57807, -32.5, .2], [-30.9, -32, .2],
				[-31.31504, -31.5, .2], [-31.57807, -31.25, .2], [-31.9, -31, .2],
				[-32.31504, -30.75, .2], [-32.9, -30.5, .2], [-33.9, -30.25, .2],
				[-38.99267, -30.00733, .2], [-39, -30, .2], [-39.9, -29, .2],
				[-40.6, -28, .2], [-41.1, -27, .2], [-41.4, -26, .2], 
				[-41.5, -25, .2], [-41.4, -24, .2], [-41.1, -23, .2],
				[-40.6, -22, .2], [-39.9, -21, .2]
			])
			landscape_curb_west = Poly3DCollection([landscape_curb_west], facecolors = "green", alpha = 0.5)
			ax.add_collection3d(landscape_curb_west)

			Loftus_Ln_Savage = np.array([
				[-135, -100, 0], [135, -100, 0],
				[135, -111, 0], [-135, -111, 0]
			])
			Loftus_Ln_Savage = Poly3DCollection([Loftus_Ln_Savage], facecolors = "gray", alpha = 0.5)
			ax.add_collection3d(Loftus_Ln_Savage)

			street_2113_W_140th_St = np.array([
				[25, 135, 0], [37, 135, 0],
				[89.98387, 55.5242, 0], [82.33043, 49.00435, 0]
			])
			street_2113_W_140th_St = Poly3DCollection([street_2113_W_140th_St], facecolors = "gray", alpha = 0.5)
			ax.add_collection3d(street_2113_W_140th_St)

			part_2_street_2113_W_140th_St = np.array([
				[89.98387, 55.5242, 0], [91, 54.64, 0], [92, 53.79, 0],
				[95, 51.36, 0], [100, 47.71, 0], [105, 44.56, 0],
				[110, 41.91, 0], [115, 39.76, 0], [120, 38.11, 0],
				[125, 36.96, 0], [130, 36.31, 0], [135, 36.16, 0],
				[135, 24.58787, 0], [130, 24.58787, 0], [125, 26.46604, 0],
				[120, 27.49929, 0], [115, 28.61513, 0], [110, 29.83724, 0],
				[105, 31.2034, 0], [100, 32.78106, 0], [95, 34.7162, 0],
				[92, 36.20661, 0], [91, 36.80745, 0], [90.00333, 37.495, 0],
				[82.33043, 49.00435, 0]
			])
			part_2_street_2113_W_140th_St = Poly3DCollection([part_2_street_2113_W_140th_St], facecolors = "gray", alpha = 0.5)
			ax.add_collection3d(part_2_street_2113_W_140th_St)

		fill_colour()

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
				tetra_poly = Poly3DCollection([tetra_vertices[face] for face in tetra_faces], alpha = 1, linewidths = 1, edgecolors = "black")
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

	def simulate_gym_traffic():
		prisms = []  # Initialize an empty list to store each person represented as a prism
		person_counter = 0  # Counter to keep track of the number of people added
		frame_interval = 50  # Number of frames to wait before adding a new person

		def create_prism(position, height = 1.82, width = 0.5, depth = 0.3):
			x, y, z = position  # Unpack the position tuple into x, y, z coordinates
			vertices = np.array([
				[x, y, z], [x + width, y, z], [x + width, y + depth, z], [x, y + depth, z],
				[x, y, z + height], [x + width, y, z + height], [x + width, y + depth, z + height], [x, y + depth, z + height]
			])
			# Define faces of the prism using vertices
			faces = [
				[vertices[j] for j in [0, 1, 5, 4]], [vertices[j] for j in [7, 6, 2, 3]],
				[vertices[j] for j in [0, 1, 2, 3]], [vertices[j] for j in [4, 5, 6, 7]],
				[vertices[j] for j in [0, 3, 7, 4]], [vertices[j] for j in [1, 2, 6, 5]]
			]
			return faces

		""" Position 1, where people spawn, is in the parking lot. """
		def position1():
			quadrant_choice = random.choice(["QIV", "QIII"])
			if quadrant_choice == "QIV":
				# Define the range for x and y coordinates within the defined area for QIV
				x_min, x_max = 5, 106
				y_min, y_max = -100, -14
			else:
				# Define the range for x and y coordinates within the defined area for QIII
				x_min, x_max = -115, -28
				y_min, y_max = -103, -15
			# Generate random x and y coordinates within the defined range
			x = random.uniform(x_min, x_max)
			y = random.uniform(y_min, y_max)
			return np.array([x, y, 0]) # Return the position with z-coordinate set to 0

		""" Position 2 is at the outside doors of the atrium. """
		def position2(start_pos):
			return np.array([7/2, -4, 0] if start_pos[0] > 0 else [-7/2, -4, 0])

		""" Position 3 is at the front checkin desk. """
		def position3():
			return np.array([0, 0, 0])

		""" Position 4 is inside the gym. """
		def position4():
			x = random.uniform(-64, 36) # Random x within range
			y = random.uniform(0, 56.5) # Random y within range
			return np.array([x, y, 0]) # Return the position

		""" Position 5, where people start to leave the gym. """
		def position5():
			return np.array([0, 0, 0])

		""" Position 6, where people move towards the exit similar to position 2. """
		def position6(start_pos):
			return position2(start_pos)

		""" Position 7, where people return to their spawn point and disappear. """
		def position7(start_pos):
			return start_pos

		""" Function to generate a random color for each new person """
		def random_color():
			return (random.random(), random.random(), random.random()) # Return a tuple of RGB values

		""" Legend function to display person count """
		def legend():
			return f"Person count: {len(prisms)}" # Return a string with the current person count

		# Display person count on the graph
		text_handle = ax.text2D(0.05, 0.95, legend(), transform = ax.transAxes, fontsize = 12)

		""" Function to interpolate positions for smoother transitions between key points """
		def interpolate_positions(pos1, pos2, steps):
			return [pos1 + (pos2 - pos1) * i / steps for i in range(steps)] # Linear interpolation

		""" Function to add a new person at position 1 and manage their movement through positions """
		def add_person():
			nonlocal person_counter # Refer to the outer scope variable
			start_pos = position1() # Get the start position
			positions = [start_pos, position2(start_pos), position3(), position4()] # List of positions to traverse
			positions.extend(position4() for _ in range(10)) # Add 10 random movements within gym
			positions.append(position5())
			positions.append(position6(start_pos))
			positions.append(position7(start_pos))
			smooth_positions = [] # List for interpolated positions
			for i in range(len(positions) - 1):
				# Interpolate between positions
				smooth_positions.extend(interpolate_positions(positions[i], positions[i + 1], frame_interval))
			color = random_color()
			# Create a 3D polygon collection
			prism = Poly3DCollection(create_prism(start_pos), color = color, alpha = 0.7)
			ax.add_collection3d(prism) # Add the prism to the axes
			prisms.append({
				"prism": prism,
				"positions": smooth_positions,
				"current_frame": 0
			})
			person_counter += 1 # Increment the person counter
			text_handle.set_text(legend()) # Update the legend text

		""" Update function for the animation, managing the position of each person frame by frame """
		def update(frame):
			nonlocal prisms # Refer to the outer scope variable
			if frame % frame_interval == 0 and person_counter < 50: # Check if it's time to add a new person
				add_person()
			for person in list(prisms): # Iterate through each person in the prisms list
				if person["current_frame"] < len(person["positions"]): # Check if there are more positions to move to
					position = person["positions"][person["current_frame"]] # Get the next position
					person["prism"].set_verts(create_prism(position)) # Update the prism's vertices to the new position
					person["current_frame"] += 1 # Increment the current frame index
				if person["current_frame"] >= len(person["positions"]): # Check if person has completed their path
					ax.collections.remove(person["prism"]) # Remove the person from the plot
					prisms.remove(person) # Remove from tracking list

		# Create an animation
		ani = FuncAnimation(fig, update, frames = 1000, interval = 100, blit = False)
		ax.set_xlim([-135, 135])
		ax.set_ylim([-135, 135])
		ax.set_zlim([0, 135])
		ax.set_box_aspect([1, 1, 1])
		hide_axes(ax)
		view()
		plt.show()

	simulate_gym_traffic()

	# Setting the aspect of the plot to be equal, to maintain scaling on all axes
	ax.set_box_aspect([1, 1, 1])  # Ratios between width, length, and height

	# Set plot limits, labels, and title
	ax.set_xlim([-135, 135])
	ax.set_ylim([-135, 135])
	ax.set_zlim([0, 135])
	ax.set_xlabel("Length (meters)")
	ax.set_ylabel("Width (meters)")
	ax.set_zlabel("Height (meters)")
	ax.set_title("")

	hide_axes(ax) # call the hide_axes function.

	# Show the plot
	plt.show()
