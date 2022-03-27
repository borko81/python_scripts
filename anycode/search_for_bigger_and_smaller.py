import heapq
import random

shuf_list = list(random.randint(-100, 100) for _ in range(10))
print(shuf_list)
print(heapq.nlargest(3, shuf_list))
print(heapq.nsmallest(3, shuf_list))