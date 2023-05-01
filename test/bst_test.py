import unittest

from app.player import Player
from app.player_bst import PlayerBST


class TestBST(unittest.TestCase):

    def setUp(self):        # Create list of test players and insert them into the Binary Search Tree
        self.players = [Player("20069321", "Daniel"), Player("10472204", "John"),  Player("29543305", "Brayden")]
        self.bst = PlayerBST()
        for player in self.players:
            self.bst.insert(player)

    def test_insert(self):      # test the insert method by checking that the players were correctly inserted and sorted
        self.assertEqual(self.bst.root.player, self.players[0])
        self.assertEqual(self.bst.root.right.player, self.players[1])
        self.assertEqual(self.bst.root.left.player, self.players[2])

    def test_search_existing_player(self):      # test that bst can find player by name
        target = self.bst.search("Daniel")
        self.assertEqual(target.player, self.players[0])

    def test_search_non_existent_player(self):      # test that search returns nothing if player doesn't exist
        target = self.bst.search("Luke")
        self.assertIsNone(target)

