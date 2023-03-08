from player import Player


class PlayerNode:
    def __init__(self, player):
        self._player = player
        self._next_player = None
        self._previous_player = None

    @property
    def player(self):
        return self._player

    @property
    def next_player(self):
        return self._next_player

    @next_player.setter
    def next_player(self, node):
        self.next_player = node

    @property
    def previous_player(self):
        return self._previous_player

    @previous_player.setter
    def previous_player(self, node):
        self.previous_player = node

    @property
    def key(self):
        return self._player.uid

    def __str__(self):
        return f"{self.key}, {self.player}"


