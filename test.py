import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from matplotlib.animation import FuncAnimation

# Function to create a rectangular prism (representing the person)
def create_person(position, height=1.82, width=0.5, depth=0.3):
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

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the grid limits
ax.set_xlim([-135, 135])
ax.set_ylim([-135, 135])
ax.set_zlim([0, 135])

# Initial position of the prism
start_pos = np.array([50, -50, 0])
target_pos = np.array([0, 0, 0])

# Create the initial prism
prism_faces = create_prism(start_pos)
prism = Poly3DCollection(prism_faces, color='blue', alpha=0.7)
ax.add_collection3d(prism)

# Function to update the position of the prism in each frame
def update(frame):
    # Interpolate position between start and target
    new_pos = start_pos + (target_pos - start_pos) * frame / 100
    # Update the prism's faces with the new position
    new_faces = create_prism(new_pos)
    prism.set_verts(new_faces)
    return prism,

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=False)

# Display the animation
plt.show()
