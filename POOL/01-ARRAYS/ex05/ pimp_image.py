from PIL import Image
from numpy import ndarray
from load_image import ft_load


def ft_display_image(imgarr: ndarray):
    if isinstance(imgarr, Image.Image):
        imgarr.show()
    else:
        img = Image.fromarray(imgarr)
        img.show()

def ft_invert(array):
    return 255 - array

def ft_red(array) -> ndarray:
    red = array.copy()
    red[:, :, 1] = 0 
    red[:, :, 2] = 0  
    return red

def ft_green(array) -> ndarray:
    green = array.copy()
    green[:, :, 0] = 0  
    green[:, :, 2] = 0 
    return green

def ft_blue(array) -> ndarray:
    blue = array.copy()
    blue[:, :, 0] = 0 
    blue[:, :, 1] = 0
    return blue

def ft_grey(array) -> ndarray:
    img = Image.fromarray(array)   
    grey = img.convert("L")
    return grey



array = ft_load("image.jpg")
# filtered_invert = ft_invert(array)
# ft_display_image(filtered_invert)

# filtered_red = ft_red(array)
# ft_display_image(filtered_red)

# filtered_green = ft_green(array)
# ft_display_image(filtered_green)

# filtered_blue = ft_blue(array)
# ft_display_image(filtered_blue)

# filtered_grey = ft_grey(array)
# ft_display_image(filtered_grey)
