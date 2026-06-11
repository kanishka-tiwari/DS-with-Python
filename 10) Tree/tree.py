#if user chooses Tree (illustration)

elif structure == "Tree":
    print(f"Demonstration of Tree (BST):")

    def insert_bst(root, data):
        if root is None:
            return treenode(data)
        if str(data) < str(root.data):
            root.left = insert_bst(root.left, data)
        else:
            root.right = insert_bst(root.right, data)
        return root

    def inorder_traverse(root, result_list):
        if root:
            inorder_traverse(root.left, result_list)
            result_list.append(root.data)
            inorder_traverse(root.right, result_list)

if parsed:
    root_node = None
for element in parsed:
    root_node = insert_bst(root_node, element)
    
    sorted_elements = []
    inorder_traverse(root_node, sorted_elements)
    print(f"In order traversal of the built tree (sorted): {sorted_elements}")
else:
    print("No data available to construct a tree")

#note: make sure the blueprint of tree has been declared