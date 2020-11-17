'''
https://leetcode.com/problems/longest-palindrome/
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = defaultdict(int)
        cnt = 0
        for i in s:
            letters[i]+=1
            if letters[i]==2:
                cnt +=2
                letters[i]=0
        return cnt+1 if cnt<len(s) else cnt
                
            

            