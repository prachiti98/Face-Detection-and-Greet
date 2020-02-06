import cv2
import numpy as np
import matplotlib.pyplot as plt
from face_functions import add_to_database,speak
 

name = input("Enter your Name: ")
print("Press ESC to exit, SPACE to click picture")
add_to_database(name)
