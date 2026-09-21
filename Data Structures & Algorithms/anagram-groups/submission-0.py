class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort by length
        # count letters for each word, each word with matching map gets added to list. Build for words of each length. 
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())