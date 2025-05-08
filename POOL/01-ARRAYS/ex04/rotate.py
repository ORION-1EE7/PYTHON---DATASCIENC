from numpy import array, zeros
from PIL import Image
from load_image import ft_load

# def ft_display_image(imgarr: array):
#     img = Image.fromarray(imgarr)
#     # gray_image = img.convert("L")
#     # gray_image.show()
#     img.show()


def ft_transpose(img: array) -> array:
    height, width, c = img.shape
    transposed = zeros((width, height, c), dtype=img.dtype)
    for i in range(height):
        for j in range(width):
            transposed[j][i] = img[i][j]
    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)
    return transposed

img = ft_load("image.jpg")
newimg = ft_transpose(img)
# ft_display_image(newimg)
