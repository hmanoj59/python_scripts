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

def bubble_sort(arr):
    for ele in list(range(len(arr)-1,0,-1)):
        for n in list(range(ele)):
            if arr[n] > arr[n+1]:
                temp_var = arr[n+1]
                arr[n+1] = arr[n]
                arr[n] = temp_var
    return arr
arr = [3,2,13,4,6,5,7,8,1,20]
bubble_sort(arr)
