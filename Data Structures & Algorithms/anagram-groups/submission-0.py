from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            counts = [0] * 26
            for letter in word:
                position = ord(letter) - ord('a')
                counts[position] += 1

            key = tuple(counts)

            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())