# 2- PIL METHODS

### 1- OPENING AND SHOWING IMAGES

You can open and display images using methods like **Image.open()** and **Image.show()**.

- **`Image.open()`** opens an image file and loads it into memory.
- **`Image.show()`** displays the image using the default image viewer on your system.

```python
from PIL import Image

# Open an image
img = Image.open("example.jpg")
img.show()  # Opens the image in the default viewer
```

### 2- IMAGE SIZE, MODE, AND FORMAT

You can get basic information about the image, such as **size**, **mode**, and **format**.

- **`img.size`** returns the dimensions (width, height) of the image.
- **`img.mode`** returns the color space (e.g., RGB, L).
- **`img.format`** gives the format of the image file (e.g., JPEG, PNG).

```python
print(img.size)   # Output: (width, height)
print(img.mode)   # Output: RGB
print(img.format) # Output: JPEG

```

### 3- RESIZING IMAGES

You can resize images using the **`resize()`** method.

- **`resize()`** resizes an image to the specified size, accepting a tuple `(width, height)`.

```python
resized_img = img.resize((300, 400))
resized_img.show()

```

### 4- CROPPING IMAGES

You can crop images using the **`crop()`** method.

- **`crop()`** requires a tuple `(left, upper, right, lower)` to define the box to keep.

```python
cropped_img = img.crop((100, 100, 400, 400))
cropped_img.show()

```

### 5- ROTATING IMAGES

You can rotate images using the **`rotate()`** method.

- **`rotate()`** rotates the image by a specified angle.

```python
rotated_img = img.rotate(90)
rotated_img.show()  # Rotates the image 90 degrees clockwise

```

### 6- SAVING IMAGES

You can save modified images using the **`save()`** method.

- **`save()`** saves the image to a specified file path with a given format.

```python
img.save("output.png")  # Saves the image in PNG format

```

### 7- CONVERTING IMAGE MODES

You can convert images to different color modes (e.g., from RGB to grayscale) using **`convert()`**.

- **`convert()`** is commonly used to change the color mode of the image.

```python
grayscale_img = img.convert("L")  # Convert to grayscale (L mode)
grayscale_img.show()
```
