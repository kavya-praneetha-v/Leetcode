class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current = nums[0]
        maxsum = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] >= nums[i]:
                current = 0
            current = current + nums[i]
            maxsum = max(maxsum, current)
        return maxsum        