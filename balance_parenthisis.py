def balance_paranthesis(s):
    if len(s)%2 != 0:
        return False
    opening = ['(', '{', '[']
    matches = [('(',')'), ('{','}'), ('[',']')]
    stack = []
    for ele in s:
        if ele in opening:
            stack.append(ele)
        else:
            if len(stack) == 0:
                return False
            last_ele = stack.pop
            if (last_ele, ele) not in matches:
                return False
    return len(stack) == 0

balance_paranthesis("{([])}")
balance_paranthesis("{{())}}")
