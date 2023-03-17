import argon2
from argon2 import PasswordHasher


class Player:
    def __init__(self, uid: str, name: str):
        self._uid = uid  # A unique id for the player
        self._name = name  # The name of the player
        self._hashed_password = None

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


@property  # getter for uid
def uid(self):
    return self._uid


@property  # getter for name
def name(self):
    return self._name


def __str__(self):  # used to print readable string of the player object
    return f"{self._uid} - {self._name}"
