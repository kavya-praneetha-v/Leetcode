class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s= s.strip()
        # cnt =0
        # for i in range(len(s) -1, -1, -1):
        #     if s[i]==\ \:
        #         break
        #     cnt +=1
        # return cnt

        s = s[::-1]
        s = s.strip()
        i = 0
        while i< len(s):
            if s[i] == \ \:
                break
            i += 1
        return i