from binary_tree import TreeNode


class BST:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def preorder_traverse(self, cur, func, *args, **kwargs):
        if not cur:
            return

        func(cur, *args, **kwargs)
        self.preorder_traverse(cur.left, func)
        self.preorder_traverse(cur.right, func)

    def insert(self, data):
        new_node = TreeNode()
        new_node.data = data

        cur = self.root
        if not cur:
            self.root = new_node
            return

        while True:
            parent = cur
            if data < cur.data:
                cur = cur.left
                if not cur:
                    parent.left = new_node
                    return
            else:
                cur = cur.right
                if not cur:
                    parent.right = new_node
                    return

    def search(self, target):
        cur = self.root
        while cur:
            if cur.data == target:
                return cur
            elif cur.data > target:
                cur = cur.left
            elif cur.data < target:
                cur = cur.right
        return cur


