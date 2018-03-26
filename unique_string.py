
def uniq_str(s):
    if len(s) <= 1:
        return
    i = 1
    while i < len(s):
#         for
        if s[i] == s[i-1]:
            return "False"
        i += 1
    return True

def uniq2_str(s):
    if len(s) <= 1:
        return
    chars = set()
    for ele in s:
        if ele in chars:
            return False
        else:
            chars.add(ele)
    return True

def uniq3_str(s):
    return len(set()) == len(s)
