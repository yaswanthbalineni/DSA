class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total=sum(nums)
        left_sum=0
        res=[]
        for i in range(len(nums)):
            right_sum=total-left_sum-nums[i]
            res.append(abs(left_sum-right_sum))
            left_sum+=nums[i]
        return res