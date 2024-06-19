import os
import cv2
import numpy as np
from IPython.display import Image, display
import matplotlib.pyplot as plt

def rgb_to_ir(rgb_image):
    ir_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
    return ir_image

def adjust_contrast(ir_image):
    # Decrease intensity of pixel values
    adjusted_ir_image = cv2.convertScaleAbs(ir_image, alpha=0.7, beta=0)
    return adjusted_ir_image

def generate_heatmap(ir_image):
    ir_colormap = cv2.applyColorMap(ir_image, cv2.COLORMAP_JET)
    return ir_colormap

# Path to the folder containing RGB images
folder_path = '/Users/shefalisingh/desktop/mini_proj/IR/images'

# Create an output directory if it doesn't exist
output_dir = '/Users/shefalisingh/desktop/mini_proj/RGB/images'
os.makedirs(output_dir, exist_ok=True)

# Iterate through each image in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Ensure only image files are processed
        # Read RGB image
        rgb_image = cv2.imread(os.path.join(folder_path, filename))

        # Process the RGB image
        ir_image = rgb_to_ir(rgb_image)
        adjusted_ir_image = adjust_contrast(ir_image)
        ir_colormap = generate_heatmap(adjusted_ir_image)
        resized_rgb_image = cv2.resize(rgb_image, (ir_colormap.shape[1], ir_colormap.shape[0]))
        blended_image = cv2.addWeighted(ir_colormap, 0.2, resized_rgb_image, 0.7, 0)

        # Display the blended image using matplotlib
       # plt.imshow(cv2.cvtColor(blended_image, cv2.COLOR_BGR2RGB))
       # plt.axis('off')
        #plt.show()

        # Save the blended image with the same filename in the output directory
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, blended_image)
        print("Blended image saved at:", output_path)

        # Display the image (Note: this display method may not work in VS Code)
        #display(Image(filename=output_path))
