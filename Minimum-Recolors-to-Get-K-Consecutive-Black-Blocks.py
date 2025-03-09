class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        ans = float("inf")
        for i in range(len(blocks)):
            if i-k >= 0 and blocks[i-k] == 'B':
                count -= 1

            if blocks[i] == 'B':
                count += 1
            ans = min(ans,k - count)
        return ans
        