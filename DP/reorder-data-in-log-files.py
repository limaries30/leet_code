class Solution:
    def reorderLogFiles(self, logs):
        digit_arr = []
        answer = []
        tmp_arr = []
        for log in logs:
            if log[0] == "d":
                digit_arr.append(log)
            else:
                if len(answer) > 0:
                    
                    while answer and self.compare(answer[-1], log):
                        tmp_arr.insert(0, answer.pop())
                    answer.append(log)
                    answer.extend(tmp_arr)
                    tmp_arr = []
                else:
                    answer.append(log)
        answer.extend(digit_arr)
        return answer

    def compare(self, a, b):
        a = a.split()
        b = b.split()

        if a[1] > b[1]:
            return True
        return False


input_1 = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
solution = Solution()
solution.reorderLogFiles(input_1)
