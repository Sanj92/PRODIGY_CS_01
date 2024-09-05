from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Open the image and convert it to an array
    img = Image.open(input_path)
    pixels = np.array(img)

    # Encrypt the image by adding the key value to each pixel
    encrypted_pixels = (pixels + key) % 256

    # Save the encrypted image
    encrypted_img = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_img.save(output_path)

def decrypt_image(input_path, output_path, key):
    # Open the image and convert it to an array
    img = Image.open(input_path)
    pixels = np.array(img)

    # Decrypt the image by subtracting the key value from each pixel
    decrypted_pixels = (pixels - key) % 256

    # Save the decrypted image
    decrypted_img = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_img.save(output_path)

if __name__ == "__main__":
    # Paths to input and output images
    input_image_path = 'input_image.jpg'
    encrypted_image_path = 'encrypted_image.jpg'
    decrypted_image_path = 'decrypted_image.jpg'

    # Key for encryption/decryption
    key = 50  # A simple key value for pixel manipulation

    # Encrypt the image
    encrypt_image(input_image_path, encrypted_image_path, key)
    print(f"Image encrypted and saved to {encrypted_image_path}")

    # Decrypt the image
    decrypt_image(encrypted_image_path, decrypted_image_path, key)
    print(f"Image decrypted and saved to {decrypted_image_path}")
