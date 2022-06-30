from collections import deque
class Solution:
    def openLock(self, deadends: str, target: str) -> int:

        if target == '0000':
            return -1

        visited = set(deadends)
        q = deque() 
        q.append(["0000",0])

        # step = 0

        def childrens(self, curr):
            res = []
            for j in range(4):
                var = ((int(curr[j]) + 1) % 10 )
                res.append(curr[:j] + str(var) + curr[j+1:])
                
                var = ((int(curr[j]) - 1 + 10) % 10 )
                res.append(curr[:j] + str(var) + curr[j+1:])

            return res


        while q:
            curr, steps = q.popleft()
            if curr == target:
                return steps
            for child in childrens(curr):
                if child not in visited:
                    visited.add(child)
                    q.append(child,steps+1)
        
        return -1
