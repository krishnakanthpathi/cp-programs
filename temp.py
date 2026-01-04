from typing import List
from collections import defaultdict


class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        l = 1
        n = len(nums)
        r = n
        res = float("inf")
        while l <= r :
            mid = (l + r) // 2
            flag = False
            cur = 0
            left = 0
            hashset = defaultdict(int)
            for right in range(n) :
                if right - left + 1 > mid :
                    hashset[nums[left]] -= 1
                    if hashset[nums[left]] <= 0 :
                        cur -= nums[left]
                        hashset.pop(nums[left])
                    left += 1
                if nums[right] not in hashset :
                    cur += nums[right]
                if cur >= k :
                    flag = True
                    break
                hashset[nums[right]] += 1
            if flag :
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res if res != float("inf") else -1

ans = Solution()
# nums =
# [22,8,27,13,12,26,2]
# k =
# 51©leetcode
nums = [22,8,27,13,12,26,2]
k = 51
print(ans.minLength(nums, k))
