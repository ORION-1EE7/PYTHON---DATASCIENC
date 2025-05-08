import numpy as np
import sys
from numpy import array
from PIL import Image, UnidentifiedImageError

def ft_display_image(imgarr: array):
    img = Image.fromarray(imgarr)
    # grey_image = img.convert("L")
    # grey_image.show()
    img.show()

def ft_load(path: str) -> array:
    try:
        img = Image.open(path)
        img = img.convert("RGB")
        img_array = np.asarray(img)
        img.close()
        print(f"The shape of image is: {img_array.shape}")
        return img_array

    except FileNotFoundError as fnf:
        print("Error: The file was not found.")
        sys.exit(1)
    except UnidentifiedImageError:
        print(f"Error: Cannot identify image file '{path}'")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
        


image = ft_load("image.jpg")
print(image)
ft_display_image(image)