def te(test_ip):
    # 165.87.67.23
    # 4.5.6.7

    if len(test_ip) < 6:
        return False
    l = [0,1,2,3,4,5,6,7,8,9,'.']
    new_ip = test_ip.split('.')
    for ele in new_ip:

        if ele == '.':
            if ele not in range(0,9):
                return False
