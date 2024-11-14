import subprocess
import os

def start_rosbag_recording(topics, base_output_path):
    # Crear una lista de procesos
    processes = []

    for i, topic in enumerate(topics):
        # Generar un nombre único para cada rosbag usando el nombre del topic o un índice
        output_path = os.path.join(base_output_path, f"{topic.replace('/', '_')}")

        # Crear el comando para grabar cada topic en una carpeta separada
        command = [
            'ros2', 'bag', 'record',
            topic,
            '-o', output_path
        ]
        
        # Iniciar el proceso y agregarlo a la lista
        process = subprocess.Popen(command)
        processes.append(process)
        print(f"Started recording topic: {topic} to {output_path}")

    try:
        # Esperar a que terminen todos los procesos
        for process in processes:
            process.wait()
    except KeyboardInterrupt:
        # Terminar todos los procesos si se recibe una interrupción de teclado
        for process in processes:
            process.terminate()
        print("Recording stopped for all topics.")

if __name__ == '__main__':
    # Definir los topics que quieres grabar
    topics = ['/camera/camera/color/image_raw', 
              '/Temperature_and_CSWI/masked_image_with_temperature',
              '/Temperature_and_CSWI/rescaled_rgb',
              '/Temperature_and_CSWI/rescaled_yolo_masks',
              '/camera/camera/depth/image_rect_raw',
              '/thermal_image',
              '/thermal_image_view',
              '/yolo_image'
              ]
    # Ruta base de salida para guardar las carpetas de archivos rosbag
    base_output_path = 'src/ProvesDeCamp/Rosbags'

    # Iniciar la grabación
    start_rosbag_recording(topics, base_output_path)
