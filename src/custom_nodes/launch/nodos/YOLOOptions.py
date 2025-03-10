from .NodeOptions import NodeOptions
import tkinter as tk
from tkinter import ttk

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

