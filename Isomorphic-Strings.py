class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h = {}
        h2 = {}

        for i in range(len(s)):
            x, y = s[i], t[i]
            
            if x not in h:
                h[x] = y
            if y not in h2:
                h2[y] = x
            if h[x] != y or h2[y] != x:
                return False
        return True


        # map1 = []
        # map2 = []
        # for idx in s:
        #     map1.append(s.index(idx))
        # for idx in t:
        #     map2.append(t.index(idx))
        # if map1 == map2:
        #     return True
        # return False

        