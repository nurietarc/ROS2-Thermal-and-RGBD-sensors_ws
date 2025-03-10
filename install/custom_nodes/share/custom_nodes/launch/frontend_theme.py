import tkinter as tk
from tkinter import ttk
import subprocess
import os
import signal
import cv2
import threading
from PIL import Image, ImageTk
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image as ROSImage
from cv_bridge import CvBridge

class ROS2RealsenseLauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Realsense Launcher")
        
        # Adjust the main window size
        self.root.geometry("1000x800")  # Increased height for additional widgets

        # Load the Azure theme
        root.tk.call("source", "custom_nodes/launch/azure.tcl")
        root.tk.call("set_theme", "light")

        # Protocol
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.show_topic = tk.BooleanVar(value=True)  # Por defecto, el tópico se muestra
        self.real_width = None  # Ancho real del tópico
        self.real_height = None  # Alto real del tópico
        self.current_canvas_width = None
        self.current_canvas_height = None

        # Variables for parameters
        self.enable_color = tk.BooleanVar(value=True)
        self.enable_depth = tk.BooleanVar(value=False)
        self.enable_infra = tk.BooleanVar(value=False)
        self.enable_infra1 = tk.BooleanVar(value=False)
        self.enable_infra2 = tk.BooleanVar(value=False)
        self.align_depth = tk.BooleanVar(value=False)
        self.pointcloud = tk.BooleanVar(value=False)
        self.rgbd_resolution = tk.StringVar(value="1280x720x30")
        self.rgbd_resolution.trace("w", lambda *args: self.update_image_frame())
        self.depth_resolution = tk.StringVar(value="640x480x30")

        # Image display
        self.image_frame = tk.Frame(root, bg='white')
        self.image_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        self.canvas = tk.Canvas(self.image_frame, bg='black')
        self.canvas.pack()

        # Frame for the embedded terminal
        self.terminal_frame = tk.Frame(root, width=450, height=200, bg='black')
        self.terminal_frame.pack(pady=20)

        # Frame for buttons
        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(pady=10)

        # Buttons
        self.start_button = ttk.Button(self.button_frame, text="Launch Realsense", style="Accent.TButton", command=self.start_realsense)
        self.start_button.pack(side="left", padx=5)

        self.stop_button = ttk.Button(self.button_frame, text="Stop Realsense", command=self.stop_realsense)
        self.stop_button.pack(side="left", padx=5)

        self.copy_button = ttk.Button(root, text="Copy shell", command=self.copy_terminal_output)
        self.copy_button.pack(pady=10)

        # General checkboxes for options
        self.enable_color_check = ttk.Checkbutton(root, text="Enable RGB", variable=self.enable_color, command=self.toggle_rgb_options, style='Switch.TCheckbutton')
        self.enable_color_check.pack()

        self.enable_depth_check = ttk.Checkbutton(root, text="Enable Depth", variable=self.enable_depth, command=self.toggle_depth_options, style='Switch.TCheckbutton')
        self.enable_depth_check.pack()

        self.enable_infra_check = ttk.Checkbutton(root, text="Enable Infra", variable=self.enable_infra, command=self.toggle_infra_options, style='Switch.TCheckbutton')
        self.enable_infra_check.pack()

        # Dropdown menus for resolutions
        self.rgb_label = ttk.Label(root, text="RGB Resolution")
        self.rgb_label.pack()
        self.rgb_menu = ttk.Combobox(root, textvariable=self.rgbd_resolution, values=["1280x720x30", "640x480x30", "640x480x15"])
        self.rgb_menu.bind("<<ComboboxSelected>>", lambda event: self.update_image_frame())
        self.rgb_menu.pack()

        self.depth_label = ttk.Label(root, text="Depth Resolution")
        self.depth_label.pack()
        self.depth_menu = ttk.Combobox(root, textvariable=self.depth_resolution, values=["640x480x30", "848x480x30", "1280x720x30"])
        self.depth_menu.pack()

        self.align_depth_check = ttk.Checkbutton(root, text="Align Depth", variable=self.align_depth)
        self.pointcloud_check = 

        self.enable_infra1_check = ttk.Checkbutton(root, text="Enable Infra1", variable=self.enable_infra1)
        self.enable_infra2_check = ttk.Checkbutton(root, text="Enable Infra2", variable=self.enable_infra2)

        self.show_topic_check = ttk.Checkbutton(
        root, 
        text="Show Topic", 
        variable=self.show_topic, 
        command=self.toggle_topic_display, 
        style='Switch.TCheckbutton'
        )


        # Initialize options
        self.toggle_rgb_options()
        self.toggle_depth_options()
        self.toggle_infra_options()

        # Embedded terminal process
        self.terminal_process = None
        self.terminal_log_file = "/tmp/xterm_output.log"

        # ROS2 threading
        self.ros_thread = None
        self.stop_ros_thread = False

        # Initialize the image frame with the default resolution
        self.update_image_frame()

    def toggle_rgb_options(self):
        """Enable/disable RGB resolution options"""
        if self.enable_color.get():
            self.rgb_label.pack()
            self.rgb_menu.pack()
            self.show_topic_check.pack()  # Mostrar el Checkbutton si RGB está activado
        else:
            self.rgb_label.pack_forget()
            self.rgb_menu.pack_forget()
            self.show_topic_check.pack_forget()  # Ocultar el Checkbutton si RGB está desactivado


    def toggle_depth_options(self):
        """Enable/disable Depth resolution options"""
        if self.enable_depth.get():
            self.depth_label.pack()
            self.depth_menu.pack()
            self.align_depth_check.pack()
            self.pointcloud_check.pack()
        else:
            self.depth_label.pack_forget()
            self.depth_menu.pack_forget()
            self.align_depth_check.pack_forget()
            self.pointcloud_check.pack_forget()

    def toggle_infra_options(self):
        """Enable/disable Infra-specific options"""
        if self.enable_infra.get():
            self.depth_label.pack()
            self.depth_menu.pack()
            self.enable_infra1_check.pack()
            self.enable_infra2_check.pack()
        else:
            self.depth_label.pack_forget()
            self.depth_menu.pack_forget()
            self.enable_infra1.set(False)
            self.enable_infra2.set(False)
            self.enable_infra1_check.pack_forget()
            self.enable_infra2_check.pack_forget()

    def update_image_frame(self):
        """Update the size of the image frame and canvas based on the selected RGB resolution."""
        width, height, _ = map(int, self.rgbd_resolution.get().split('x'))
        aspect_ratio = width / height

        # Define a reasonable maximum width for the display
        max_display_width = 450
        display_width = max_display_width
        display_height = int(display_width / aspect_ratio)

        # Update the frame and canvas dimensions
        self.image_frame.config(width=display_width, height=display_height)
        self.canvas.config(width=display_width, height=display_height)

    def start_realsense(self):
        """Launch the Realsense node in an embedded terminal"""
        self.update_image_frame()
        
        if self.terminal_process and self.terminal_process.poll() is None:
            print("A Realsense process is already running. Stopping it before starting a new one.")
            self.stop_realsense()

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

        self.terminal_process = subprocess.Popen([
            "xterm", "-geometry", "82x20", "-into", str(self.terminal_frame.winfo_id()), 
            "-fa", "Monospace", "-fs", "6", "-sb", "-rightbar", "-e", f"{launch_command} | tee {self.terminal_log_file}"
        ], preexec_fn=os.setsid)

        print(f"Embedded shell launched with PID: {self.terminal_process.pid}")

        # Start the ROS2 thread to receive and display images
        self.stop_ros_thread = False
        self.ros_thread = threading.Thread(target=self.start_ros_image_listener)
        self.ros_thread.start()

    def stop_realsense(self):
        """Stops the Realsense node"""
        if self.terminal_process:
            try:
                if self.terminal_process.poll() is None:
                    print(f"Sending Ctrl+C to shell {self.terminal_process.pid}")
                    os.killpg(os.getpgid(self.terminal_process.pid), signal.SIGINT)
                    self.terminal_process.wait()
                    print("Ctrl+C sent and process stopped.")
                else:
                    print("The Realsense process has already stopped.")
            except ProcessLookupError:
                print("The process does not exist or has already been terminated.")
        else:
            print("No Realsense process found.")

        # Stop the ROS2 thread
        self.stop_ros_thread = True
        if self.ros_thread:
            self.ros_thread.join()

    def on_closing(self):
        """Forcefully close the application when the window is closed."""
        print("Closing application...")

        # Stop the Realsense process if it is running
        self.stop_realsense()

        # Ensure the ROS2 thread is terminated
        if self.ros_thread and self.ros_thread.is_alive():
            print("Stopping ROS thread...")
            self.stop_ros_thread = True  # Signal the thread to stop
            self.ros_thread.join(timeout=2)  # Wait for the thread to stop
            if self.ros_thread.is_alive():
                print("ROS thread did not terminate. Forcing exit.")
            else:
                print("ROS thread stopped.")

        # Exit the Tkinter main loop and destroy the window
        self.root.quit()  # Stop the Tkinter main loop
        self.root.destroy()  # Destroy the Tkinter window

        # Ensure Python exits completely
        print("Force exiting application.")
        os._exit(0)  # Ensures all processes are terminated

    def copy_terminal_output(self):
        """Copies the terminal content to the clipboard"""
        if os.path.exists(self.terminal_log_file):
            with open(self.terminal_log_file, 'r') as log_file:
                terminal_content = log_file.read()
                self.root.clipboard_clear()
                self.root.clipboard_append(terminal_content)
                self.root.update()
                print("Terminal content copied to clipboard.")
        else:
            print("Terminal output file not found.")

    def start_ros_image_listener(self):
        """Starts a ROS2 node to listen to image topics and display them."""
        rclpy.init()
        node = Node('image_listener')
        bridge = CvBridge()

        def image_callback(msg):
            """Callback to process and display images from the ROS topic."""
            if not self.show_topic.get():
                return  # No hace nada si el tópico está oculto

            cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
            actual_width, actual_height = cv_image.shape[1], cv_image.shape[0]

            # Almacena las dimensiones reales solo si cambian
            if self.real_width != actual_width or self.real_height != actual_height:
                self.real_width = actual_width
                self.real_height = actual_height
                self.update_image_frame(width=actual_width, height=actual_height)

            # Ajusta la imagen para que se adapte al canvas
            display_width = self.canvas.winfo_width()
            display_height = self.canvas.winfo_height()
            cv_image = cv2.resize(cv_image, (display_width, display_height))

            # Convertir a formato PIL para Tkinter
            image = Image.fromarray(cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB))
            photo = ImageTk.PhotoImage(image=image)

            # Mostrar la imagen en el Canvas
            self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
            self.canvas.image = photo  # Mantén una referencia para evitar recolección de basura


        subscription = node.create_subscription(ROSImage, '/camera/camera/color/image_raw', image_callback, 10)

        while not self.stop_ros_thread:
            rclpy.spin_once(node, timeout_sec=0.1)  # Timeout to allow interruption

        print("ROS listener thread stopping...")
        node.destroy_node()
        rclpy.shutdown()
        print("ROS listener thread stopped.")

    def update_image_frame(self, width=None, height=None):
        """
        Update the size of the image frame and canvas based on the real image dimensions 
        or the selected RGB resolution.
        """
        if not hasattr(self, 'canvas') or not isinstance(self.canvas, tk.Canvas):
            print("Canvas does not exist, skipping update.")
            return

        # Usa las dimensiones reales si están disponibles
        if width is None or height is None:
            if self.real_width and self.real_height:
                width, height = self.real_width, self.real_height
            else:
                width, height, _ = map(int, self.rgbd_resolution.get().split('x'))

        aspect_ratio = width / height

        # Define un ancho máximo razonable
        max_display_width = 450
        display_width = max_display_width
        display_height = int(display_width / aspect_ratio)

        # Verifica si las dimensiones ya son correctas
        if (self.current_canvas_width == display_width and 
                self.current_canvas_height == display_height):
            print("Canvas size is already correct, skipping update.")
            return

        # Actualiza las dimensiones del frame y del canvas
        self.image_frame.config(width=display_width, height=display_height)
        self.canvas.config(width=display_width, height=display_height)

        # Guarda las dimensiones actuales
        self.current_canvas_width = display_width
        self.current_canvas_height = display_height

        print(f"Canvas updated to: {display_width}x{display_height} (Aspect Ratio: {aspect_ratio:.2f})")

    def toggle_topic_display(self):
        """Toggle the display of the ROS topic."""
        if self.show_topic.get():  # Mostrar el tópico si está activado
            # Usa las dimensiones reales si están disponibles, o un aspecto por defecto
            max_display_width = 450  # Ancho máximo para la columna derecha
            if self.real_width and self.real_height:
                aspect_ratio = self.real_width / self.real_height
            else:
                aspect_ratio = 16 / 9  # Aspecto por defecto si no se sabe
            
            display_width = max_display_width
            display_height = int(display_width / aspect_ratio)

            # Recrea el Canvas con las dimensiones calculadas
            self.canvas = tk.Canvas(self.image_frame, bg='black', width=display_width, height=display_height)
            self.canvas.pack()
            print(f"Topic display shown with size: {display_width}x{display_height}")
        else:  # Ocultar el tópico
            # Borra todos los widgets dentro del frame
            for widget in self.image_frame.winfo_children():
                widget.destroy()
            print("Topic display hidden.")



# Create the Tkinter window
root = tk.Tk()
app = ROS2RealsenseLauncherApp(root)
root.mainloop()