class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for val1 in range(0,len(nums)):
            for val2 in range(val1+1, len(nums)):
                if nums[val1] + nums[val2] == target:
                    output.extend([val1,val2])
        return output
