# merge([1,2,4],[1,3,4])

def merge(l1,l2):

    return sorted(l1+l2)
    #or
    l1.extend(l2)
    return sorted(l1)

    # output = []
    # for ele1 in l1:
    #     for ind,ele2 in enumerate(l2):
    #         if ele1 < ele2:
    #             l2.insert(ind-1,ele1)
    #         else:
    #             l2.insert(ind,ele1)
    # return l2
