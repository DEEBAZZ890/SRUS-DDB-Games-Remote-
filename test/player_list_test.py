import unittest
from app.player_list import PlayerList
from app.player import Player
from app.player_node import PlayerNode


class TestLinkedList(unittest.TestCase):
    def test_empty_list_insert(self):
        test_list = PlayerList()
        test_player = Player(20069321, "Daniel")
        test_list.insert_head_node(test_player)
        self.assertEqual(test_list._head.player, test_player)
        self.assertIsNone(test_list._head.next_player)
        self.assertIsNone(test_list._head.previous_player)

    def test_filled_list_insert(self):
        test_list = PlayerList()
        test_existing_player = Player(20069321, "Daniel")
        test_new_player = Player(10472204, "John")

        test_list.insert_head_node(test_existing_player)
        test_list.insert_head_node(test_new_player)

        self.assertEqual(test_list._head.player, test_new_player)
        self.assertEqual(test_list._head.next_player.player, test_existing_player)
        self.assertIsNone(test_list._head.previous_player)
        self.assertEqual(test_list._head.next_player.previous_player.player, test_new_player)

    def test_tail_insert_on_list(self):
        test_list = PlayerList()
        test_insert_one = test_list.insert_tail_node(Player(20069321, "Daniel"))
        test_insert_two = test_list.insert_tail_node(Player(10472204, "John"))
        test_insert_three = test_list.insert_tail_node(Player(29543305, "Brayden"))

        self.assertEqual(test_list._head, test_insert_one)
        self.assertEqual(test_list._tail, test_insert_three)
        self.assertEqual(test_insert_one.next_player, test_insert_two)
        self.assertEqual(test_insert_two.previous_player, test_insert_one)
        self.assertEqual(test_insert_two.next_player, test_insert_three)
        self.assertEqual(test_insert_three.previous_player, test_insert_two)
