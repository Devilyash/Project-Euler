#Seive of Eratosthenes
class Solution:
    def solve(self, n):
        sum = 0
        dp = [1] * n
        for i in range(2,n):
            if dp[i]:
                sum += i
                for j in range(i*i, n, i):
                    dp[j] = 0
        print(sum)
                
obj = Solution()
obj.solve(2000000)
