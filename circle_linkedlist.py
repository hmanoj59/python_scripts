def circle_node(node):

    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker1 == marker2:
            return True

    return False



#Initializing node
class Node(object):
    def __init__(self,node):
            self.value = value
            self.nextnode = None

'''
Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean
indicating if the linked list contains a "cycle". A cycle is when a node's next point actually points back to a previous node
in the list. This is also sometimes known as a circularly linked list. You've been given the Linked List Node class code:
'''
