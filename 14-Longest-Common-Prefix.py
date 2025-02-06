class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        print(strs)
        

        first = strs[0] #flight
        last = strs[-1] #flower
        minLength = min(len(first), len(last)) #6
        
        i = 0
        while i < minLength and first[i] == last[i]:
            i += 1
        return last[0:i]
        