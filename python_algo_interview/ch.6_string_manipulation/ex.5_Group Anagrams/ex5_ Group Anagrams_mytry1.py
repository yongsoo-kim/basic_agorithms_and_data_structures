# Quiz description URL:
# https://leetcode.com/problems/group-anagrams/

# result
# Runtime: 172 ms, faster than 6.71% of Python3 online submissions for Group Anagrams.
# Memory Usage: 16.9 MB, less than 99.12% of Python3 online submissions for Group Anagrams.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        char_dict = dict()

        while strs:
            word = strs.pop(0)
            char_list = []

            for w in word:
                char_list.append(w)

            char_list.sort()
            dict_key = ''.join(char_list)

            if dict_key not in char_dict:
                char_dict[dict_key] = [word]

            else:
                char_dict[dict_key].append(word)

        result = []

        for key in char_dict.keys():
            result.append(char_dict[key])

        return result
