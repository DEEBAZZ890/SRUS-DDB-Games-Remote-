import unittest
from app.player import Player


class TestPlayerStringMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.test_player = Player("20069321", "Daniel")

    def test_if_(self):
        self.assertEqual(self.test_player, '', '')
        return "Player test was not empty"

    def test_if_uid_is_string(self):
        print("nothing")


if __name__ == '__main__':
    unittest.main()
