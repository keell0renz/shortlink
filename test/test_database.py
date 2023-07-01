import unittest
from src.database.database import get_session

#python3 -m unittest discover -p "test*.py" -s test

class TestDatabase(unittest.TestCase):
    def test_getting_session(self):
        pass

if __name__ == "__main__":
    unittest.main()