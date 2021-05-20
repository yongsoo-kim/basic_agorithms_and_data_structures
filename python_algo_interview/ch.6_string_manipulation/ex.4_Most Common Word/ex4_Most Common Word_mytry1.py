# Quiz description URL:
# https://leetcode.com/problems/most-common-word/

# result
# Runtime: 32 ms, faster than 88.43% of Python3 online submissions for Reorder Data in Log Files.
# Memory Usage: 14.4 MB, less than 63.62% of Python3 online submissions for Reorder Data in Log Files.


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_hit = dict()

        paragraph = re.sub('[^a-zA-Z0-9 ]', ' ', paragraph)

        words = [w.lower() for w in paragraph.split()]
        words = [w for w in words if w not in banned]

        max_val = 0
        max_val_key = words[0]

        for w in words:
            if w in banned:
                continue
            else:
                if w in word_hit:
                    word_hit[w] += 1
                    if word_hit[w] > max_val:
                        max_val = word_hit[w]
                        max_val_key = w
                else:
                    word_hit[w] = 1

        return max_val_key

