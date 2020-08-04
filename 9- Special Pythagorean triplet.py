class Solution:
    def solve(self):
        for a in range(100, 1000):
            for b in range(a+1, 1000):
                csq = a**2 + b**2
                c = csq**0.5
                
                if a + b + c == 1000:
                    print(a*b*c)
                    break
                
obj = Solution()
obj.solve()
