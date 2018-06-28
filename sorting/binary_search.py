def binary_search(arr,ele):
    first = 0
    last = len(arr) - 1
    found = False    
    while first <= last and not found:
        middle = int((first+last)/2)
        if ele == arr[middle]:
            found = True
        else:
            if ele < arr[middle]:
                last = middle -1 
            else:
                first = middle + 1
    return found
binary_search([1,2,3,4,5,6],7)
