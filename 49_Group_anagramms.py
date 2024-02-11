from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_dict = defaultdict(list)
        for anagram in strs:
            anagrams_dict[''.join(sorted(anagram))].append(anagram)
        return list(anagrams_dict.values())
c