#if user chooses Queue (illustration)

elif structure == "Queue":
    queue = deque()
    for elements in parsed:
        queue.append(elements)
        print(f"Demonstration of Queue after enqueing: list{queue}")
        
        if queue:
            removed_item = queue.popleft()
            print(f"Dequeued item: {removed_item}")
            print(f"Demonstration of Queue after dequeuing: list{queue}")
        else: 
            print("Queue is empty")