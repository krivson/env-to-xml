import os
import xml.etree.ElementTree as ET


def convert_env_to_xml(env_file_path, output_file_path=None):
    """
    Converts a .env file to an XML format.

    Args:
        env_file_path (str): Path to the .env file.
        output_file_path (str, optional): Path for the output XML file. 
                                          If not provided, the XML file will be created in the same directory as the .env file.
    """
    # Ensure the .env file exists
    if not os.path.exists(env_file_path):
        raise FileNotFoundError(f"The .env file '{env_file_path}' does not exist.")
    
    # Determine output path and filename
    if output_file_path is None:
        base_dir = os.path.dirname(env_file_path) or "."
        output_file_path = os.path.join(base_dir, "output.xml")

    # Create the root XML element
    root = ET.Element("environment")

    try:
        # Read the .env file
        with open(env_file_path, 'r') as file:
            for line in file:
                # Clean up the line and skip comments or empty lines
                line = line.strip()
                if line and not line.startswith('#'):
                    try:
                        # Split the line into key and value
                        name, value = line.split('=', 1)
                        # Add an element to the XML
                        env_element = ET.SubElement(root, "env")
                        env_element.set("name", name.strip())
                        env_element.set("value", value.strip())
                    except ValueError:
                        print(f"Warning: Invalid format on line: {line}")

        # Write the XML to a file
        tree = ET.ElementTree(root)
        with open(output_file_path, 'wb') as output:
            tree.write(output, encoding='utf-8', xml_declaration=True)

        print(f"Successfully converted '{env_file_path}' to '{output_file_path}'")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Specify paths (update as necessary)
    env_file_path = input("Enter the path to the .env file: ").strip()
    output_file_path = input("Enter the desired output XML file path (leave blank for default): ").strip() or None

    # Perform the conversion
    convert_env_to_xml(env_file_path, output_file_path)