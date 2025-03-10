from .NodeOptions import NodeOptions
import tkinter as tk
from tkinter import ttk

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