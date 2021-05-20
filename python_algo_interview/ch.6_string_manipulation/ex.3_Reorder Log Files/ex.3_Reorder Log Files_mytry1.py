# Quiz description URL:
#https://leetcode.com/problems/reorder-data-in-log-files/

# result
# Failed!!!!!!!!!!!!!!!

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = list()
        letter_logs = list()

        for log in logs:
            log_parts = log.split()
            log_id = log_parts[0]
            log_content_frag = log_parts[1]
            if log_content_frag.isnumeric():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        ln = len(letter_logs)

        for i in range(0, ln - 1):
            for j in range(i + 1, ln):
                id1 = letter_logs[i].split()[0]
                id2 = letter_logs[j].split()[0]
                contents1 = ''.join(letter_logs[i].split()[1:])
                contents2 = ''.join(letter_logs[j].split()[1:])
                if contents1 > contents2:
                    letter_logs[j], letter_logs[i] = letter_logs[i], letter_logs[j]

                elif contents1 == contents2:
                    if id1 > id2:
                        letter_logs[j], letter_logs[i] = letter_logs[i], letter_logs[j]


        return letter_logs + digit_logs