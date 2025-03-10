import tkinter as tk
from tkinter import ttk
import subprocess
import os
import signal

class ROS2RealsenseLauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Realsense Launcher")
        self.root.geometry("1000x800")
        root.tk.call("source", "custom_nodes/launch/azure.tcl")
        root.tk.call("set_theme", "light")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Parameters
        self.init_parameters()

        # Create Notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Tabs
        self.main_tab = ttk.Frame(self.notebook)
        self.extra_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.main_tab, text="Launch ros2 nodes")
        self.notebook.add(self.extra_tab, text="Visualize topics")

        # Widgets
        self.create_main_tab_widgets()
        self.create_extra_tab_widgets()

    def init_parameters(self):
        self.enable_color = tk.BooleanVar(value=True)
        self.enable_depth = tk.BooleanVar(value=False)
        self.enable_infra = tk.BooleanVar(value=False)
        self.enable_infra1 = tk.BooleanVar(value=False)
        self.enable_infra2 = tk.BooleanVar(value=False)
        self.align_depth = tk.BooleanVar(value=False)
        self.pointcloud = tk.BooleanVar(value=False)
        self.rgb_resolution = tk.StringVar(value="1280x720x30")
        self.depth_resolution = tk.StringVar(value="640x480x30")
        self.terminal_process = None
        self.terminal_log_file = "terminal_log.txt"

        # Extra widget references
        self.extra_rgb = None
        self.extra_depth = None
        self.extra_infra = None

    def create_main_tab_widgets(self):
        self.terminal_frame = tk.Frame(self.main_tab, width=450, height=300, bg="black")
        self.terminal_frame.pack(pady=20)

        self.create_buttons(self.main_tab)
        self.create_checkboxes(self.main_tab)

    def create_extra_tab_widgets(self):
        # Example: Add advanced settings or logs in the extra tab
        ttk.Label(self.extra_tab, text="Extra settings coming soon!", font=("Arial", 12)).pack(pady=20)

    def create_buttons(self, parent):
        button_frame = ttk.Frame(parent)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Launch Realsense", style="Accent.TButton",
                   command=self.launch_realsense_node).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Stop Realsense", command=self.stop_realsense).pack(side="left", padx=5)

        ttk.Button(parent, text="Copy shell", command=self.copy_terminal_output).pack(pady=10)

    def create_checkboxes(self, parent):
        ttk.Checkbutton(parent, text="Enable RGB", variable=self.enable_color, command=self.toggle_rgb_options,
                        style="Switch.TCheckbutton").pack()
        ttk.Checkbutton(parent, text="Enable Depth", variable=self.enable_depth, command=self.toggle_depth_options,
                        style="Switch.TCheckbutton").pack()
        ttk.Checkbutton(parent, text="Enable Infra", variable=self.enable_infra, command=self.toggle_infra_options,
                        style="Switch.TCheckbutton").pack()

        if self.enable_color.get():
            self.create_extra_rgb(parent)

    def create_extra_rgb(self, parent):
        if not self.extra_rgb:
            frame = ttk.Frame(parent)
            frame.pack(pady=5)
            ttk.Label(frame, text="RGB resolution").pack(side="left")
            menu = ttk.Combobox(frame, textvariable=self.rgb_resolution,
                                values=["1280x720x30", "640x480x30", "640x480x15"],width=13)
            menu.pack(side="left")
            self.extra_rgb = frame

    def destroy_extra_rgb(self):
        if self.extra_rgb:
            self.extra_rgb.destroy()
            self.extra_rgb = None

    def create_extra_depth(self, parent):
        if not self.extra_depth:
            frame = ttk.Frame(parent)
            frame.pack(pady=5)
            ttk.Label(frame, text="Depth resolution").pack(side="left")
            ttk.Combobox(frame, textvariable=self.depth_resolution,
                         values=["640x480x30", "848x480x30", "1280x720x30"],width=13).pack(side='left')
            ttk.Checkbutton(frame, text="Align depth", variable=self.align_depth).pack(side='left')
            ttk.Checkbutton(frame, text="Pointcloud", variable=self.pointcloud).pack(side='left')
            self.extra_depth = frame

    def destroy_extra_depth(self):
        if self.extra_depth:
            self.extra_depth.destroy()
            self.extra_depth = None

    def create_extra_infra(self, parent):
        if not self.extra_infra:
            frame = ttk.Frame(parent)
            frame.pack(pady=5)
            ttk.Label(frame, text="Depth resolution").pack(side="left")
            ttk.Combobox(frame, textvariable=self.depth_resolution,
                         values=["640x480x30", "848x480x30", "1280x720x30"],width=13).pack(side='left')
            ttk.Checkbutton(frame, text="infra 1", variable=self.enable_infra1).pack(side='left')
            ttk.Checkbutton(frame, text="infra 2", variable=self.enable_infra2).pack(side='left')
            self.extra_infra = frame

    def destroy_extra_infra(self):
        if self.extra_infra:
            self.extra_infra.destroy()
            self.extra_infra = None

    def toggle_rgb_options(self):
        if self.enable_color.get():
            self.create_extra_rgb(self.main_tab)
        else:
            self.destroy_extra_rgb()

    def toggle_depth_options(self):
        if self.enable_depth.get():
            self.create_extra_depth(self.main_tab)
        else:
            self.destroy_extra_depth()

    def toggle_infra_options(self):
        if self.enable_infra.get():
            self.create_extra_infra(self.main_tab)
        else:
            self.destroy_extra_infra()

    def launch_realsense_node(self):
        if self.terminal_process and self.terminal_process.poll() is None:
            self.stop_realsense()

        launch_command = (
            f"ros2 launch custom_nodes main_launch2.py "
            f"enable_color:={str(self.enable_color.get()).lower()} "
            f"enable_depth:={str(self.enable_depth.get()).lower()} "
            f"enable_infra1:={str(self.enable_infra1.get()).lower()} "
            f"enable_infra2:={str(self.enable_infra2.get()).lower()} "
            f"align_depth:={str(self.align_depth.get()).lower()} "
            f"pointcloud:={str(self.pointcloud.get()).lower()} "
            f"rgb_resolution:={self.rgb_resolution.get()} "
            f"depth_resolution:={self.depth_resolution.get()}"
        )

        xterm_command = (
        "xterm -geometry 82x30 "
        f"-into {self.terminal_frame.winfo_id()} "  # Embebe en el frame de Tkinter
        "-fa Monospace -fs 6 -sb -rightbar "
        f"-e bash -c '{launch_command}'"  # Ejecuta el comando dentro del terminal
        )

        self.terminal_process = subprocess.Popen(xterm_command, shell=True, preexec_fn=os.setsid)

    def stop_realsense(self):
        if self.terminal_process:
            try:
                if self.terminal_process.poll() is None:
                    os.killpg(os.getpgid(self.terminal_process.pid), signal.SIGINT)
                    self.terminal_process.wait()
                else:
                    print("The Realsense process has already stopped.")
            except ProcessLookupError:
                print("The process does not exist or has already been terminated.")
            self.terminal_process = None
        else:
            print("No Realsense process found.")

    def on_closing(self):
        self.stop_realsense()
        self.root.quit()
        self.root.destroy()
        os._exit(0)


    def copy_terminal_output(self):
        if os.path.exists(self.terminal_log_file):
            with open(self.terminal_log_file, 'r') as log_file:
                self.root.clipboard_clear()
                self.root.clipboard_append(log_file.read())
                self.root.update()

root = tk.Tk()
app = ROS2RealsenseLauncherApp(root)
root.mainloop()
