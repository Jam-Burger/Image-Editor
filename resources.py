from tkinter import *
from PIL import Image, ImageTk

def tk_img(path, size):
    img = Image.open(path).resize(size)
    return ImageTk.PhotoImage(img)
class Images:
    def __init__(self):
        self.logo= tk_img("images/Imagify-logo.jpeg", (100, 100))
        icon_size= (40, 40)
        self.rotate_a_img = tk_img("images/rotate_a.png", icon_size)
        self.rotate_c_img = tk_img("images/rotate_c.png", icon_size)

        self.flip_h_img = tk_img("images/flip_h.png", icon_size)
        self.flip_v_img = tk_img("images/flip_v.png", icon_size)

        self.crop_rotate_img = tk_img("images/crop.png", icon_size)
        self.adjust_img = tk_img("images/brightness.png", icon_size)

        self.invert_img = tk_img("images/invert.png", icon_size)
        self.resize_img = tk_img("images/resize.png", icon_size)

        self.undo_img = tk_img("images/undo.png", icon_size)
        self.redo_img = tk_img("images/redo.png", icon_size)
    