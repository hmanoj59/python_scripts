class BinaryTree(object):
    def __init__(self,obj):
        self.key = obj
        self.left_child = None
        self.right_child = None
    def insert_left(self, obj):
        if self.left_child == None:
            self.left_child = BinaryTree(obj)
        else:
            new_node = BinaryTree(obj)
            new_node.left_child = self.left_child
            self.left_child = new_node
    def insert_right(self, obj):
        if self.right_child == None:
            self.right_child = BinaryTree(obj)
        else:
            new_node = BinaryTree(obj)
            new_node.right_child = self.right_child
            self.right_child = new_node
    def get_left_child(self):
        return self.left_child
    def get_right_child(self):
        return self.right_child
    def get_root_val(self):
        return self.key
    def set_root_val(self, new_val):
        self.key = new_val
b = BinaryTree(1)
b.insert_left(2)
b.get_root_val()
b.get_left_child().get_root_val()
b.insert_right(3)
b.get_right_child().get_root_val()
b.set_root_val(4)
b.get_root_val()
