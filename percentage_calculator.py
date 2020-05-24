if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    lines = ""
    for _ in range(n):
        name, *new_line = input().split()
        sum_total = 0
        for ele in new_line:
            sum_total += float(ele)
        avg = sum_total/float(len(new_line))
        student_marks[name] = round(avg,2)
        
        # scores = list(map(float, line))
        # student_marks[name] = scores
    query_name = input()
    print("%.2f" % student_marks[query_name])
# print(lines)

