import os
from PIL import Image

# Set the hardcoded paths for the images
image_paths = [
    '/home/user/Desktop/fe_images/fe1.jpeg',  # Replace with the actual paths
    '/home/user/Desktop/fe_images/fe3.jpeg'
]

# Set the output directory to save transformed images
output_dir = '/home/user/Desktop/fe_images/'  # Path to save transformed images

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Specify the translation amounts (in pixels)
tx = 50  # Translation along X-axis (horizontal shift)
ty = 30  # Translation along Y-axis (vertical shift)

# Loop through the hardcoded image paths and transform
for i, img_path in enumerate(image_paths):
    # Load the image
    img = Image.open(img_path)
    
    # transform the image
    # Apply translation using the affine transformation matrix
        # The matrix [1, 0, tx, 0, 1, ty] means:
        # [1, 0, tx] - X translation
        # [0, 1, ty] - Y translation
    img_transformed = img.transform(img.size, Image.AFFINE, (1, 0, tx, 0, 1, ty))
    
    # Create a filename for the transformed image
    transformed_image_path = output_dir+'/transformed_'+str(i+1)+'_'+os.path.basename(img_path)
    print(transformed_image_path)
    
    # Save the transformed image
    img_transformed.save(transformed_image_path)
    print('Saved transformed image:',transformed_image_path)

