##Binary Search Algorithm
def binary_search(arr, ele):
    first_ele = 0
    last_ele = len(arr) - 1
    found = False

    middle_ele = int((first_ele + last_ele)/2)

    while first_ele <= last_ele or found:
        if ele == arr[middle_ele]:
            found = True
            return middle_ele
        if ele <  arr[middle_ele]:
            mid = mid - 1
        else:
            mid = mid + 1
                    
