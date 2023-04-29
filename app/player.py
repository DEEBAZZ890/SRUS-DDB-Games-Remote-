import argon2
from argon2 import PasswordHasher


class Player:
    def __init__(self, uid: str, name: str):
        self._uid = uid  # A unique id for the player
        self._name = name  # The name of the player
        self._hashed_password = None
        self._score = 0

    def add_password(self, password):
        if not password:
            return "No password entered. The player requires a password that is not empty"
        else:
            ph = PasswordHasher()
            hash_value = ph.hash(password)
            self._hashed_password = hash_value

    def verify_password(self, password):
        ph = PasswordHasher()
        verification = ph.verify(self._hashed_password, password)
        return verification

    @staticmethod
    def sort_players_descending(player_list):
        list_length = len(player_list)
        # Insertion sort algorithm
        for i in range(1, list_length):
            current_player = i - 1
            key = player_list[i]
            while current_player >= 0 and player_list[current_player].score < key.score:
                player_list[current_player + 1] = player_list[current_player]
                current_player -= 1
            player_list[current_player + 1] = key
        return player_list


@property  # getter for uid
def uid(self):
    return self._uid


@property  # getter for name
def name(self):
    return self._name


@name.setter
def name(self, value):
    self._name = value


@property
def score(self):
    return self._score


@score.setter
def score(self, value):
    if value < 0:
        raise ValueError("Score must be positive")
    else:
        self._score = value


def __str__(self):  # used to print readable string of the player object
    return f"{self._uid} - {self._name}"


def __lt__(self, other):  # Dunder method for less than
    return self.score < other.score


def __le__(self, other):  # Dunder method for less than or equal to
    return self.score <= other.score


def __eq__(self, other):  # Dunder method for equal to
    return self.score == other.score


def __gt__(self, other):  # Dunder method for greater than
    return self.score > other.score


def __ge__(self, other):  # Dunder method for greater than or equal to
    return self.score >= other.score
