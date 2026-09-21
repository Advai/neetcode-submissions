class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     sorted_s=sorted(s)
    #     sorted_t=sorted(t)
    #     if sorted_s==sorted_t:
    #         return True
    #     return False
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = count_s[s[i]]+1 if s[i] in count_s else 1
            count_t[t[i]] = count_t[t[i]]+1 if t[i] in count_t else 1
        return count_s == count_t