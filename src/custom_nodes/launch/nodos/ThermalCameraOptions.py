from .NodeOptions import NodeOptions
import tkinter as tk
from tkinter import ttk
import subprocess
import signal
import os


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
