class Solution:
    def numSquares(self, n: int) -> int:
        # Creating a list of all the squares below square root of n (say n = 36)
        #  the list will contain 1, 2, 3, 4, 5, 6, 7
        square_nums = [ i * i for i in range(1,int(n**0.5)+1)]

        level = 0 #To determine at which level we are in the BFS
        queue = {n} # A set is defined 

        while queue: # Till the queue has elements in it
            level += 1 # Increasing the level

            next_queue = set() #Define another set to replace queue with the updated (n - square_Value)

            for remainder in queue: #Getting each element of queue (only one element)
                for square_num in square_nums: #Traversing in the square_nums list and 
                    # if the number is equal to remainder then returning the count if it is less than square nums then breaking the loop
                    # else subtracting the square num from the remainder and adding it to the set and then replacing the queue with next_queue 
                    if remainder == square_num:
                        return level
                    elif remainder <square_num:
                        break
                    else:
                        next_queue.add(remainder-square_num)
            
            queue = next_queue

        return level

Myobject = Solution()
print(Myobject.numSquares(999))