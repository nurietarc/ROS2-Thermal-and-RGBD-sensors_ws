from nodos.NodeLauncher import NodeLauncher
from nodos.NodeOptions import NodeOptions
from nodos import CalculationOptions, RealsenseOptions, ThermalCameraOptions, YOLOOptions, NDVIOptions

import tkinter as tk
from tkinter import ttk

class ROS2App:
    def __init__(self, root):
        self.root = root
        self.root.title("ROS2 Launcher")
        self.root.geometry("1400x900")
        root.tk.call("source", "custom_nodes/launch/azure.tcl")
        root.tk.call("set_theme", "light")

        # Define el estilo de botón pequeño
        root.tk.call("ttk::style", "configure", "Small.Accent.TButton",
                    "-font", "Arial 11",
                    "-padding", "2 2",
                    "-background", "#007fff")

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Create Notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.main_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.main_tab, text="Detection, Temperature and CSWI")
        self.create_main_tab_widgets()

        self.NDVI_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.NDVI_tab , text="NDVI")
        self.create_NDVI_tab_widgets()

    def create_main_tab_widgets(self):
        # Nodo Realsense
        self.realsense_launcher = NodeLauncher(
            self.main_tab, title="RGB Camera - Realsense Node", options=RealsenseOptions()
        )
        self.thermalcamera_launcher = NodeLauncher(
            self.main_tab, title="Thermal Camera - Optris Node", options=ThermalCameraOptions()
        )

        self.yolo_launcher = NodeLauncher(
            self.main_tab, title="Yolo segmentation - Ultralytics Node", options=YOLOOptions()
        )

        self.calculation_launcher = NodeLauncher(
            self.main_tab, title="Temperature and CSWI", options=CalculationOptions(self.yolo_launcher.options)
        )

    def create_NDVI_tab_widgets(self):
        print("prueba")
        self.NDVI_launcher = NodeLauncher(
            self.NDVI_tab, title="NVDIA", options=NDVIOptions()
        )
    def on_closing(self):
        """Acciones al cerrar la aplicación."""
        self.realsense_launcher.stop_node()
        self.thermalcamera_launcher.stop_node()
        self.yolo_launcher.stop_node()
        self.calculation_launcher.stop_node()


        thermal_camera_options = self.thermalcamera_launcher.options
        if isinstance(thermal_camera_options, ThermalCameraOptions):
            thermal_camera_options.stop_colorconvert_node()

        self.root.quit()
        self.root.destroy()


root = tk.Tk()
app = ROS2App(root)
root.mainloop()
