'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)==0:
            return 0
        self.max_cnt = 0
        ans = s[0]
        for i in s:
            idx = ans.find(i)
            if idx==-1:
                ans+=i
            else:
                self.update(len(ans))
                ans = ans[idx+1:]+i
        self.update(len(ans))
        return self.max_cnt
    def update(self,cnt):
        if cnt>self.max_cnt:
            self.max_cnt = cnt