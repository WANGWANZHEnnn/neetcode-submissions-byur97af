import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []

        for p in points:
            distance_sq = p[0]**2 + p[1]**2
            dis.append((distance_sq, p))
            
        heapq.heapify(dis)

        result = []
        for _ in range(k):
            dist, point = heapq.heappop(dis)
            result.append(point)
        return result




            
        







        