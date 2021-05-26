# Quiz description URL:
# https://leetcode.com/problems/product-of-array-except-self/


# Point:
# 1.Think left and right separately.
# 2. "1" can be multiplied and it won't affect number change. Let's use this number for default number.
# 3. 여태까지의 곱을 저장할 변수가 loop바깥에 존재해야함을 깨닫는다.
# 4. (1)리스트에 먼저 저장 -> (2)i번째 변경 을 함으로서 리스트에는 i-1개의 변이된 내용이 저장됨. -> 새로운 방식.
# 5. 반대로, (2)i번째 변경 (1)리스트에  저장  을 함으로서 리스트에는 i개의 변이된 내용이 저장됨 -> 내가 주로 하는 방식.




#   ex) [1,2], [3, 4].... idx: 0, 2, ....
# result
# Runtime: 224 ms, faster than 94.00% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21.1 MB, less than 82.01% of Python3 online submissions for Product of Array Except Self.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1
        # 오른쪽 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out