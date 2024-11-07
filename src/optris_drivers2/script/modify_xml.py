# Programa mediante el cual se puede modificar un archivo xml para cambiar un parametro 
# utilizado en el, mediante la ejecución de un archivo launch

from lxml import etree
import sys

def modify_focus_in_xml(xml_path, new_focus_value):
    # Parsear el archivo XML con lxml
    parser = etree.XMLParser(remove_blank_text=False)
    tree = etree.parse(xml_path, parser)
    root = tree.getroot()

    # Buscar el elemento <focus> y modificar su valor
    focus_element = root.find('.//focus')
    if focus_element is not None:
        focus_element.text = str(new_focus_value)
        # Guardar los cambios en el archivo con pretty_print para mantener el formato
        tree.write(xml_path, pretty_print=True, xml_declaration=True, encoding="UTF-8")

if __name__ == '__main__':
    xml_file_path = sys.argv[1]
    new_focus_value = sys.argv[2]
    modify_focus_in_xml(xml_file_path, new_focus_value)

# ###############################
# # Version inicial de programa #
# ###############################
# # El problema de esta version es que se modificava completamente el archivo xml (desaparecian muchos comentarios)

# import sys
# import xml.etree.ElementTree as ET

# def modify_focus_in_xml(xml_path, new_focus_value):
#     tree = ET.parse(xml_path)
#     root = tree.getroot()

#     # Buscar el elemento <focus> y modificar su valor
#     for focus in root.iter('focus'):
#         focus.text = str(new_focus_value)

#     # Guardar los cambios en el mismo archivo
#     tree.write(xml_path)

# if __name__ == '__main__':
#     xml_file_path = sys.argv[1]
#     new_focus_value = sys.argv[2]
#     modify_focus_in_xml(xml_file_path, new_focus_value)