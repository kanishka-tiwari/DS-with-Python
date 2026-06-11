#if user chooses Heap (illustration)

elif structure == "Heap":
    heap = []
    for element in parsed:
        try:
            heapq.heappush(heap, float(element))
        except ValueError:
            heapq.heappush(heap, element)
        if heap:
            smallest = heapq.heappop(heap)
            print(f"Popped smallest item: {smallest}")
            print(f"Heap after popping: {heap}")