import os
from PIL import Image

# Set the hardcoded paths for the images
image_paths = [
    '/home/user/Desktop/fe_images/fe1.jpeg',  # Replace with the actual paths
    '/home/user/Desktop/fe_images/fe3.jpeg'
]

# Set the output directory to save resized images
output_dir = '/home/user/Desktop/fe_images/'  # Path to save resized images

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Specify the target size for resizing
target_size = (256, 256)  # Change this to your desired size

# Loop through the hardcoded image paths and resize
for i, img_path in enumerate(image_paths):
    # Load the image
    img = Image.open(img_path)
    
    # Resize the image
    img_resized = img.resize(target_size)
    
    # Create a filename for the resized image
    resized_image_path = output_dir+'/resized_'+str(i+1)+'_'+os.path.basename(img_path)
    print(resized_image_path)
    
    # Save the resized image
    img_resized.save(resized_image_path)
    print('Saved resized image:',resized_image_path)
