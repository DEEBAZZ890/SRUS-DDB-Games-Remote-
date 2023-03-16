class Player:
    def __init__(self, uid: str, name: str):
        self._uid = uid     # A unique id for the player
        self._name = name       # The name of the player


@property       # getter for uid
def uid(self):
    return self._uid


@property       # getter for name
def name(self):
    return self._name


def __str__(self):      # used to print readable string of the player object
    return f"{self._uid} - {self._name}"
