import unittest
from mc_reader import MCReader

class TestMCReader(unittest.TestCase):
    def test_world_reading(self):
        reader = MCReader("test_world")
        reader.read_world()

if __name__ == '__main__':
    unittest.main()