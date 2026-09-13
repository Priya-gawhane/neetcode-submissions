class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            count = [0] * 26

            for ch in word:
                index = ord(ch) - ord('a')
                count[index] += 1

            key = tuple(count)

            if key not in seen:
                seen[key] = []

            seen[key].append(word)

        return list(seen.values())