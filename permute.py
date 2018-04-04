def permute(s):
    out = []
    #base case
    if len(s) == 1:
        out = [s]
    #recursion
    else:
        for i,ele in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                out += [ele + perm]
    return out
    
