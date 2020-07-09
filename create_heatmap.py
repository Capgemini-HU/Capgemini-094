import csv
from PIL import Image
import numpy as np
import os

if not os.path.exists('src\\main\\webapp'):
    os.makedirs('src\\main\\webapp')

width = 1920
height = 1280

heatmap_info = np.zeros([height, width, 4], dtype=np.uint8)
heatmap_info[:,:] = [255, 255, 255, 0]

try:
    with open("heatmap_points.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            heatmap_info[int(row[0]), int(row[1])] = [255, 0, 0, 255]

    img = Image.fromarray(heatmap_info)
    img.save('src\\main\\webapp\\heatmap.png')
    print("heatmap saved.")
except FileNotFoundError:
    print("heatmap_points.csv not found, nothing saved")
