class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=sum(nums)
        if abs(target)>total:
            return 0
        if (total+target)%2!=0:
            return 0
        n=len(nums)
        r=(total+target)//2
        dp=[[-1]*(r+1)for _ in range(n+1)]
        def solve(n,target):
            if n==0:
                return 1 if target==0 else 0
            if dp[n][target]!=-1:
                return dp[n][target]
            if nums[n-1]>target:
                dp[n][target]=solve(n-1,target)
            else:
                inc=solve(n-1,target-nums[n-1])
                exc=solve(n-1,target)
                dp[n][target]=inc+exc
            return dp[n][target]
        return solve(n,r)