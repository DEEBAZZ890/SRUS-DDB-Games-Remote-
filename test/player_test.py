import unittest
from app.player import Player


class TestPlayerPrivateInstanceVariables(unittest.TestCase):
    def test_uid(self):     # Checks that player id is added successfully
        player = Player("20069321", "Daniel")
        self.assertEqual(player._uid, "20069321")

    def test_name(self):       # Checks that player name is added successfully
        player = Player("20069321", "Daniel")
        self.assertEqual(player._name, "Daniel")

