import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    """Generates the Mandelbrot set."""
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2)

def mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    """Calculates the mandelbrot set."""
    r1, r2 = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    return np.array([[check_mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2])

def check_mandelbrot(c, max_iter):
    """Checks if a point is in the Mandelbrot set."""
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n

def plot_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter, core_color, glow_color):
    """Plots the Mandelbrot set with color for core and glow effects."""
    
    mandelbrot_image = mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)

    # Determine background color based on core color
    if core_color == 'black':
        background_color = (0, 0, 0)  # black
    elif core_color == 'white':
        background_color = (1, 1, 1)  # white
    else:
        background_color = (1, 1, 1)  # default to white for all other colors

    # Create an RGB color image initialized to the background color with float64 type
    color_image = np.full((height, width, 3), background_color, dtype=np.float64)

    # Set core color for points in the Mandelbrot set
    core_mask = mandelbrot_image == max_iter
    color_image[core_mask] = colors.to_rgb(core_color)

    # Calculate a glow effect around the edges
    for i in range(max_iter):
        glow_mask = (mandelbrot_image > i) & (mandelbrot_image < max_iter)
        
        # Use white glow for black core, gray for white core, otherwise use glow color
        if core_color == 'black':
            glow_color_rgb = (1, 1, 1)  # white glow
        elif core_color == 'white':
            glow_color_rgb = (0.5, 0.5, 0.5)  # gray glow
        else:
            glow_color_rgb = colors.to_rgb(glow_color)

        # Safely add glow color with float type
        color_image[glow_mask] += (i / max_iter) * np.array(glow_color_rgb, dtype=np.float64)

    # Clip values to not exceed 1
    color_image = np.clip(color_image, 0, 1)

    # Display the image
    plt.imshow(color_image, extent=(xmin, xmax, ymin, ymax))
    plt.title('Mandelbrot Set with Glow Effect')
    plt.xlabel('Real Part')
    plt.ylabel('Imaginary Part')
    plt.axis('off')  # Turn off the axis
    plt.show()

# Get user input for favorite colors including black and white
print("Available colors: red, orange, yellow, green, blue, indigo, violet, black, white")
favorite_color1 = input("What's your first favorite color for the core? ").lower()
favorite_color2 = input("What's your second favorite color for the glow? ").lower()

# Define valid colors
valid_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'black', 'white']
if favorite_color1 not in valid_colors or favorite_color2 not in valid_colors:
    print("One or both of the colors entered are invalid. Please use valid colors including black and white.")
else:
    # Set parameters for the Mandelbrot set
    xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
    width, height = 800, 800
    max_iter = 100

    # Plot the Mandelbrot set with the specified colors
    plot_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter, favorite_color1, favorite_color2)
