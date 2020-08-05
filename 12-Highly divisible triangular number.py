import math
class Solution:
    def solve(self):
        n = 1
        for i in range(2,1000000):
            n += i
            j = 1
            lst = []
            while j <= int(math.sqrt(n)):
                if n%j == 0:
                    if (n//j) == j:
                        lst.append(j)
                    else:
                        lst.append(j)
                        lst.append(n//j)
                j = j + 1
            if len(lst) > 500:
                print(n)
                break
                
obj = Solution()
obj.solve()
#76576500
