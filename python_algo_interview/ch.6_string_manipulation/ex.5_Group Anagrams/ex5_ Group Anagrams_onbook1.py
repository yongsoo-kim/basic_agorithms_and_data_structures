# Quiz description URL:
# https://leetcode.com/problems/group-anagrams/

# Point:
# 1.Use Deque.
# 2.Use 'values()' method for return the dictionary value lists.

# result
# Runtime: 112 ms, faster than 31.34% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.2 MB, less than 80.62% of Python3 online submissions for Group Anagrams.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Set default '[]' for every single keys. This will prevent 'append' Key error on line No.20
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()