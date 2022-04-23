import math
import heapq

heap = []
array = [1,2,3,4]
heapq.heappush(heap,array[3])
heapq.heappush(heap,array[2])
heapq.heappush(heap,array[1])
print(heap)