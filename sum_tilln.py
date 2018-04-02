def sum_n(n):
    if n < 10:
        return n
    else:
        return n%10 + sum_n(int(n/10))
