def move_n(val, head):
    left_node = head
    right_node = head
    
    for i in range(val-1):
        if not right_node.nextnode:
            return "False nodes less than val"            
        right_node = right_node.nextnode

    while right_node.nextnode:
        left_node = left_node.nextnode
        right_node = right_node.nextnode
    return left_node
        
        
        
