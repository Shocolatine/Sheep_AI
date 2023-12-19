import numpy as np

def create_grid(data):
    # Create an 8x10 grid filled with zeros
    grid = np.zeros((10, 8), dtype=int)

    # Populate the grid based on the data
    for size, coordinates in data.items():
        for coord in coordinates:
            x, y = coord
            block_width = int(size.split()[-1])
            grid[y-1, x-block_width:x] = int(size[-1])

    return grid