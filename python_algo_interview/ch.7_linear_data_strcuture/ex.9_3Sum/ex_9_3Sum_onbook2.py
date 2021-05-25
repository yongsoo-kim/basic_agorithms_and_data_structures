# Quiz description URL:
# https://leetcode.com/problems/3sum/


# Point:
# 1.Use 2 pointer
# 2. Before use 2 pointer, sort first!

# result
# Runtime: 864 ms, faster than 71.60% of Python3 online submissions for 3Sum.
# Memory Usage: 17.5 MB, less than 50.49% of Python3 online submissions for 3Sum.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    # 중복 제거
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results
