from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        discS = defaultdict(int)
        discT = defaultdict(int)


        for char in s:
            discS[char] +=1

        for char in t:
            discT[char] +=1

        if discS == discT:
            return True
        else:
            return False

