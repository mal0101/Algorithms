# this is another leetcode problem in which the binary search algorithme is used to find the square root of a number x
# reminder : the square root of a number x is the number y such that y * y = x
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x  # 0 and 1 are their own square roots

        left, right = 2, x // 2

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
