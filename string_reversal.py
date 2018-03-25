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

    final_output = ""

    for ind,ele in enumerate(output):
        final_output += output[len(output) - 1 -ind]
        final_output += ' '
    print(final_output)
