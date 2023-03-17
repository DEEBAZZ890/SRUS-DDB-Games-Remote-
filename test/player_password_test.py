import unittest

from argon2 import PasswordHasher

from app.player import Player


class TestPlayerClassPasswordMethods(unittest.TestCase):

    def test_add_password(self):        # tests that the add password method works by verifying the stored password after the method has been called
        test_player = Player("20069321", "Daniel")
        test_player.add_password("password")
        self.assertTrue(test_player.verify_password("password"))
        self.assertIsNotNone(test_player._hashed_password)

    def test_verify_that_password_is_correct(self):     # checks that verification returns true if password is correct
        test_player = Player("20069321", "Daniel")
        test_player.add_password("password")
        self.assertTrue(test_player.verify_password("password"))

