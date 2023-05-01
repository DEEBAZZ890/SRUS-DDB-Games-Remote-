import unittest

from app.player import Player
from app.player_bst import PlayerBST


class TestBST(unittest.TestCase):

    def setUp(self):
        self.players = [Player("20069321", "Daniel"), Player("10472204", "John"),  Player("29543305", "Brayden")]
        self.bst = PlayerBST()
        for player in self.players:
            self.bst.insert(player)

    def test_insert(self):
        self.assertEqual(self.bst.root.player, self.players[0])
        self.assertEqual(self.bst.root.right.player, self.players[1])
        self.assertEqual(self.bst.root.left.player, self.players[2])

    def test_update_insert(self):
        new_player = Player("385674678", "Mike")
        self.bst.insert(new_player)
        self.assertEqual(self.bst.root.right.right.player, new_player)

    def test_search_existing_player(self):
        daniel = self.bst.search("Daniel")
        self.assertEqual(daniel.player, self.players[0])

    def test_search_non_existing_player(self):
        luke = self.bst.search("Luke")
        self.assertIsNone(luke)

