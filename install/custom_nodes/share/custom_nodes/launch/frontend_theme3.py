import tkinter as tk
from tkinter import ttk
import subprocess
import os
import signal
from tkinter import messagebox
import threading
import rclpy
import time

class NodeOptions:
    """Clase base para opciones de configuración de un nodo."""
    def create_widgets(self, parent):
        raise NotImplementedError("Este método debe ser implementado por subclases.")

class RealsenseOptions(NodeOptions):
    """ Opciones específicas para el nodo Realsense."""
    def __init__(self):
        super().__init__()
        self.enable_color = tk.BooleanVar(value=True)
        self.enable_depth = tk.BooleanVar(value=False)
        self.enable_infra = tk.BooleanVar(value=False)
        self.enable_infra1 = tk.BooleanVar(value=False)
        self.enable_infra2 = tk.BooleanVar(value=False)
        self.align_depth = tk.BooleanVar(value=False)
        self.pointcloud = tk.BooleanVar(value=False)
        self.rgb_resolution = tk.StringVar(value="1280x720x30")
        self.depth_resolution = tk.StringVar(value="640x480x30")
        self.extra_rgb, self.extra_depth, self.extra_infra = None, None, None

    def create_widgets(self, parent):
        ttk.Checkbutton(parent, text="Enable RGB", variable=self.enable_color, command=lambda: self.toggle_rgb_options(parent), style="Switch.TCheckbutton").pack()
        ttk.Checkbutton(parent, text="Enable Depth", variable=self.enable_depth, command=lambda: self.toggle_depth_options(parent), style="Switch.TCheckbutton").pack()
        ttk.Checkbutton(parent, text="Enable Infra", variable=self.enable_infra, command=lambda: self.toggle_infra_options(parent), style="Switch.TCheckbutton").pack()
        
        # Crear widgets adicionales en base a estados iniciales
        if self.enable_color.get(): self.create_extra_rgb(parent)
        if self.enable_depth.get(): self.create_extra_depth(parent)
        if self.enable_infra.get(): self.create_extra_infra(parent)

    def create_extra_rgb(self, parent):
        if not self.extra_rgb:
            frame = ttk.Frame(parent)
            frame.pack(pady=5)
            ttk.Label(frame, text="RGB Resolution").pack(side="left")
            ttk.Combobox(frame, textvariable=self.rgb_resolution,
                         values=["1280x720x30", "640x480x30", "640x480x15"], width=13).pack(side="left")
            self.extra_rgb = frame

    def destroy_extra_rgb(self):
        if self.extra_rgb:
            self.extra_rgb.destroy()
            self.extra_rgb = None

    def create_extra_depth(self, parent):
        if not self.extra_depth:
            # Contenedor principal
            frame = ttk.LabelFrame(parent, text="Depth Configuration", padding=5)
            frame.pack(pady=5)  # Expandir y centrar

            # Fila para el Label y el Combobox
            row1 = ttk.Frame(frame)
            row1.pack(side="top", pady=5, anchor="center")  # Centrar la fila
            ttk.Label(row1, text="Depth Resolution").pack(side="left", padx=5)  # Label a la izquierda
            ttk.Combobox(row1, textvariable=self.depth_resolution, values=["640x480x30", "848x480x30", "1280x720x30"], width=13).pack(side="left", padx=5)  # Combobox a la derecha

            # Fila para los Checkbuttons
            row2 = ttk.Frame(frame)
            row2.pack(side="top", pady=5, anchor="center")  # Centrar la fila
            ttk.Checkbutton(row2, text="Align Depth", variable=self.align_depth).pack(side="left", padx=5)
            ttk.Checkbutton(row2, text="Pointcloud", variable=self.pointcloud).pack(side="left", padx=5)

            # Guardar referencia al frame
        self.extra_depth = frame

    def destroy_extra_depth(self):
        if self.extra_depth:
            self.extra_depth.destroy()
            self.extra_depth = None

    def create_extra_infra(self, parent):
        if not self.extra_infra:
            # Contenedor principal
            frame = ttk.LabelFrame(parent, text="Infrared Configuration", padding=5)
            frame.pack(pady=5)  # Expandir y centrar

            # Fila para el Label y el Combobox
            row1 = ttk.Frame(frame)
            row1.pack(side="top", pady=5, anchor="center")  # Centrar la fila
            ttk.Label(row1, text="Depth Resolution").pack(side="left", padx=5)  # Label a la izquierda
            ttk.Combobox(row1, textvariable=self.depth_resolution, values=["640x480x30", "848x480x30", "1280x720x30"], width=13).pack(side="left", padx=5)  # Combobox a la derecha

            # Fila para los Checkbuttons
            row2 = ttk.Frame(frame)
            row2.pack(side="top", pady=5, anchor="center")  # Centrar la fila
            ttk.Checkbutton(row2, text="Infra 1", variable=self.enable_infra1).pack(side="left", padx=5)
            ttk.Checkbutton(row2, text="Infra 2", variable=self.enable_infra2).pack(side="left", padx=5)

            # Guardar referencia al frame
            self.extra_infra = frame

    def destroy_extra_infra(self):
        if self.extra_infra:
            self.extra_infra.destroy()
            self.extra_infra = None

    def toggle_rgb_options(self, parent):
        if self.enable_color.get(): self.create_extra_rgb(parent)
        else: self.destroy_extra_rgb()

    def toggle_depth_options(self, parent):
        if self.enable_depth.get(): self.create_extra_depth(parent)
        else: self.destroy_extra_depth()

    def toggle_infra_options(self, parent):
        if self.enable_infra.get(): self.create_extra_infra(parent)
        else: self.destroy_extra_infra()

