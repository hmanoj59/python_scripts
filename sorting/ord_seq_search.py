def ord_seq_search(arr,ele):
    pos = 0
    found = True
    stopped = True
    while pos < len(arr) and not found and not stopped:
        if arr[pos] == ele:
            found = True
        else:
            if arr[pos] > ele:
                stopped = True
            else:
                pos += 1
    return found
ord_seq_search([1,2,3,4,5],5)
