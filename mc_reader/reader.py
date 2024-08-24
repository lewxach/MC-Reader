import os
import getpass
from .nbt_parser import parse_nbt_file
from .mca_parser import parse_mca_file
from .utils import read_session_lock

class MCReader:
    def __init__(self, world_name):
        current_user = getpass.getuser()
        self.world_path = os.path.join(
            f"C:\\Users\\{current_user}\\AppData\\Roaming\\.minecraft\\saves\\", world_name
        )

    def read_world(self):
        data_dirs = ['data', 'DIM1/data', 'playerdata', 'DIM-1/data']
        mca_dirs = ['entities', 'poi', 'region']

        for dir_name in data_dirs:
            dir_path = os.path.join(self.world_path, dir_name)
            self.read_dat_files(dir_path)

        self.read_level_dat()

        for dir_name in mca_dirs:
            dir_path = os.path.join(self.world_path, dir_name)
            self.read_mca_files(dir_path)

        self.read_session_lock()

    def read_dat_files(self, dir_path):
        if os.path.exists(dir_path):
            for filename in os.listdir(dir_path):
                if filename.endswith('.dat'):
                    file_path = os.path.join(dir_path, filename)
                    parse_nbt_file(file_path)

    def read_level_dat(self):
        level_dat_path = os.path.join(self.world_path, 'level.dat')
        if os.path.exists(level_dat_path):
            parse_nbt_file(level_dat_path)

    def read_mca_files(self, dir_path):
        if os.path.exists(dir_path):
            for filename in os.listdir(dir_path):
                if filename.endswith('.mca'):
                    file_path = os.path.join(dir_path, filename)
                    parse_mca_file(file_path)

    def read_session_lock(self):
        session_lock_path = os.path.join(self.world_path, 'session.lock')
        if os.path.exists(session_lock_path):
            read_session_lock(session_lock_path)