from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, player):       # Checks if a root exists or if a new player will be added to the BST. If yes, calls insert logic
        if self._root is None:
            self._root = PlayerBNode(player)
        else:
            self.insert_logic(player, self._root)

    def insert_logic(self, player, node):   # Inserts new player in the appropriate location based on their name and the existing nodes.
        if player.name < node.player.name:
            if node.left is None:
                node.left = PlayerBNode(player)
            else:
                self.insert_logic(player, node.left)
        elif player.name > node.player.name:
            if node.right is None:
                node.right = PlayerBNode(player)
            else:
                self.insert_logic(player, node.right)
        else:
            node.player = player

    def search(self, name):       # Calls the search logic method to recursively search through the BST
        return self.search_logic(name, self._root)

    def search_logic(self, name, node):     # Checks each node for a matching player name starting with the root
        if node is None or node.player.name == name:
            return node
        elif name < node.player.name:
            return self.search_logic(name, node.left)
        else:
            return self.search_logic(name, node.right)

    def created_sorted_list(self, node=None, lst=None):     # Sorts non balanced BST by adding from lowest to highest
        if node is None:
            node = self._root
        if lst is None:
            lst = []
        if node.left is not None:
            self.created_sorted_list(node.left, lst)        # Recursive call
        lst.append(node.player)
        if node.right is not None:
            self.created_sorted_list(node.right, lst)       # Recursive call
        return lst

    def bst_balance(self, lst):     # calls the balance optimization and assigns the new root which is the middle element
        self._root = self.bst_balance_logic(lst)

    def bst_balance_logic(self, lst):       # Balancing logic. finds the middle element and then creates left and right subtrees from the midpoint
        if not lst:
            return None
        mid_element = len(lst) // 2
        new_root = PlayerBNode(lst[mid_element])
        new_root.left = self.bst_balance_logic(lst[:mid_element])
        new_root.right = self.bst_balance_logic(lst[mid_element + 1:])
        return new_root
