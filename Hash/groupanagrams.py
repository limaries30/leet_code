'''
https://leetcode.com/problems/group-anagrams/
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for i in strs:
            anagram = ''.join(sorted(i))
            if anagram in anagram_dict.keys():
                anagram_dict[anagram].append(i)
            else:
                anagram_dict[anagram]=[i]
        #ans = []
        # for i in anagram_dict.values():
        #     ans.append(i)
        return anagram_dict.values()