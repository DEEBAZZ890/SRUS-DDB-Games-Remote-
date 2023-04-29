import unittest

from app.player import Player
from app.player_bst import PlayerBST


class TestBST(unittest.TestCase):

    def setup(self):
        self.players = [Player("20069321", "Daniel"), Player("10472204", "John"),  Player("29543305", "Brayden")]
        self.bst = PlayerBST()
        for player in self.players:
            self.bst.insert(player)

# Somereason the setup isnt runnign. FIX YOU SILLY PERSON

    def test_insert(self):
        self.setup()
        self.assertEqual(self.bst.root.player, self.players[0])
        self.assertEqual(self.bst.root.right.player, self.players[1])
        self.assertEqual(self.bst.root.left.player, self.players[2])

    def test_update_insert(self):
        self.setup()
        new_player = Player("385674678", "Mike")
        self.bst.insert(new_player)
        self.assertEqual(self.bst.root.right.right.player, new_player)

    def test_search_existing_player(self):
        self.setup()
        daniel = self.bst.search("Daniel")
        self.assertEqual(daniel.player, self.players[0])

    def test_search_non_existing_player(self):
        self.setup()
        luke = self.bst.search("Luke")
        self.assertIsNone(luke)

