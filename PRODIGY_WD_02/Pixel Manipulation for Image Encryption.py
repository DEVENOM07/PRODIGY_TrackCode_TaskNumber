from PIL import Image
import os

def process_image(image_path, key, output_path, mode='encrypt'):
    img = Image.open(image_path).convert("RGBA")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b, a = pixels[i, j]

            shift = (i + j + key) % 256

            if mode == 'encrypt':
                r = (r ^ key + shift) % 256
                g = (g ^ (key + 3) + shift) % 256
                b = (b ^ (key + 7) + shift) % 256
            elif mode == 'decrypt':
                r = ((r - shift) % 256) ^ key
                g = ((g - shift) % 256) ^ (key + 3)
                b = ((b - shift) % 256) ^ (key + 7)

            pixels[i, j] = (r, g, b, a)

    img.save(output_path)
    print(f"Image {mode}ed and saved to: {output_path}")

# --- SETTINGS ---
image_path = r"C:\Users\lenovo\Pictures\Screenshots\1.png"  # path to original image
key = 20  # change to your desired secret key
mode = 'encrypt'  # or 'decrypt'

# Save output in the same folder
output_image = os.path.join(os.path.dirname(image_path), f"{mode}_1.png")

# --- RUN ---
process_image(image_path, key, output_image, mode)
