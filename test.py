import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from matplotlib.animation import FuncAnimation
import random

""" Function to create a rectangular prism (representing the person) """
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

""" Position 1 is in the parking lot. """
def position1():
    quadrant_choice = random.choice(["QIV", "QIII"])
    return np.array([50, -50, 0] if quadrant_choice == "QIV" else [-50, -50, 0])

""" Position 2 is at the outside doors of the atrium. """
def position2(start_pos):
    return np.array([7/2, -4, 0] if start_pos[0] > 0 else [-7/2, -4, 0])

""" Position 3 is at the front checkin desk. """
def position3():
    return np.array([0, 0, 0])

""" Position 4 is inside the gym. """
def position4():
    x = random.uniform(-64, 36)
    y = random.uniform(0, 56.5)
    return np.array([x, y, 0])

""" Function to generate a random color for each new person """
def random_color():
    return (random.random(), random.random(), random.random())

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-135, 135])
ax.set_ylim([-135, 135])
ax.set_zlim([0, 135])

prisms = []
person_counter = 0
frame_interval = 50  # Number of frames to wait before adding a new person

""" Legend function to display person count """
def legend():
    return f"Person count: {len(prisms)}"

# Display person count on the graph
text_handle = ax.text2D(0.05, 0.95, legend(), transform=ax.transAxes, fontsize=12)

""" Function to interpolate positions for smoother transitions between key points """
def interpolate_positions(pos1, pos2, steps):
    return [pos1 + (pos2 - pos1) * i / steps for i in range(steps)]

""" Function to add a new person at position 1 and manage their movement through positions """
def add_person():
    global person_counter
    start_pos = position1()
    positions = [start_pos, position2(start_pos), position3()]
    positions.extend(position4() for _ in range(10))  # Move randomly 10 times within the specified area
    smooth_positions = []
    for i in range(len(positions) - 1):
        smooth_positions.extend(interpolate_positions(positions[i], positions[i+1], 50))
    
    color = random_color()
    prism = Poly3DCollection(create_prism(start_pos), color=color, alpha=0.7)
    ax.add_collection3d(prism)
    prisms.append({
        'prism': prism,
        'positions': smooth_positions,
        'current_frame': 0
    })
    person_counter += 1
    text_handle.set_text(legend())  # Update legend text

""" Update function for the animation, managing the position of each person frame by frame """
def update(frame):
    global prisms
    if frame % frame_interval == 0 and person_counter < 50:
        add_person()
    for person in prisms:
        if person['current_frame'] < len(person['positions']):
            position = person['positions'][person['current_frame']]
            person['prism'].set_verts(create_prism(position))
            person['current_frame'] += 1

ani = FuncAnimation(fig, update, frames=1000, interval=100, blit=False)
plt.show()
