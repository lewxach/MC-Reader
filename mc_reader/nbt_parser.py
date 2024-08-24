import nbt

def parse_nbt_file(file_path):
    try:
        nbt_data = nbt.NBTFile(file_path, 'rb')
        print(f"Parsed NBT file: {file_path}")
        # TODO: process more nbt data for that sweet nectar
    except Exception as e:
        print(f"Error parsing NBT file {file_path}: {e}")