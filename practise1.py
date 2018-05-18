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

def finder2(arr1,arr2):
    import collections
    val = {}
    d = collections.defaultdict(int)
    for ele in arr2:
        d[ele] += 1
    for ele in arr1:
        if d[ele] == 0:
            return ele
        else:
            d[ele] -= 1

def finder1(arr1,arr2):
    arr1.sort()
    arr2.sort()
    for num1, num2 in zip(arr1,arr2):
        if num1!= num2:
            return num1
    return arr1[-1]
finder1([1,2,3,4,5,6,7],[3,7,2,1,4,6])
def rev_word(s):
    out = []
    i = 0
    while i < len(s):
        if s[i] != ' ':
            start_ele = i
            while i < len(s) and s[i] != ' ':
                i += 1
            out.append(s[start_ele:i])
        i += 1
    return ' '.join(reversed(out))
rev_word('go? to ready you are John, Hi')
def compress(s):
    if len(s) < 2:
        return s + str(1)
    output = ""
    i = 0
    count = 1
    while i < len(s):
        if s[i] == s[i-1]:
            count += 1
        else:
            output = output + s[i-1] + str(count)
            count = 1
        i += 1
    output = output + s[i-1] + str(count)
    return output
compress(' AAAAABBBBCCCC')
def uniq(s):
#     return len(set(s)) == len(s)
    output = set()
    for ele in s:
        if ele in output:
            return False
        else:
            output.add(ele)
    return True
uniq('abcdefg')
def large_cont_sum(arr):
    if len(arr) == 0:
        return 0
    current_sum = max_sum = arr[0]
    for ele in arr[1:]:
        current_sum = max(current_sum+ele,ele)
        max_sum = max(current_sum, max_sum)
    return max_sum
large_cont_sum([1,2,-1,3,4,10,10,-10,-1])

class stack():
    def __init__(self):
        self.items = []
    def isempty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def size(self):
        return len(self.items)
s = stack()
s.push(2)
s.isempty()
s.push(1)
s.size()
s.pop()
s.pop()
class queue():
    def __init__(self):
        self.items = []
    def isempty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
s = queue()
s.isempty()
s.push(1)
s.push(2)
s.push('three')
s.isempty()
s.size()
s.pop()
s.pop()
s.pop()
def balance_check(s):
    opening = ['(','{','[']
    matches = set([('(',')'),('{','}'),('[',']')])
    output = []
    if len(s)%2 != 0:
        return False
    for ele in s:
        if ele in opening:
            output.append(ele)
        else:
            last_ele = output.pop()
            if ( last_ele,ele ) not in matches:
                return False
    return True



balance_check('[](){([[[]]])}')
class circular_double_linked_list():
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        self.previousnode = None
a = circular_double_linked_list(1)
b = circular_double_linked_list(2)
a.nextnode = b
b.previousnode = a
a.previousnode = b
b.nextnode = a
class Single_linked_list():
    def __init__(self, item):
        self.item = item
        self.nextnode = None
def cycle_check(node):
###Test to check if it is a circular linked list
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode
        if marker1 == marker2:
            return True
    return False
