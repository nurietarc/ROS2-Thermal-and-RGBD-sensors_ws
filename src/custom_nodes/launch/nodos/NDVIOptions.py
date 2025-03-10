from .NodeOptions import NodeOptions
import tkinter as tk
from tkinter import ttk

class NDVIOptions(NodeOptions):
    def __init__(self):
        super().__init__()

    def create_widgets(self, parent):
        ttk.Label(parent, text="No specific options required", font=("Arial", 12)).pack(anchor="center", pady=5)