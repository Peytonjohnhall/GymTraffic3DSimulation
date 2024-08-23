import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from matplotlib.animation import FuncAnimation
import random

# Function to create a rectangular prism (representing the person)
def create_prism(position, height=1.82, width=0.5, depth=0.3):
    x, y, z = position
    vertices = np.array([
        [x, y, z], [x + width, y, z], [x + width, y + depth, z], [x, y + depth, z],  # Bottom face
        [x, y, z + height], [x + width, y, z + height], [x + width, y + depth, z + height], [x, y + depth, z + height]  # Top face
    ])
    faces = [
        [vertices[j] for j in [0, 1, 5, 4]], [vertices[j] for j in [7, 6, 2, 3]],  # Sides
        [vertices[j] for j in [0, 1, 2, 3]], [vertices[j] for j in [4, 5, 6, 7]],  # Bottom and Top
        [vertices[j] for j in [0, 3, 7, 4]], [vertices[j] for j in [1, 2, 6, 5]]   # Other Sides
    ]
    return faces

# Function for position 1 (start position)
def position1():
    quadrant_choice = random.choice(["QIV", "QIII"])
    if quadrant_choice == "QIV":
        return np.array([50, -50, 0])
    else:
        return np.array([-50, -50, 0])

# Function for position 2 (second position)
def position2(start_pos):
    if np.array_equal(start_pos, np.array([50, -50, 0])):
        return np.array([7/2, -4, 0])
    else:
        return np.array([-7/2, -4, 0])

# Function for position 3 (third position - universal)
def position3():
    return np.array([0, 0, 0])

# Function for position 4 (fourth position - random movement within an area)
def position4():
    x = random.uniform(-64, 36)
    y = random.uniform(0, 56.5)
    return np.array([x, y, 0])

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the grid limits
ax.set_xlim([-135, 135])
ax.set_ylim([-135, 135])
ax.set_zlim([0, 135])

# Initial position (start position)
start_pos = position1()

# Define the positions
second_pos = position2(start_pos)
third_pos = position3()

# Sequence of positions
positions = [start_pos, second_pos, third_pos]

# Add random positions in the fourth area
for _ in range(10):  # Move randomly 10 times within the specified area
    positions.append(position4())

# Interpolate between positions for smoother transitions
def interpolate_positions(pos1, pos2, steps):
    return [pos1 + (pos2 - pos1) * i / steps for i in range(steps)]

# Increase smoothness by interpolating between positions
smooth_positions = []
for i in range(len(positions) - 1):
    smooth_positions.extend(interpolate_positions(positions[i], positions[i+1], 50))

# Create the initial prism
prism_faces = create_prism(start_pos)
prism = Poly3DCollection(prism_faces, color='blue', alpha=0.7)
ax.add_collection3d(prism)

# Function to update the position of the prism in each frame
def update(frame):
    pos = smooth_positions[frame]
    new_faces = create_prism(pos)
    prism.set_verts(new_faces)
    return prism,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(smooth_positions), interval=100, blit=False)

# Display the animation
plt.show()
