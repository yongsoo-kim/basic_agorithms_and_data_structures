# Quiz description URL:
# https://leetcode.com/problems/group-anagrams/

# Point:
# 1.Use Deque.
# 2.Use 'values()' method for return the dictionary value lists.

# result
# Runtime: 108 ms, faster than 35.43% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.6 MB, less than 66.43% of Python3 online submissions for Group Anagrams.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strs: Deque = collections.deque(strs)
        char_dict = dict()

        while strs:
            word = strs.popleft()
            char_list = []

            for w in word:
                char_list.append(w)

            char_list.sort()
            dict_key = ''.join(char_list)

            if dict_key not in char_dict:
                char_dict[dict_key] = [word]

            else:
                char_dict[dict_key].append(word)

        return char_dict.values()
