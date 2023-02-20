#implement trigonometric functions
import math


#find the sine
def get_sine(x):
    #x in degrees
    angle_rad = math.radians(x)
    angle_sin = math.sin(angle_rad)
    return angle_sin