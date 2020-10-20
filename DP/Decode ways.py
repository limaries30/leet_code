"""91. Decode Ways
Medium

3262

3176

Add to List

Share
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.
Example 4:

Input: s = "1"
Output: 1
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
Accepted
454,024
Submissions
1,798,324
"""


class Solution:
    def numDecodings(self, s: str) -> int:

        self.dp = [0 for i in range(len(s))]

        if len(s) == 0 or s[0] == "0":
            return 0
        if len(s) == 1:
            return 1

        self.dp[0] = 1

        if s[1] == "0":
            if int(s[:2]) > 26:
                return 0
            else:
                self.dp[1] = 1
        else:
            if int(s[:2]) > 26:
                self.dp[1] = 1
            else:
                self.dp[1] = 2

        for i in range(2, len(s)):

            if s[i] == "0":
                if s[i - 1] == "0":
                    return 0
                if int(s[i - 1 : i + 1]) > 26:
                    return 0
                self.dp[i] = self.dp[i - 2]
            else:
                if s[i - 1] != "0":
                    if int(s[i - 1 : i + 1]) <= 26:
                        self.dp[i] = self.dp[i - 2] + self.dp[i - 1]
                    else:
                        self.dp[i] = self.dp[i - 1]
                else:
                    self.dp[i] = self.dp[i - 1]
        return self.dp[len(s) - 1]


#     def numDecodings(self, s: str) -> int:

#         self.last_idx = len(s)-1
#         str_len = len(s)
#         if str_len==0 or str_len==1:
#             return str_len if s!="0" else 0

#         self.s = s
#         self.cnt = 0
#         self.DFS(0)

#         return self.cnt

#     def DFS(self,idx):

#         if idx>self.last_idx:
#             self.cnt+=1
#             return
#         if self.s[idx]=='0':
#             return

#         self.DFS(idx+1)
#         if idx<self.last_idx and int(self.s[idx:idx+2])<=26:
#             self.DFS(idx+2)
