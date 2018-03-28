def circle_node(node):

    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextnode != None:
        marker1 = nextnode
        marker2 = nextnode.nextnode

        if marker1 == marker2:
            return True

    return False



#Initializing node
class Node(object):
    def __init__(self,node):
            self.value = value
            self.nextnode = None
