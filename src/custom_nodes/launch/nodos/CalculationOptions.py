from .NodeOptions import NodeOptions
import tkinter as tk
from tkinter import ttk

class CalculationOptions(NodeOptions):
    """Opciones específicas para el nodo Temperature and CSWI."""
    def __init__(self, yolo_options):
        super().__init__()
        self.yolo_options = yolo_options  # Referencia al nodo Ultralytics

    def create_widgets(self, parent):
        ttk.Label(parent, text="No specific options required", font=("Arial", 12)).pack(anchor="center", pady=5)