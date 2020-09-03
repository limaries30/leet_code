'''
1208. Get Equal Substrings Within Budget
You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.

You are also given an integer maxCost.

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of twith a cost less than or equal to maxCost.

If there is no substring from s that can be changed to its corresponding substring from t, return 0.

'''

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_cnt = 0
        q = []
        acc_cost = 0
        for i in range(len(s)):
            cost = abs(ord(s[i])-ord(t[i]))
            q.append(cost)
            acc_cost += cost
            if acc_cost > maxCost:
                while acc_cost>maxCost:
                    acc_cost-=q.pop(0)
            q_len = len(q)
            if max_cnt<q_len:
                max_cnt = q_len
        return max_cnt