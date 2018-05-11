def anagram(s1,s2):
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")
    output = {}
    for ele in s1:
        if ele in output:
            output[ele] += 1
        else:
            output[ele] = 1
    for ele in s2:
        if ele in output:
            output[ele] -= 1
        else:
            output[ele] = 1
    for ele in output:
        if output[ele] != 0:
            return False
    return True
anagram('go go go','gggooo')
def pair_sum(s1,s2):
    ##pair_sum([1,3,2,2],4)
    if len(s1) < 2:
        return
    seen = set()
    output = set()
    for ele in s1[1:]:
        val = s2 - ele
        if val not in seen:
            seen.add(val)
        else:
            output.add((val,ele))
    print(output)
pair_sum([1,3,2,2],4)
import collections
def finder(s1,s2):
    #finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]
#     for ele in s1:
#         if ele not in s2:
#             print(ele)
    output = collections.defaultdict(int)
    for ele in s2:
        output[ele] += 1
    for ele in s1:
        if output[ele] == 0:
            return ele
        else:
            output[ele] -= 1
#     print(output)
finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])


def finder1(arr1,arr2):
    arr1.sort()
    arr2.sort()
    for num1, num2 in zip(arr1,arr2):
        if num1!= num2:
            return num1
    return arr1[-1]
finder1([1,2,3,4,5,6,7],[3,7,2,1,4,6])
