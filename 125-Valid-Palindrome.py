class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ''.join(i for i in s if i.isalnum()).lower()
        print(newstr)
        print(newstr[::-1])
        return newstr[::-1] == newstr








    ## string -> remove spl characters  -> all upper to lower 
        