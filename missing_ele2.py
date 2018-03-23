import collections

def missing_element(arr1, arr2):

    d = collections.defaultdict(int) #Initalizes key if it does not have in hash

    for ele in arr2:
        d[ele] += 1
    for ele in arr1:
        if d[ele] == 0:
            return ele
        else:
            d[ele] -= 1
missing_element([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1])
