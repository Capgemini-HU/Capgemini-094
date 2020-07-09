import csv
from PIL import Image
import numpy as np

width = 1920
height = 1280

heatmap_info = np.zeros([height, width, 4], dtype=np.uint8)
heatmap_info[:,:] = [255, 255, 255, 0]

with open("example_heatmap_points.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(f'\t{row[0]} works in the {row[1]} department.')
        heatmap_info[int(row[0]), int(row[1])] = [255, 0, 0, 255]
        line_count += 1
    print(f'Processed {line_count} lines.')


img = Image.fromarray(heatmap_info)
img.save('heatmap.png')
