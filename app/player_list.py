from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, node):
        self._tail = node

    def is_empty(self):
        return self._head is None

    def insert_head_node(self, player):
        new_player = PlayerNode(player)
        if self.is_empty():
            self._head = new_player
        else:
            new_player.next_player = self._head
            self._head.previous_player = new_player
            self._head = new_player

# self.assertEqual(ll._head.next_node.prev_node.player, player2)
