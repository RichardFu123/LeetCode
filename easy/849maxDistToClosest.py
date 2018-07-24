class Solution(object):
    def maxDistToClosest(self, seats):
        ans = 0
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K+1)/2)

        return int(max(ans, seats.index(1), seats[::-1].index(1)))
