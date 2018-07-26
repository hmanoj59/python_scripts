#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# [2,4,3]
# [5,6,4]

def add_two(l1,l2):
    carry_over = 0
    output = []
    for ele1,ele2 in zip(l1[::-1],l2[::-1]):
        val = ele1 + ele2
        if carry_over != 0:
            val = val + carry_over
            carry_over = 0
        if val > 9:
            carry_over = int(str(val)[0])
            val = int(str(val)[1])
        output.append(val)
    return output
