import unittest
from app.player_list import PlayerList
from app.player import Player
from app.player_node import PlayerNode


class TestLinkedList(unittest.TestCase):

    def test_empty_list_insert(self):   # Test that inserts a player into an empty list
        test_list = PlayerList()
        test_player = Player("20069321", "Daniel")
        test_list.insert_head_node(test_player)

        self.assertEqual(test_list._head.player, test_player)
        self.assertIsNone(test_list._head.next_player)
        self.assertIsNone(test_list._head.previous_player)

    def test_filled_list_insert(self):  # Test that inserts a player into an already populated list
        test_list = PlayerList()
        test_existing_player = Player("20069321", "Daniel")
        test_new_player = Player("10472204", "John")

        test_list.insert_head_node(test_existing_player)
        test_list.insert_head_node(test_new_player)

        self.assertEqual(test_list._head.player, test_new_player)
        self.assertEqual(test_list._head.next_player.player, test_existing_player)
        self.assertIsNone(test_list._head.previous_player)
        self.assertEqual(test_list._head.next_player.previous_player.player, test_new_player)

    def test_tail_insert_on_list(self):     # Tests the tail insert functionality by entering three new players into an empty list. Also checks that the order is preserved when new entries are added
        test_list = PlayerList()
        test_insert_one = test_list.insert_tail_node(Player("20069321", "Daniel"))
        test_insert_two = test_list.insert_tail_node(Player("10472204", "John"))
        test_insert_three = test_list.insert_tail_node(Player("29543305", "Brayden"))

        self.assertEqual(test_list._head, test_insert_one)
        self.assertEqual(test_list._tail, test_insert_three)
        self.assertEqual(test_insert_one.next_player, test_insert_two)
        self.assertEqual(test_insert_two.previous_player, test_insert_one)
        self.assertEqual(test_insert_two.next_player, test_insert_three)
        self.assertEqual(test_insert_three.previous_player, test_insert_two)

    def test_single_item_delete_head_from_list(self):   # Tests the delete method when a single entry is stored in the list
        test_list = PlayerList()
        temp_player_head = Player("20069321", "Daniel")
        test_list.insert_head_node(temp_player_head)

        self.assertEqual(test_list.delete_head_node(), temp_player_head)
        self.assertTrue(test_list._head is None)

    def test_three_item_list_delete_head(self):     # Tests the delete method on a populated list to ensure that order is preserved and delete is working when existing items are present.
        test_list = PlayerList()
        first_head = Player("20069321", "Daniel")
        second_head = Player("10472204", "John")
        third_head = Player("29543305", "Brayden")
        test_list.insert_head_node(first_head)
        test_list.insert_head_node(second_head)
        test_list.insert_head_node(third_head)

        self.assertEqual(test_list.delete_head_node(), third_head)
        self.assertEqual(test_list._head.player, second_head)

    def test_two_items_list_delete_tail(self):      # Test for ensuring that the tail deletion updates the pointers for the newly assigned tail
        test_list = PlayerList()
        first_tail = Player("20069321", "Daniel")
        second_tail = Player("10472204", "John")
        test_list.insert_tail_node(first_tail)
        test_list.insert_tail_node(second_tail)

        self.assertEqual(test_list.delete_tail_node(), second_tail)
        self.assertEqual(test_list._tail.player, first_tail)

    def test_delete_item_by_key(self):      # Tests the delete by key method. Checks that target player is removed and pointers are updated
        test_list = PlayerList()
        first_insert = Player("20069321", "Daniel")
        second_insert = Player("10472204", "John")
        third_insert = Player("29543305", "Brayden")
        test_list.insert_head_node(first_insert)
        test_list.insert_head_node(second_insert)
        test_list.insert_head_node(third_insert)
        test_list.delete_player_node_by_key("10472204")

        self.assertEqual(test_list._head.player._uid, "29543305")
        self.assertIsNone(test_list._head.previous_player)
