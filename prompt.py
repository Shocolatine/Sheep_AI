import numpy as np
import matplotlib.pyplot as plt

def create_image_from_grid(grid):
    cmap = plt.get_cmap('viridis', 5)

    # Replace eights with the last non-zero number (2, 3, or 4) in each row
    modified_grid = np.zeros_like(grid)
    for i in range(grid.shape[0]):
        row = grid[i, :]
        non_zero_indices = (row != 0).nonzero()[0]
        for j in non_zero_indices:
            if row[j] != 8:
                tmp=row[j]
            if tmp == 8:
                modified_grid[i, j] = tmp
                continue
            modified_grid[i, j] = tmp


     # Create the plot with custom ticks and color map
    fig, ax = plt.subplots()
    im = ax.imshow(modified_grid, interpolation='nearest', cmap=cmap, vmin=0, vmax=4)

    # Set ticks and labels for x and y axes
    ax.set_xticks(np.arange(grid.shape[1]))
    ax.set_yticks(np.arange(grid.shape[0]))
    ax.set_xticklabels(np.arange(1, grid.shape[1] + 1))
    ax.set_yticklabels(np.arange(1, grid.shape[0] + 1))

    # Set color bar with custom ticks
    cbar = plt.colorbar(im, ticks=[0, 1, 2, 3, 4])
    cbar.set_label('Values')

    # Save the plot to an image file (e.g., PNG)
    plt.savefig('grid_image.png', bbox_inches='tight')