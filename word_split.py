def word_split(st, list_of_ele, output = None):
    if output is None:
        output = []
    for ele in list_of_ele:
        if st.startswith(ele):
            output.append(ele)
            return word_split(st[len(ele):], list_of_ele, output)
    return output
