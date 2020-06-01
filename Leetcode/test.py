from heapq import heappop, heappush, heapify 
  
min_heap = []
heapify(min_heap)

heappush(min_heap, 4)
heappush(min_heap, 2)
heappush(min_heap, 5)
heappush(min_heap, 7)

print(heappop(min_heap))
print(heappop(min_heap))
print(heappop(min_heap))
print(heappop(min_heap))

