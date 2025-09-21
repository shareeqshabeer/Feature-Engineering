import os
from PIL import Image
import numpy as np

# Set the hardcoded paths for the images
image_paths = [
    '/home/user/Desktop/fe_images/fe1.jpeg',  # Replace with the actual paths
    '/home/user/Desktop/fe_images/fe3.jpeg'
]

# Set the output directory to save normalized images
output_dir = '/home/user/Desktop/fe_images/'  # Path to save normalized images

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through the hardcoded image paths and normalize
for i, img_path in enumerate(image_paths):
    # Load the image
    img = Image.open(img_path)

    # Convert the image to a NumPy array for normalized
    img_array = np.array(img)
        
    # Normalize the original image to [0, 1]
    img_normalized = img_array / 255.0  # Normalize to range [0, 1]
        
    # Convert the normalized NumPy array back to an image
    img_normalized_pil = Image.fromarray((img_normalized * 255).astype(np.uint8))
    
    # Create a filename for the normalized image
    normalized_image_path = output_dir+'/normalized_'+str(i+1)+'_'+os.path.basename(img_path)
    print(normalized_image_path)
    
    # Save the normalized image
    img_normalized_pil.save(normalized_image_path)
    print('Saved normalized image:',normalized_image_path)

