import numpy
import sys
from numpy import array
from PIL import Image, UnidentifiedImageError

def ft_load(path: str) -> array:
    try:
        img = Image.open(path)
        img = img.convert("RGB")
        img_array = numpy.asarray(img)
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
        


# print(ft_load("image.jpg"))