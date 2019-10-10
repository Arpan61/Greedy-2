# Time Complexity : O(time)
# Space Complexity :O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # alpha_count will have count of number of occurances of each task
        alpha_count = [0] * 26
        for a in tasks:
            alpha_count[ord(a) - ord('A')] += 1
        # we will sort so that when we see from reverse order we can club the tasks together
        alpha_count.sort()
        time = 0
        # while there are remaining tasks
        while (alpha_count[25] > 0):
            nCount = 0
            # for each slot which is of size n
            while (nCount <= n):
                # if there is no task then break
                if alpha_count[25] == 0:
                    break
                # if slab is below 26 and the we have task at 25 -nCOunt index then we will club it together and decrease its value
                if nCount < 26 and alpha_count[25 - nCount] > 0:
                    alpha_count[25 - nCount] -= 1
                # irrespective of task present or not, increase the time and ncount as in the case when there is no task, we will add idle time
                nCount += 1
                time += 1
            # sort the alpha_count so that in next iteration we can have tasks which can clubbed together
            alpha_count.sort()

        return time