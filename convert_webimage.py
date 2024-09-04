import tkinter as tk
from tkinter import filedialog
from PIL import Image

def convert_webp_to_jpeg(input_file, output_file):
    try:
        # Open the .webp image file
        with Image.open(input_file) as img:
            # Convert the image to RGB mode if it isn't already
            img = img.convert('RGB')
            # Save the image as a JPEG file
            img.save(output_file, 'jpeg')
        print(f"Image successfully converted and saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def select_file_and_convert():
    # Create a file dialog to select the input file
    root = tk.Tk()
    root.withdraw()  # Hide the main window (optional)
    
    # Open file dialog to select a .webp file
    input_file = filedialog.askopenfilename(
        title="Select a WEBP image file",
        filetypes=[("WEBP files", "*.webp"), ("All files", "*.*")]
    )
    
    if input_file:
        # Ask for the output file location
        output_file = filedialog.asksaveasfilename(
            title="Save as JPEG",
            defaultextension=".jpeg",
            filetypes=[("JPEG files", "*.jpeg"), ("All files", "*.*")]
        )
        
        if output_file:
            convert_webp_to_jpeg(input_file, output_file)

if __name__ == "__main__":
    select_file_and_convert()
