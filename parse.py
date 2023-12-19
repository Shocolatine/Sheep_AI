import cv2
import numpy as np
from rectangle import tile
from create_grid import create_grid

data = {}
img = cv2.imread('images/grey_img.png')
tempS1 = cv2.imread('images/templates/g1v2.png')
tempS2 = cv2.imread('images/templates/g2v2.png')
tempS3 = cv2.imread('images/templates/g3v2.png')
tempS4 = cv2.imread('images/templates/g4v2.png')

temp_sizes = [tempS1, tempS2, tempS3, tempS4]
colors = [(0, 0, 225), (0, 225, 0), (225, 0, 0), (0, 225, 225)]

for i, (temp_size, color) in enumerate(zip(temp_sizes, colors), start=1):
    ens = tile(img, temp_size, color, i)
    print(ens)
    data.update(ens)

# Create and print the grid
grid = create_grid(data)
print(grid)

cv2.imwrite('images/result.png', img)
result = cv2.imread('images/result.png')
cv2.imshow('resultat', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
