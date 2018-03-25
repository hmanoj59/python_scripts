def ref_str(str):
    output = []
    i = 0
    while i < len(str):
        if str[i] != ' ':
            first_char = i
            while i < len(str) and str[i] != ' ':
                i += 1
            output.append(str[first_char:i])
        i +=1
    return " ".join(reversed(output))
