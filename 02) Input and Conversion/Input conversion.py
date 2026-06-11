raw = input("Entre the data you want to be demonstrated: ")

print("\n Available data structures: List, Tuple, Set, Linked list, Stack, Queue, Graph, Heap, Recursion, Tree")
structure = input("\n Select a data structure to be demonstrated from the ones listed above: ")

parsed = []

for item in raw:
    try:
        parsed.append(int(item))
    except ValueError:  
        try:
            parsed.append(float(item))
        except ValueError:

                 parsed.append(item)