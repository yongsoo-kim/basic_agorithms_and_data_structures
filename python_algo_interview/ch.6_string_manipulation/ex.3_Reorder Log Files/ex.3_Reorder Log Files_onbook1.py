# Quiz description URL:
# https://leetcode.com/problems/reorder-data-in-log-files/

# point:
# Use lambda & understand sort key

# result
# Runtime: 32 ms, faster than 88.43% of Python3 online submissions for Reorder Data in Log Files.
# Memory Usage: 14.4 MB, less than 63.62% of Python3 online submissions for Reorder Data in Log Files.

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # sort with 2 keys with lambda
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits
