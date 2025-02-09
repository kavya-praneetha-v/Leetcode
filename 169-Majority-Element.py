class Solution:
    def majorityElement(self, nums: List[int]) -> int:        
        nums.sort()
        n = len(nums)
        count = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                if count > n//2:
                    return nums[i-1]
                count = 0
            count += 1
        return nums[n-1]


        