class ThermalCameraOptions(NodeOptions):
    """ Opciones específicas para el segundo nodo."""
    def __init__(self):
        self.focus_value = tk.IntVar(value=70)  # Valor inicial del deslizador
        self.color_range_active = tk.BooleanVar(value=True)  # Inicializar el estado del nodo colorconvert
        self.terminal_frame = None  # Frame para la terminal embebida
        self.colorconvert_process = None  # Proceso del nodo colorconvert
        self.node_active = tk.BooleanVar(value=False)  # Nuevo: Estado del nodo
        
    def create_widgets(self, parent):
        tk.Label(
            parent,
            text="Position of focus motor in % of range [0; 100]; Set to -1 value to disable focus change on startup.",
            wraplength=300,  # Ajustar texto a líneas
            justify="center"
        ).pack(anchor="center")

        # Crear el Scale y vincularlo al evento de actualización
        value_label = ttk.Label(parent, text=str(self.focus_value.get()))
        value_label.pack(anchor="center")

        ttk.Scale(
            parent,
            from_=-1,
            to=100,
            orient="horizontal",
            variable=self.focus_value,
            length=300,
            command=lambda val: value_label.config(text=f"{float(val):.0f}")
        ).pack(anchor="center")

        # Botón para activar el nodo colorconvert
        ttk.Checkbutton(
            parent,
            text="Activate Color Range",
            variable=self.color_range_active,
            command=lambda: self.toggle_colorconvert_node(parent),
            style="Switch.TCheckbutton"
        ).pack(anchor="center", pady=10)

        # Crear la terminal embebida al cargar los widgets
        self.terminal_frame = tk.Frame(parent, width=300, height=100, bg="black")
        self.terminal_frame.pack(anchor="center", pady=10)

        self.colorconvert_log_file = "/tmp/colorconvert_output.log"
        xterm_command = (
            f"xterm -geometry 82x20 -into {self.terminal_frame.winfo_id()} "
            "-fa Monospace -fs 6 -sb -rightbar"
        )
        print(f"Inicializando terminal embebida: {xterm_command}")
        subprocess.Popen(xterm_command, shell=True, preexec_fn=os.setsid)

        # Crear el botón "Copy Shell"
        button_frame = tk.Frame(parent)
        button_frame.pack(anchor="center", pady=5)

        ttk.Button(
            button_frame,
            text="Copy Shell",
            command=self.copy_shell_command
        ).pack(anchor="center", padx=5)

    def toggle_colorconvert_node(self, parent):
        """Gestiona el estado del checkbox ColorConvert."""
        if self.color_range_active.get():  # Si el checkbox está activado
            print("Color Range activado.")
            if self.is_thermalcamera_active():
                print("Nodo principal ya está activo. Lanzando nodo ColorConvert.")
                self.launch_colorconvert_node()
            else:
                print("Nodo principal no está activo. Nodo ColorConvert se lanzará cuando el principal se inicie.")
        else:
            print("Color Range desactivado. Deteniendo nodo ColorConvert.")
            self.stop_colorconvert_node()

    def launch_colorconvert_node(self):
        """Lanza el nodo ColorConvert y redirige su salida a un archivo de logs."""
        if self.colorconvert_process and self.colorconvert_process.poll() is None:
            print("ColorConvert node is already running.")
            return

        self.colorconvert_log_file = "/tmp/colorconvert_output.log"
        # Redirigir stderr a stdout con `2>&1`
        launch_command = "stdbuf -oL ros2 run optris_drivers2 optris_colorconvert_node 2>&1"
        xterm_command = (
            f"xterm -geometry 82x20 -into {self.terminal_frame.winfo_id()} "
            f"-fa Monospace -fs 6 -sb -rightbar -e bash -c '{launch_command} | tee {self.colorconvert_log_file}'"
        )
        print(f"Lanzando nodo ColorConvert con comando: {xterm_command}")
        self.colorconvert_process = subprocess.Popen(xterm_command, shell=True, preexec_fn=os.setsid)

    def is_thermalcamera_active(self):
        """Devuelve el estado del nodo basado en la interfaz."""
        return self.node_active.get()

    def copy_shell_command(self):
        """Copia el contenido de la terminal del nodo ColorConvert al portapapeles."""
        if os.path.exists(self.colorconvert_log_file):
            with open(self.colorconvert_log_file, 'rb') as log_file:  # Abrir en modo binario
                try:
                    raw_content = log_file.read()  # Leer todo el contenido
                    # Filtrar caracteres imprimibles (ASCII 32-126, tab, newline, carriage return)
                    filtered_content = ''.join(
                        chr(byte) for byte in raw_content if 32 <= byte <= 126 or byte in (9, 10, 13)
                    )
                    if filtered_content.strip():  # Asegurarse de que no esté vacío
                        self.terminal_frame.clipboard_clear()  # Limpiar el portapapeles
                        self.terminal_frame.clipboard_append(filtered_content)  # Copiar el contenido filtrado
                        self.terminal_frame.update()  # Actualizar el portapapeles
                        print(f"Contenido del nodo ColorConvert copiado al portapapeles desde: {self.colorconvert_log_file}")
                    else:
                        print("El archivo de logs contiene solo caracteres no imprimibles.")
                except Exception as e:
                    print(f"Error al procesar el archivo de logs: {e}")
        else:
            print("No se encontró el archivo de logs o no está definido.")

    def stop_colorconvert_node(self):
        """Detiene el nodo ColorConvert y cierra la terminal embebida."""
        if self.colorconvert_process:
            try:
                os.killpg(os.getpgid(self.colorconvert_process.pid), signal.SIGINT)
                self.colorconvert_process.wait()
                
                print("ColorConvert node stopped.")
            except ProcessLookupError:
                print("No active process to stop.")
            self.colorconvert_process = None

