import csv
from PIL import Image
import numpy as np
import os

if not os.path.exists('src\\main\\webapp'):
    os.makedirs('src\\main\\webapp')

print(os.path.dirname(os.path.abspath(__file__)))

try:
    base = Image.open('C:\\InnovationFiles\\base_image.png').convert('RGB')

except FileNotFoundError:
    print("Base image not found. Make sure it is in C:\\InnovationFiles and named 'base_image.jpg'")


width = 1200
height = 900

heatmap_info = np.zeros([height, width, 4], dtype=np.uint8)
heatmap_info[:,:] = [255, 255, 255, 0]

try:
    with open("heatmap_points.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            heatmap_info[int(row[0]) + 1, int(row[1]) + 1] = [255, 0, 0, 255]
            heatmap_info[int(row[0]) + 1, int(row[1])] = [255, 0, 0, 255]
            heatmap_info[int(row[0]), int(row[1]) + 1] = [255, 0, 0, 255]
            heatmap_info[int(row[0]), int(row[1])] = [255, 0, 0, 255]
            heatmap_info[int(row[0]) - 1, int(row[1])] = [255, 0, 0, 255]
            heatmap_info[int(row[0]), int(row[1]) - 1] = [255, 0, 0, 255]
            heatmap_info[int(row[0]) - 1, int(row[1]) - 1] = [255, 0, 0, 255]
    img = Image.fromarray(heatmap_info)
    img.convert('RGB')

    # img.paste(im=base, mask=img)

    base.paste(im=img, mask=img)

    base.save('C:\\InnovationFiles\\heatmap.png')
    # blend = Image.blend(im1=img, im2=base, alpha=0.5)
    img.save('C:\\InnovationFiles\\heatmap_empty.png')
    print("heatmap saved.")
except FileNotFoundError:
    print("heatmap_points.csv not found or directory not existing, nothing saved")
