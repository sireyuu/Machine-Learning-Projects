# Used for CIS
# If library doesn't work, pip install Pillow from your terminal
from PIL import Image, ImageTk
import os

# CHANGE: Path to the directory folder containing your images
directory = "C:/Users/Desktop/Sample"

processed_count = 0

# TO: Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):  
        input_image = Image.open(os.path.join(directory, filename))

        # Creating a copy of the input image
        modified_image = input_image.copy()

        # Extracting pixel map
        pixel_map = modified_image.load()

        # Extracting the width and height of the image 
        width, height = modified_image.size

        # For every pixel in the image, add a pink square
        for i in range(width):
            for j in range(height):
                pixel_map[i, j] = (255, 105, 180)  # RGB value for pink

        # Extract the filename and extension
        base_filename, file_extension = os.path.splitext(filename)
        base_filename = base_filename.replace('_bau_sqr', '')
        print("Base Filename:", base_filename)
        print("File Extension:", file_extension)

        # Saves image with naming convention of campaign image
        output_filename_camp_lzd = f"{base_filename}_camp_lzd{file_extension}"
        modified_image.save(os.path.join(directory, output_filename_camp_lzd))

        output_filename_camp_shp = f"{base_filename}_camp_shp{file_extension}"
        modified_image.save(os.path.join(directory, output_filename_camp_shp))

        # Logs in console
        print(f"Added pink square to {filename}")

print("All images processed are located in the same folder together with the original images.")
