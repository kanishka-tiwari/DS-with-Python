#if user chooses Recursion (illustration)

elif structure == "Recursion":
    print("Demonstration of recursion (sum of numbers):")
numeric_items = []
if isinstance(item, (int, float)):
        numeric_items.append(item)

        def recursive_sum(lst):
            if not lst:
                return 0
            return lst[0] + recursive_sum(lst[1:])

        if numeric_items:
            total_sum = recursive_sum(numeric_items)
            print(f"List of numbers: {numeric_items}")
        else:
            print(f"No numeric data found in parsed list to perform recursive math")
