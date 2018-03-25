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

    for value in output[::-1]:
        final_output += element
        final_output += ' '
    print(final_output)
