class Solution:
    def coloredCells(self, n: int) -> int:
        # colored = 1
        # for i in range(1,n):
        #     colored += 4 * i
        # return colored

        # New Math Intuition cur values square + before value's square 1, 4, 9, 16, 25

        return n ** 2 + ((n-1) ** 2)
