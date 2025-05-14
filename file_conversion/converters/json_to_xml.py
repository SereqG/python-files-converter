import xml.etree.ElementTree as ET

def convert_json_to_xml(json_data):
    """
    Converts JSON data (dict or list) to an XML ElementTree.
    """
    xml_root = ET.Element("root")
    build_xml_body(json_data, xml_root)
    return ET.ElementTree(xml_root)

def build_xml_body(data, parent_element):
    """
    Recursively builds XML structure from data into the parent element.
    """
    if isinstance(data, list):
        for item in data:
            child = ET.SubElement(parent_element, "element")
            build_xml_body(item, child)
    elif isinstance(data, dict):
        for key, value in data.items():
            child = ET.SubElement(parent_element, key)
            build_xml_body(value, child)
    else:
        parent_element.text = str(data)
