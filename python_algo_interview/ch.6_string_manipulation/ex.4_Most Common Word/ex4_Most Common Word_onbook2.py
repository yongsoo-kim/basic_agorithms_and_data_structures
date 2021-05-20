# Quiz description URL:
# https://leetcode.com/problems/most-common-word/

# Point:
# 1.Understand regular expression and why 'r' is necessary for 'sub'
# 2.Use Counter. This will return word counts in tuple format in clear way.
# 3.Understand 'most_common' method

# result
# Runtime: 36 ms, faster than 61.95% of Python3 online submissions for Most Common Word.
# Memory Usage: 14.2 MB, less than 74.69% of Python3 online submissions for Most Common Word.


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 데이터 전처리(Preprocessing)가 필요함.
        # 값을 깨끗하게 하기 위해 Data Cleansing을 실시.
        words = [word for word in re.sub(r'[^\w]',' ', paragraph).lower().split() if word not in banned]

        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫번째 인덱스 리턴
        # ex) [('ball', 2)]
        return counts.most_common(1)[0][0]

