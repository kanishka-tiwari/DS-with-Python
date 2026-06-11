#if user chooses Stack (illustration)

elif structure == "Stack":  
    stack = []
    for element in parsed:
        stack.append(element)
    print(f"Demonstration of Stack after pushing: {stack}")

    if stack: 
        removed_item = stack.pop()
        print(f"LIFO: {removed_item}")
        print(f"Stack after popping: {stack}")
    else:
        print("Stack is empty")