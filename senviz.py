import matplotlib.pyplot as plt
import numpy as np
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import numpy

fig, ax = plt.subplots()

# create sensors
patches = []

def add_sensor(x_pos, y_pos, view_distance, fov, start_degree="inf", blindzone=0.0, color="blue", z_order=0.0):
    if start_degree == "inf":
        start_degree = 90-fov/2
    patches.append(mpatches.Wedge((x_pos, y_pos), view_distance, start_degree, fov + start_degree, color=color, ec="none", width=view_distance - blindzone, zorder=z_order))

# CAMERAS

# left 
add_sensor(0.32, 0, 80, 60, 0, blindzone=5.0, color="blue")
# left central
add_sensor(0.32, 0, 80, 60, 40, blindzone=5.0, color="blue")
# right central
add_sensor(-0.32, 0, 80, 60, 80, blindzone=5.0, color="blue")
# right
add_sensor(-0.32, 0, 80, 60, 120, blindzone=5.0, color="blue")
# central
add_sensor(-0.32, 0, 120, 30, blindzone=8.0, color="yellow", z_order=-1)

# LIDARS
# 360 LIDAR
add_sensor(0, 0, 45, 360, blindzone=6.5, color="red", z_order=-1)

# close range lidar
add_sensor(0, 0, 8.0, 360, color="orange")

# plot all items
collection = PatchCollection(patches, alpha=0.25, match_original=True)
ax.add_collection(collection)

# add vehicle model at the end
v_x = 5
v_y = 25
collection = PatchCollection([mpatches.Rectangle((-v_x/2, -v_y), v_x, v_y, color="grey")], match_original=True)
ax.add_collection(collection)

plt.xlabel('distance [m]')
plt.ylabel('distance [m]')
plt.axis('equal')
plt.tight_layout()
#plt.grid()

plt.show()
