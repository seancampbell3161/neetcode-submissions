class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_split = list(s)
        t_split = list(t)
        s_split.sort()
        t_split.sort()
        pairs = list(zip(s_split, t_split))

        for t in pairs:
            if len(pairs) < max(len(s_split), len(t_split)) or t[0] != t[1]:
                return False
        return True