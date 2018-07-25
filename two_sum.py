##Given an array of integers, return indices of the two numbers such that they add up to a specific target.
##You may assume that each input would have exactly one solution, and you may not use the same element twice.
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
def test_sum(ar,tar):
    i = 0
    output = []
    while i < len(ar):
        for ele in ar[i:]:
            if ar[i] + ele == tar:
                output.append((i,ar.index(ele)))
        i += 1
    return output
