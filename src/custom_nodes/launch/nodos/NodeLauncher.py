import tkinter as tk
from tkinter import ttk
from nodos import NodeOptions, CalculationOptions, RealsenseOptions, ThermalCameraOptions, YOLOOptions
import subprocess
import signal
import os

class NodeLauncher:
    """ Clase genérica para gestionar nodos ROS2."""
    def __init__(self, parent, title, options):
        print(f"Initializing NodeLauncher for title: {title}, with options class: {type(options).__name__}")
        self.options = options
        self.terminal_process = None

        # Crear frame principal
        self.frame = ttk.Frame(parent)
        self.frame.pack(side="left", fill="y", expand=True, padx=10, pady=10)

        # Etiqueta del nodo
        ttk.Label(self.frame, text=title, font=("Arial", 12, "bold")).pack(pady=5)

        # Terminal embebida
        self.terminal_frame = tk.Frame(self.frame, width=300, height=300, bg="black")
        self.terminal_frame.pack(pady=10)

        # Botones para lanzar, detener y copiar el nodo
        self.create_buttons()
        self.options.create_widgets(self.frame)

    def create_buttons(self):
        button_frame = ttk.Frame(self.frame)
        button_frame.pack(pady=10)

        style = ttk.Style()
        style.configure("Small.TButton", padding=(2, 2), font=("Arial", 11))  # Ajustar padding y fuente

        ttk.Button(button_frame, text="Launch Node", style="Small.Accent.TButton", command=self.launch_node).pack(side="left", padx=1)
        ttk.Button(button_frame, text="Stop Node", style="Small.TButton", command=self.stop_node).pack(side="left", padx=1)
        ttk.Button(button_frame, text="Copy Shell", style="Small.TButton", command=self.copy_terminal_output).pack(side="left", padx=1)

    def generate_command(self):
        """Generar el comando dinámico basado en las opciones."""
        if isinstance(self.options, RealsenseOptions):
            return (
                f"ros2 launch custom_nodes launch_realsense.py "
                f"enable_color:={str(self.options.enable_color.get()).lower()} "
                f"enable_depth:={str(self.options.enable_depth.get()).lower()} "
                f"enable_infra1:={str(self.options.enable_infra1.get()).lower()} "
                f"enable_infra2:={str(self.options.enable_infra2.get()).lower()} "
                f"align_depth:={str(self.options.align_depth.get()).lower()} "
                f"pointcloud:={str(self.options.pointcloud.get()).lower()} "
                f"rgb_resolution:={self.options.rgb_resolution.get()} "
                f"depth_resolution:={self.options.depth_resolution.get()}"
            )
        elif isinstance(self.options, ThermalCameraOptions):
            return f"ros2 launch custom_nodes launch_thermalcamera.py focus:={self.options.focus_value.get()}"
        
        elif isinstance(self.options, YOLOOptions):
            selected_classes = "[" + ",".join(map(str, self.options.get_selected_classes())) + "]"
            return f"ros2 launch ultralytics_ros tracker.launch.xml yolo_model:={self.options.selected_model_name.get()} classes:={selected_classes}"

        elif isinstance(self.options, CalculationOptions):
            return f"python3 ~/sensors_ws/src/custom_nodes/scripts/temperature_cswi_calculation.py"
    
    def launch_node(self):
        if self.terminal_process and self.terminal_process.poll() is None:
            self.stop_node()

        launch_command = self.generate_command()
        # Usar un archivo de logs único para cada nodo
        self.terminal_log_file = f"/tmp/{self.options.__class__.__name__.lower()}_output.log"

        xterm_command = (
            f"xterm -geometry 70x40 -into {self.terminal_frame.winfo_id()} "
            f"-fa Monospace -fs 6 -sb -rightbar -e bash -c '{launch_command} | tee {self.terminal_log_file}'"
        )
        print(f"Lanzando nodo con comando: {xterm_command}")
        self.terminal_process = subprocess.Popen(xterm_command, shell=True, preexec_fn=os.setsid)

        # Actualizar estado del nodo principal
        if isinstance(self.options, ThermalCameraOptions):
            self.options.node_active.set(True)

            # Si el checkbox de Color Range está activado, lanzar el nodo ColorConvert
            if self.options.color_range_active.get():
                print("El checkbox Color Range está activado. Lanzando nodo ColorConvert.")
                self.options.launch_colorconvert_node()

    def stop_node(self):
        if self.terminal_process:
            try:
                if self.terminal_process.poll() is None:
                    os.killpg(os.getpgid(self.terminal_process.pid), signal.SIGINT)
                    self.terminal_process.wait()
                else:
                    print("El nodo ya está detenido.")
            except ProcessLookupError:
                print("El proceso ya no existe.")
            self.terminal_process = None

        # Actualizar estado del nodo
        if isinstance(self.options, ThermalCameraOptions):
            self.options.node_active.set(False)
            self.options.stop_colorconvert_node()

    def copy_terminal_output(self):
        """Copia el contenido de la terminal del nodo actual al portapapeles."""
        if os.path.exists(self.terminal_log_file):
            with open(self.terminal_log_file, 'r') as log_file:
                terminal_content = log_file.read()
                self.frame.clipboard_clear()  # Limpiar el portapapeles
                self.frame.clipboard_append(terminal_content)  # Copiar el contenido de la terminal
                self.frame.update()  # Actualizar el portapapeles
                print(f"Contenido de la terminal copiado al portapapeles desde: {self.terminal_log_file}")
        else:
            print(f"No se encontró el archivo de logs: {self.terminal_log_file}")