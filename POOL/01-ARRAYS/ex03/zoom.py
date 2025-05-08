
import sys
from numpy import array
from PIL import Image
from load_image import ft_load  

def ft_display_image(imgarr: array):
    img = Image.fromarray(imgarr)
    gray_image = img.convert("L")
    gray_image.show()
    img.show()


def ft_zoom(img: array)->array:
    try:
        shapes = img.shape 
        x_start = shapes[0] // 2
        y_start = shapes[1] // 2
        x_start -= 200
        y_start -= 200
        zoomed = img[y_start:y_start + 400, x_start:x_start + 400] 
        print(f"New shape after slicing: {zoomed.shape} or {zoomed.shape[:2]}")
        print(zoomed)
        return zoomed
    except Exception as e:
        print(f"Zooming failed: {e}")
        sys.exit(1)

image = ft_load("image.jpg")    
zoomed = ft_zoom(image)

# ft_display_image(zoomed)