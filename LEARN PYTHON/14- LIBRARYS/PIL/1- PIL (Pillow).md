# 1- PIL (Pillow)

- Pillow is the **Python Imaging Library**, commonly referred to as PIL.

- It is used for **opening, editing, and saving image files** in many formats (JPEG, PNG, BMP, GIF, etc.).
- Useful for tasks like **resizing, cropping, rotating, converting color modes**, and more.

### **INITIALIZATION**

To use Pillow, you must install it (if not already) and import it. The main class for image handling is called Image.

```bash
pip install Pillow
```

```python
from PIL import Image
```

### **EXAMPLE: OPENING IMAGES**

```python
from PIL import Image

# Open an image file
img = Image.open("example.jpg")

# Display the image
img.show()

# Print basic info
print(img.format)  # Output: JPEG
print(img.size)    # Output: (width, height)
print(img.mode)    # Output: RGB

```
