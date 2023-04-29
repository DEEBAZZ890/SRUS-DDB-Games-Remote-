from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, player):
        if self._root is None:
            self._root = PlayerBNode(player)
        else:
            self._insert_setup(player, self._root)

    def _insert_setup(self, player, node):
        if player._name < node.player._name:
            if node.left is None:
                node.left = PlayerBNode(player)
            else:
                self._insert_setup(player, node.left)
        elif player._name > node.player._name:
            if node.right is None:
                node.right = PlayerBNode(player)
            else:
                self._insert_setup(player, node.right)
        else:
            node.player = player


    def search(self, name):
        return self._search(name, self._root)

    def _search(self, name, node):
        if node is None or node.player._name == name:
            return node
        elif name < node.player._name:
            return self._search(name, node.left)
        else:
            return self._search(name, node.right)
