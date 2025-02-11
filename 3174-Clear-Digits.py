class Solution:
    def clearDigits(self, s: str) -> str:
        stacks = []
        for i in range(0, len(s)):
            if s[i].isdigit():
                stacks.pop()
            else:
                stacks.append(s[i])
        return "".join(stacks)