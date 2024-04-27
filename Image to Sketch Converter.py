#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install opencv-python


# In[ ]:


import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

class ImageToSketchConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Sketch Converter")

        # Variables
        self.image_path = None
        self.output_image = None

        # GUI Elements
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.convert_button = tk.Button(root, text="Convert to Sketch", command=self.convert_to_sketch)
        self.convert_button.pack()

        self.save_button = tk.Button(root, text="Save Sketch", command=self.save_sketch)
        self.save_button.pack()

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            self.preview_image()

    def preview_image(self):
        image = Image.open(self.image_path)
        image.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def convert_to_sketch(self):
        if self.image_path:
            original_image = cv2.imread(self.image_path)
            gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
            inverted_image = 255 - gray_image
            blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
            inverted_blurred_image = 255 - blurred_image
            pencil_sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
            self.output_image = pencil_sketch
            self.preview_sketch(pencil_sketch)

    def preview_sketch(self, sketch):
        sketch = cv2.resize(sketch, (400, 400))
        sketch_image = Image.fromarray(sketch)
        photo = ImageTk.PhotoImage(sketch_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def save_sketch(self):
        if self.output_image is not None:
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
            if save_path:
                cv2.imwrite(save_path, self.output_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToSketchConverter(root)
    root.mainloop()


# In[6]:


pip install tkinter pillow


# In[ ]:




