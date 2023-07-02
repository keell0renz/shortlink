import unittest
from src.database.database import get_session

# python3 -m unittest discover -p "test*.py" -s test

# No tests temporarily!


class TestDatabase(unittest.TestCase):
    def test_getting_session(self):
        with get_session() as session:
            pass


if __name__ == "__main__":
    unittest.main()
