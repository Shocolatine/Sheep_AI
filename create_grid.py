import numpy as np
import random

def create_grid(data):
    # Create an 8x10 grid filled with zeros
    grid = np.zeros((10, 8), dtype=int)

    # Populate the grid based on the data
    for size, coordinates in data.items():
        for coord in coordinates:
            x, y = coord
            block_width = int(size.split()[-1])
            
            # Fill the block with its corresponding value and the rest with 8
            grid[y-1, x-block_width:x] = [int(size[-1])] + [8] * (block_width - 1)

    return grid

def remove_and_add_line(grid):
    grid = grid[1:]
    new_line = generate_random_line()
    grid = np.vstack((grid, np.array(new_line)))
    return grid

def generate_random_line():
    possible_lines = ["4 8 8 8", "3 8 8", "2 8", "1", "0"]
    
    while True:
        # Initialize an empty list to store the line numbers
        line_numbers = []
        
        # Randomly select from possible_lines until the line contains exactly 8 numbers
        while len(line_numbers) != 8:
            if len(line_numbers) > 8:
                    line_numbers = []
            random_line = random.choice(possible_lines)
            line_numbers.extend([int(x) for x in random_line.split()])
        
        # Check if the sum of numbers (excluding eights) is greater than 3 and less than 8
        if 3 < sum(num for num in line_numbers if num != 8) < 8:
            print("\n")
            print(line_numbers)
            print("\n")
            return line_numbers