import math 

class Solution:
    def numSquares(self, n: int) -> int:
        
        while (n%4 == 0):
            n /= 4
        if (n % 8 ==7): #4**K*(8n + 7)
            return 4
        
        if (self.is_perfect(n)):
            return 1
        
        x = int(math.sqrt(n))
        for i in range(1, x + 1):  # sum of 2 perfect squares
            if self.is_perfect(n - i * i):
                return 2
        
        return 3
        
        
    def is_perfect(self, n):
        x = int(math.sqrt(n))
        return x * x == n