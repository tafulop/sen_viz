import matplotlib.pyplot as plt
import numpy as np
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import numpy

class Sensor:
    def __init__(self, x, y, range, fov, orientation, blindzone=0, color="blue"):
        self.pos_x = x
        self.pos_y = y
        self.range = range
        self.fov = fov
        self.orient = orientation
        self.blindzone = blindzone
        self.color = color

class SensorContainer:
    sensors = {}
    def add(self, name, sensor):
        self.sensors[name] = sensor

class Vehicle:
    def __init__(self, width, length, color="grey"):
        self.width = width
        self.length = length
        self.color = color

def display(sensors, vehicle, sensor_alpha=0.25, vehicle_alpha=1.0):
    fig, ax = plt.subplots()
    # add sensors
    s_patches = []
    for key in sensors:
        s = sensors[key]
        theta_1 = s.orient - (s.fov/2)
        theta_2 = s.orient + (s.fov/2)
        wedge = mpatches.Wedge((s.pos_x, s.pos_y), s.range, theta_1, theta_2, color=s.color, ec="none", width=s.range - s.blindzone, label=key)
        s_patches.append(wedge)

    collection = PatchCollection(s_patches, alpha=sensor_alpha, match_original=True)
    ax.add_collection(collection)
    # add vehicle
    ax.add_collection(PatchCollection([mpatches.Rectangle((-vehicle.width/2.0, -vehicle.length), vehicle.width, vehicle.length, color="grey")], alpha=vehicle_alpha, match_original=True))
    # displaying content
    plt.legend(loc=0, handles=s_patches)
    plt.xlabel('distance [m]')
    plt.ylabel('distance [m]')
    plt.axis('equal')
    plt.tight_layout()
    #plt.grid()
    plt.show()

# add a few sensors
sensors = SensorContainer()
sensors.add("camera_1", Sensor(0,0,40,60,30,6,"yellow"))
sensors.add("camera_2", Sensor(0,0,40,60,60,6,"green"))
sensors.add("camera_3", Sensor(0,0,80,30,90,10,"blue"))
sensors.add("camera_4", Sensor(0,0,40,60,120,6,"black"))
sensors.add("camera_5", Sensor(0,0,40,60,150,6,"orange"))
sensors.add("lidar_360", Sensor(0,0,35,360,90,7.5,"red"))

# add a vehicle
vehicle = Vehicle(5.0, 20.0)

display(sensors.sensors, vehicle)
