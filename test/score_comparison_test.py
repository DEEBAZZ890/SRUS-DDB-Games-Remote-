import unittest
from app.player import Player
from app.player_list import PlayerList


class TestPlayerScoreComparison(unittest.TestCase):
    def test_less_than(self):                               # Tests that __lt__ dunder method works on scores
        player_one = Player("20069321", "Daniel")
        player_two = Player("10472204", "John")
        player_three = Player("29543305", "Brayden")
        player_one.score = 100
        player_two.score = 50
        player_three.score = 75
        self.assertTrue(player_two.score < player_one.score)
        self.assertFalse(player_one.score < player_two.score)
        self.assertFalse(player_one.score < player_three.score)

    def test_less_than_or_equal(self):                      # Tests that __le__ dunder method works on scores
        player_one = Player("20069321", "Daniel")
        player_two = Player("10472204", "John")
        player_three = Player("29543305", "Brayden")
        player_one.score = 100
        player_two.score = 50
        player_three.score = 75
        self.assertTrue(player_two.score <= player_one.score)
        self.assertTrue(player_one.score <= player_one.score)
        self.assertFalse(player_one.score <= player_two.score)

    def test_equal(self):                                        # Tests that __eq__ dunder method works on scores
        player_one = Player("20069321", "Daniel")
        player_two = Player("10472204", "John")
        player_three = Player("29543305", "Brayden")
        player_one.score = 100
        player_two.score = 50
        player_three.score = 75
        self.assertFalse(player_two.score == player_one.score)
        self.assertFalse(player_one.score == player_three.score)

    def test_greater_than(self):                                  # Tests that __gt__ dunder method works on scores
        player_one = Player("20069321", "Daniel")
        player_two = Player("10472204", "John")
        player_three = Player("29543305", "Brayden")
        player_one.score = 100
        player_two.score = 50
        player_three.score = 75
        self.assertTrue(player_one.score > player_two.score)
        self.assertFalse(player_two.score > player_one.score)
        self.assertTrue(player_one.score > player_three.score)

    def test_greater_than_or_equal(self):                          # Tests that __qe__ dunder method works on scores
        player_one = Player("20069321", "Daniel")
        player_two = Player("10472204", "John")
        player_three = Player("29543305", "Brayden")
        player_one.score = 100
        player_two.score = 50
        player_three.score = 75
        self.assertTrue(player_one.score >= player_two.score)
        self.assertTrue(player_one.score >= player_one.score)
        self.assertFalse(player_two.score >= player_one.score)

    def test_descending_sort(self):                                # Tests that descending sort of scores for players is working
        player_one = Player("20069321", "Daniel")
        player_two = Player("10472204", "John")
        player_three = Player("29543305", "Brayden")
        player_one.score = 20
        player_two.score = 15
        player_three.score = 43
        test_list = [player_one, player_two, player_three]
        sorted_list = Player.sort_players_descending(test_list)
        expected_order = [player_three, player_one, player_two]
        self.assertEqual(sorted_list[0].score, 43)
        self.assertEqual(sorted_list[1].score, 20)
        self.assertEqual(sorted_list[2].score, 15)
        self.assertEqual(sorted_list, expected_order)


