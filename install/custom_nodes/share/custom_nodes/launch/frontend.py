import tkinter as tk
from tkinter import ttk
import subprocess
import os
import signal

class ROS2RealsenseLauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Realsense Launcher")
        
        # Ajustar el tamaño de la ventana principal a un rectángulo más alto que ancho
        self.root.geometry("500x800")

        # Frame para la terminal embebida con tamaño fijo
        self.terminal_frame = tk.Frame(root, width=450, height=400, bg='black')
        self.terminal_frame.pack(pady=20)

        # Variables para guardar los valores de los parámetros
        self.enable_color = tk.BooleanVar(value=True)  # Por defecto RGB habilitado
        self.enable_depth = tk.BooleanVar(value=False)  # Default: Depth disabled
        self.enable_infra = tk.BooleanVar(value=False)  # Habilitar Infra general
        self.enable_infra1 = tk.BooleanVar(value=False)  # Default: Infra1 disabled
        self.enable_infra2 = tk.BooleanVar(value=False)  # Default: Infra2 disabled
        self.align_depth = tk.BooleanVar(value=False)
        self.pointcloud = tk.BooleanVar(value=False)
        self.rgbd_resolution = tk.StringVar(value="1280x720x30")
        self.depth_resolution = tk.StringVar(value="640x480x30")

        # Botón para iniciar el nodo
        self.start_button = tk.Button(root, text="Iniciar Realsense", command=self.start_realsense)
        self.start_button.pack(pady=10)

        # Botón para detener el nodo
        self.stop_button = tk.Button(root, text="Detener Realsense", command=self.stop_realsense)
        self.stop_button.pack(pady=10)

        # Botón para copiar y pegar el contenido de la terminal
        self.copy_button = tk.Button(root, text="Copiar Terminal", command=self.copy_terminal_output)
        self.copy_button.pack(pady=10)

        # Casilla de verificación general para habilitar RGB
        self.enable_color_check = tk.Checkbutton(root, text="Enable RGB", variable=self.enable_color, command=self.toggle_rgb_options)
        self.enable_color_check.pack()

        # Casilla de verificación general para habilitar Depth
        self.enable_depth_check = tk.Checkbutton(root, text="Enable Depth", variable=self.enable_depth, command=self.toggle_depth_options)
        self.enable_depth_check.pack()

        # Casilla de verificación general para habilitar Infra
        self.enable_infra_check = tk.Checkbutton(root, text="Enable Infra", variable=self.enable_infra, command=self.toggle_infra_options)
        self.enable_infra_check.pack()

        # Menú desplegable para la resolución RGBD
        self.resolution_label = tk.Label(root, text="Selecciona resolución RGBD:")
        self.resolution_label.pack()
        self.resolution_menu = ttk.Combobox(root, textvariable=self.rgbd_resolution, 
                                             values=["1280x720x30", "640x480x30", "640x480x15"])
        self.resolution_menu.pack()

        # Menú desplegable para la resolución de Depth
        self.depth_resolution_label = tk.Label(root, text="Selecciona resolución de Depth:")
        self.depth_resolution_menu = ttk.Combobox(root, textvariable=self.depth_resolution, 
                                                   values=["640x480x30", "848x480x30", "1280x720x30"])

        # Opción de alinear Depth
        self.align_depth_check = tk.Checkbutton(root, text="Align Depth", variable=self.align_depth)
        
        # Opción de Pointcloud
        self.pointcloud_check = tk.Checkbutton(root, text="Enable Pointcloud", variable=self.pointcloud)

        # Casillas de verificación para parámetros específicos de Infra
        self.enable_infra1_check = tk.Checkbutton(root, text="Enable Infra1", variable=self.enable_infra1)
        self.enable_infra2_check = tk.Checkbutton(root, text="Enable Infra2", variable=self.enable_infra2)

        # Inicializamos las opciones por defecto
        self.toggle_rgb_options()
        self.toggle_depth_options()
        self.toggle_infra_options()

        # Proceso de la terminal embebida
        self.terminal_process = None
        self.terminal_log_file = "/tmp/xterm_output.log"  # Archivo temporal para almacenar la salida de xterm

    def toggle_rgb_options(self):
        """Activa/desactiva las opciones de resolución de RGB según Enable RGB"""
        if self.enable_color.get():
            # Mostrar siempre la selección de resolución RGBD como la primera opción
            self.resolution_label.pack_forget()
            self.resolution_menu.pack_forget()
            self.resolution_label.pack()
            self.resolution_menu.pack()
        else:
            # Ocultar resolución RGBD si RGB está deshabilitado
            self.resolution_label.pack_forget()
            self.resolution_menu.pack_forget()

        # Asegurarse de actualizar las demás opciones
        self.toggle_depth_options()

    def toggle_depth_options(self):
        """Activa o desactiva las opciones de Depth, alineación y pointcloud según Enable Depth"""
        # Primero aseguramos que la resolución de Depth siempre sea la primera visible
        self.repack_widgets()

        if self.enable_depth.get():
            # Mostrar opciones específicas de Depth
            self.align_depth_check.pack()
            self.pointcloud_check.pack()
        else:
            # Ocultar opciones específicas de Depth
            self.align_depth_check.pack_forget()
            self.pointcloud_check.pack_forget()

    def toggle_infra_options(self):
        """Activa o desactiva las opciones de Infra1, Infra2 y la resolución de Depth según Enable Infra"""
        # Primero aseguramos que la resolución de Depth siempre sea la primera visible
        self.repack_widgets()

        if self.enable_infra.get():
            # Mostrar las opciones Infra1 e Infra2
            self.enable_infra1_check.pack()
            self.enable_infra2_check.pack()
        else:
            # Ocultar Infra1 e Infra2 si Infra está deshabilitado
            self.enable_infra1.set(False)
            self.enable_infra2.set(False)
            self.enable_infra1_check.pack_forget()
            self.enable_infra2_check.pack_forget()

    def repack_widgets(self):
        """Reorganiza todos los widgets relacionados en el orden correcto"""
        # Eliminar todos los widgets dependientes de Infra y Depth
        self.depth_resolution_label.pack_forget()
        self.depth_resolution_menu.pack_forget()
        self.enable_infra1_check.pack_forget()
        self.enable_infra2_check.pack_forget()
        self.align_depth_check.pack_forget()
        self.pointcloud_check.pack_forget()

        # Reempaquetar en el orden correcto
        if self.enable_color.get():
            # Si RGB está habilitado, primero va la resolución RGB
            self.resolution_label.pack()
            self.resolution_menu.pack()

        if self.enable_depth.get() or self.enable_infra.get():
            # Luego siempre la resolución de Depth
            self.depth_resolution_label.pack()
            self.depth_resolution_menu.pack()

        if self.enable_depth.get():
            # Luego las opciones específicas de Depth
            self.align_depth_check.pack()
            self.pointcloud_check.pack()

        if self.enable_infra.get():
            # Luego las opciones de Infra
            self.enable_infra1_check.pack()
            self.enable_infra2_check.pack()

    def start_realsense(self):
        """Lanza el nodo de Realsense en una terminal embebida"""
        # Comando para lanzar realsense
        launch_command = (
            f"ros2 launch custom_nodes main_launch2.py "
            f"enable_color:={str(self.enable_color.get()).lower()} "
            f"enable_depth:={str(self.enable_depth.get()).lower()} "
            f"enable_infra1:={str(self.enable_infra1.get()).lower()} "
            f"enable_infra2:={str(self.enable_infra2.get()).lower()} "
            f"align_depth:={str(self.align_depth.get()).lower()} "
            f"pointcloud:={str(self.pointcloud.get()).lower()} "
            f"rgb_resolution:={self.rgbd_resolution.get()} "
            f"depth_resolution:={self.depth_resolution.get()}"
        )

        # Coordenadas para colocar la terminal dentro del Frame
        x, y = self.terminal_frame.winfo_rootx(), self.terminal_frame.winfo_rooty()

        # Lanzar xterm embebido con redirección de salida a un archivo
        self.terminal_process = subprocess.Popen([
            "xterm", "-geometry", "82x40", "-into", str(self.terminal_frame.winfo_id()), 
            "-fa", "Monospace", "-fs", "6", "-sb", "-rightbar", "-e", f"{launch_command} | tee {self.terminal_log_file}"
        ], preexec_fn=os.setsid)

        print(f"Terminal embebida lanzada con PID: {self.terminal_process.pid}")

    def stop_realsense(self):
        """Detiene el nodo de Realsense enviando un SIGINT (Ctrl+C)"""
        if self.terminal_process:
            print(f"Enviando SIGINT a PID {self.terminal_process.pid}")
            os.killpg(os.getpgid(self.terminal_process.pid), signal.SIGINT)  # Enviar SIGINT (Ctrl+C) al grupo de procesos
            self.terminal_process.wait()  # Esperar a que el proceso termine correctamente
            print("SIGINT enviado y proceso detenido.")
        else:
            print("No se encontró el proceso de Realsense.")

    def copy_terminal_output(self):
        """Copia el contenido de la terminal al portapapeles"""
        if os.path.exists(self.terminal_log_file):
            with open(self.terminal_log_file, 'r') as log_file:
                terminal_content = log_file.read()
                # Copiar al portapapeles
                self.root.clipboard_clear()
                self.root.clipboard_append(terminal_content)
                self.root.update()  # Actualizar el portapapeles
                print("Contenido de la terminal copiado al portapapeles.")
        else:
            print("No se encontró el archivo de salida de la terminal.")

# Crear la ventana de Tkinter
root = tk.Tk()

# Crear la aplicación
app = ROS2RealsenseLauncherApp(root)

# Iniciar la interfaz gráfica
root.mainloop()