class YOLOOptions(NodeOptions):
    """ Opciones específicas para el nodo YOLO."""
    def __init__(self):
        super().__init__()
        self.selected_model = tk.StringVar(value="COCO")  # Modelo seleccionado
        self.selected_model_name = tk.StringVar(value="yolov8n-seg.pt")  # Nombre del modelo YOLO
        self.selected_classes = []  # Lista de clases seleccionadas
        self.select_all_classes = tk.BooleanVar(value=False)  # Opción "Todos"
        self.available_models = ["COCO", "Custom"]  # Lista de modelos disponibles
        self.coco_classes = {
            0: "person", 1: "bicycle", 2: "car", 3: "motorcycle", 4: "airplane", 5: "bus", 6: "train",
            7: "truck", 8: "boat", 9: "traffic light", 10: "fire hydrant", 11: "stop sign", 12: "parking meter",
            13: "bench", 14: "bird", 15: "cat", 16: "dog", 17: "horse", 18: "sheep", 19: "cow", 20: "elephant",
            21: "bear", 22: "zebra", 23: "giraffe", 24: "backpack", 25: "umbrella", 26: "handbag", 27: "tie",
            28: "suitcase", 29: "frisbee", 30: "skis", 31: "snowboard", 32: "sports ball", 33: "kite",
            34: "baseball bat", 35: "baseball glove", 36: "skateboard", 37: "surfboard", 38: "tennis racket",
            39: "bottle", 40: "wine glass", 41: "cup", 42: "fork", 43: "knife", 44: "spoon", 45: "bowl",
            46: "banana", 47: "apple", 48: "sandwich", 49: "orange", 50: "broccoli", 51: "carrot", 52: "hot dog",
            53: "pizza", 54: "donut", 55: "cake", 56: "chair", 57: "couch", 58: "potted plant", 59: "bed",
            60: "dining table", 61: "toilet", 62: "tv", 63: "laptop", 64: "mouse", 65: "remote", 66: "keyboard",
            67: "cell phone", 68: "microwave", 69: "oven", 70: "toaster", 71: "sink", 72: "refrigerator", 73: "book",
            74: "clock", 75: "vase", 76: "scissors", 77: "teddy bear", 78: "hair drier", 79: "toothbrush"
        }

    def create_widgets(self, parent):
        # Etiqueta para seleccionar el modelo
        ttk.Label(parent, text="Select YOLO Model", font=("Arial", 12)).pack(anchor="center", pady=5)

        # Combobox para seleccionar el modelo
        model_combobox = ttk.Combobox(
            parent,
            textvariable=self.selected_model,
            values=self.available_models,
            state="readonly",
            width=20
        )
        model_combobox.pack(anchor="center", pady=10)
        model_combobox.bind("<<ComboboxSelected>>", self.on_model_selected)

        # Checkbox para seleccionar todas las clases
        ttk.Checkbutton(
            parent,
            text="Select All Classes",
            variable=self.select_all_classes,
            command=self.toggle_select_all_classes
        ).pack(anchor="center", pady=5)

        # Listbox con scrollbar para seleccionar múltiples clases
        self.class_listbox = tk.Listbox(parent, selectmode="multiple", height=15)
        for idx, name in self.coco_classes.items():
            self.class_listbox.insert("end", f"{idx}: {name}")
        self.class_listbox.pack(anchor="center", fill="x", padx=10, pady=5)

    def toggle_select_all_classes(self):
        """Activa o desactiva la selección de todas las clases."""
        if self.select_all_classes.get():
            # Marca todas las clases en el Listbox
            self.class_listbox.select_set(0, tk.END)
        else:
            # Desmarca todas las clases en el Listbox
            self.class_listbox.selection_clear(0, tk.END)

    def on_model_selected(self, event):
        """Callback al seleccionar un modelo."""
        model = self.selected_model.get()
        if model == "COCO":
            self.selected_model_name.set("yolov8n-seg.pt")
            self.update_class_listbox(self.coco_classes)
        elif model == "Custom":
            self.selected_model_name.set("custom_model_name.pt")
            custom_classes = {0: "custom_class_1", 1: "custom_class_2", 2: "custom_class_3"}  # Ejemplo
            self.update_class_listbox(custom_classes)
        else:
            self.selected_model_name.set("None")
            self.update_class_listbox({})
        print(f"Selected YOLO model: {model}, Model Name: {self.selected_model_name.get()}")

    def update_class_listbox(self, classes):
        """Actualiza las opciones del class_listbox según el modelo seleccionado."""
        self.class_listbox.delete(0, tk.END)  # Vaciar la lista existente
        for idx, name in classes.items():
            self.class_listbox.insert("end", f"{idx}: {name}")

    def get_selected_classes(self):
        """Obtiene las clases seleccionadas como una lista de índices."""
        if self.select_all_classes.get():
            return list(self.coco_classes.keys())  # Retorna todas las clases
        selected_indices = self.class_listbox.curselection()
        self.selected_classes = [int(self.class_listbox.get(i).split(":")[0]) for i in selected_indices]
        return self.selected_classes

class CalculationOptions(NodeOptions):
    """Opciones específicas para el nodo Temperature and CSWI."""
    def __init__(self, yolo_options):
        super().__init__()
        self.yolo_options = yolo_options  # Referencia al nodo Ultralytics

    def create_widgets(self, parent):
        ttk.Label(parent, text="No specific options required", font=("Arial", 12)).pack(anchor="center", pady=5)


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
        self.notebook.add(self.main_tab, text="Launch ros2 nodes")

        # Widgets
        self.create_main_tab_widgets()

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
