class Solution:
    def openLock(self, deadends: str, target: str) -> int:


        def plusOne(s,j):
            num = list(s)

            if num[j] == '9':
                num[j] == '0'
            else:
                num[j] = str(int(num[j]) + 1)

            return ''.join(num)

        def minusOne(s,j):
            num = list(s)

            if num[j] == '0':
                num[j] == '9'
            else:
                num[j] = str(int(num[j]) - 1)

            return ''.join(num)

        

        visited = set()
        visited.add('0000')

        deads = set(deadends)

        step = 0
        queue = ['0000']

        while (len(queue)!= 0):

            for i in range(len(queue)):
                curr = queue.pop()

                if curr in deads:
                    continue

                if curr in target:
                    return step
                    
                for j in range(0,4):

                    up = plusOne(curr,j)

                    if up not in visited:
                        visited.add(up)
                        queue.append(up)

                    down = minusOne(curr,j)
                    if down not in visited:
                        visited.add(down)
                        queue.append(down)

            step += 1
    

        return -1