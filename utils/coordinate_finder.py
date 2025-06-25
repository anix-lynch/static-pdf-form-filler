#!/usr/bin/env python3
"""
Interactive PDF Coordinate Finder
Click on PDF to get exact coordinates for form field mapping
"""
import fitz
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import io
import sys

class PDFCoordinateFinder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PDF Coordinate Finder")
        self.doc = None
        self.page = None
        self.coordinates = {}
        
    def load_pdf(self):
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if pdf_path:
            self.doc = fitz.open(pdf_path)
            self.page = self.doc[0]  # First page
            self.display_page()
    
    def display_page(self):
        # Convert PDF page to image
        mat = fitz.Matrix(2, 2)  # Scale factor
        pix = self.page.get_pixmap(matrix=mat)
        img_data = pix.tobytes("ppm")
        
        # Display in tkinter
        img = Image.open(io.BytesIO(img_data))
        photo = ImageTk.PhotoImage(img)
        
        canvas = tk.Canvas(self.root, width=img.width, height=img.height)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo  # Keep reference
        
        # Bind click event
        canvas.bind("<Button-1>", self.on_click)
        
        # Instructions
        tk.Label(self.root, text="Click where you want form fields. Coordinates will print to console.").pack()
    
    def on_click(self, event):
        x, y = event.x // 2, event.y // 2  # Adjust for scale factor
        print(f"Clicked at coordinates: x={x}, y={y}")
        
        # Prompt for field name
        field_name = input("Enter field name for this location: ")
        self.coordinates[field_name] = {'x': x, 'y': y, 'page': 0}
        print(f"Saved {field_name}: {self.coordinates[field_name]}")
    
    def run(self):
        tk.Button(self.root, text="Load PDF", command=self.load_pdf).pack()
        self.root.mainloop()

if __name__ == "__main__":
    try:
        finder = PDFCoordinateFinder()
        finder.run()
    except ImportError:
        print("GUI libraries not available. Install with: pip install pillow")
        print("Or use the command-line analyzer instead.")
