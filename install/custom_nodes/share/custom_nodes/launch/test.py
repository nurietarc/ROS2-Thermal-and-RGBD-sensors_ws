import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()

# Listar los temas disponibles
print("Temas disponibles:", style.theme_names())

root.mainloop()