import struct

def parse_mca_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            header = f.read(8192)  # i think tha first 8 kb is the header
            for i in range(0, 4096, 4):
                offset = struct.unpack(">I", header[i:i+4])[0]
                if offset != 0:
                    sector = offset >> 8
                    print(f"Found chunk at sector {sector} in file {file_path}")
        # TODO: add more processing of the file
    except Exception as e:
        print(f"Error parsing MCA file {file_path}: {e}")