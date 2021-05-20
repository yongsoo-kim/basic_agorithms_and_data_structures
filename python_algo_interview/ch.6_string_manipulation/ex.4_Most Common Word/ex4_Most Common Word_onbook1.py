# Quiz description URL:
# https://leetcode.com/problems/most-common-word/

# Point:
# 1.lower can work whole string
# 2.Use list comprehension
# 3.Understand how to get max value key from dictionary

# result
# Runtime: 36 ms, faster than 61.95% of Python3 online submissions for Most Common Word.
# Memory Usage: 14.4 MB, less than 49.41% of Python3 online submissions for Most Common Word.


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 데이터 전처리(Preprocessing)가 필요함.
        # 값을 깨끗하게 하기 위해 Data Cleansing을 실시.
        words = [word for word in re.sub(r'[^\w]',' ', paragraph).lower().split() if word not in banned]

        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1

        # get the max value key.
        return max(counts, key=counts.get)

