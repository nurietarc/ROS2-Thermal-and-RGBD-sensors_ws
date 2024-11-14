cmake_minimum_required(VERSION 3.8)
project(custom_nodes)

find_package(ament_cmake REQUIRED)

# Instala los archivos de lanzamiento
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

# Instala los scripts (si los tienes en la carpeta `scripts`)
install(DIRECTORY scripts/
  DESTINATION share/${PROJECT_NAME}/scripts
)

ament_package()

