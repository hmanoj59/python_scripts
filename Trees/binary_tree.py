def binary_tree(root):
    return [root,[],[]]

def insert_left(root,new_branch):
    prev_child = root.pop(1)
    if len(prev_child) > 1:
        root.insert(1,[new_branch,prev_child,[]])
    else:
        root.insert(1,[new_branch,[],[]])
    return root

def insert_right(root, new_branch):
    prev_child = root.pop(2)
    if len(prev_child) > 1:
        root.insert(2, [new_branch,[],prev_child])
    else:
        root.insert(2,[new_branch,[],[]])
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]
r = binary_tree(1)
insert_left(r,2)
insert_left(r,3)
insert_right(r,4)
insert_right(r,5)
get_root_val(r)
set_root_val(r,6)
get_root_val(r)
get_left_child(r)
get_right_child(r)
