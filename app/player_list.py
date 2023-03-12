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
            self._tail = new_player
        else:
            new_player.next_player = self._head
            self._head.previous_player = new_player
            self._head = new_player
        return new_player

    def delete_head_node(self):
        if self.is_empty():
            return None
        else:
            existing_head = self._head
            self._head = existing_head.next_player
            if self._head is None:
                self._tail = None
            else:
                self._head.previous_player = None
            return existing_head.player

    def insert_tail_node(self, player):
        new_player = PlayerNode(player)
        if self.is_empty():
            self._head = new_player
            self._tail = new_player
        else:
            new_player.previous_player = self._tail
            self._tail.next_player = new_player
            self._tail = new_player
        return new_player

    def delete_tail_node(self):
        if self._tail is None:
            return None
        else:
            existing_tail = self._tail
            self._tail = existing_tail.previous_player
            if self._tail is None:
                self._head = None
            else:
                self._tail.next_player = None
            return existing_tail.player

