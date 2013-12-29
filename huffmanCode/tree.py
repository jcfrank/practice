
class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = ''
        self.count = None

    def __str__(self):
        return self.data + ':' + str(self.count)
