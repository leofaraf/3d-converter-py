from tkinter import filedialog
from tkinter.messagebox import showinfo
from warnings import showwarning
from utils import logger, blender
import logging
import tkinter as tk
import bpy
from tkinter import *

class App:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("3D models convertor")
        self.root.geometry("250x250")
        self.var = StringVar()
        self.var.set("Input file ins't picked")
        self.input_path = None

        open_button = tk.Button(
            self.root,
            text='Pick a File',
            command=self.select_file
        )

        open_button.pack(expand=True)

        l = Label(self.root, textvariable = self.var)
        l.pack(expand=True)

        convert_button = tk.Button(
            self.root,
            text='Convert and Save as',
            command=self.save_file
        )
        convert_button.pack(expand=True)
        self.root.mainloop()

    def select_file(self):
        filetypes = [
            ('obj, dae, glb, fbx, ply, stl', '*.obj;*.dae;*.glb;*.fbx;*.ply;*.stl')
        ]

        input_path = filedialog.askopenfilename(
            title='Pick an input file',
            initialdir='/',
            filetypes=filetypes)

        if input_path:
            self.var.set("Input file is picked\nPress to the button under")
            self.input_path = input_path

    def save_file(self):
        filetypes = (
            ('.OBJ', '*.obj'),
            ('.DAE', '*.dae'),
            ('.GLB', '*.glb'),
            ('.FBX', '*.fbx'),
            ('.PLY', '*.ply'),
            ('.STL', '*.stl')
        )

        output_path = filedialog.asksaveasfilename(
            title="Save As",
            filetypes=filetypes,
            initialdir="./",
            defaultextension=".obj"
        )
        
        if output_path:
            if self.input_path == None:
                showinfo(
                    "Warning",
                    "Please, pick a input file before converting!"
                )
            else:
                blender.convert(
                    self.input_path,
                    self.input_path.split(".")[-1],
                    output_path,
                    output_path.split(".")[-1]
                )
                showinfo(
                    "Info",
                    "Successful"
                )
            

if __name__ == "__main__":
    logger.configure_logger(True)
    app = App()