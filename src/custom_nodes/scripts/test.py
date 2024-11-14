from ultralytics import YOLO

# Cargar el modelo personalizado
model = YOLO('/home/yeray/sensors_ws/install/ultralytics_ros/share/ultralytics_ros/models/lettuce.pt')

# Obtener las clases del modelo
class_names = model.names  # Esto devuelve un diccionario con class_id como claves y nombres de clase como valores
print(class_names)