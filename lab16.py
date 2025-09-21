import os
from PIL import Image

# Set the hardcoded paths for the images
image_paths = [
    '/home/user/Desktop/fe_images/fe1.jpeg',  # Replace with the actual paths
    '/home/user/Desktop/fe_images/fe3.jpeg'
]

# Set the output directory to save rotated images
output_dir = '/home/user/Desktop/fe_images/'  # Path to save rotated images

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Specify the target size for rotating
rotation_angle = 90  # Change this to your desired size

# Loop through the hardcoded image paths and resize
for i, img_path in enumerate(image_paths):
    # Load the image
    img = Image.open(img_path)
    
    # rotate the image
    img_rotated = img.rotate(rotation_angle)
    
    # Create a filename for the rotated image
    rotated_image_path = output_dir+'/rotated_'+str(i+1)+'_'+os.path.basename(img_path)
    print(rotated_image_path)
    
    # Save the rotated image
    img_rotated.save(rotated_image_path)
    print('Saved rotated image:',rotated_image_path)

