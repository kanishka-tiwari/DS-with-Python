import ast
import heapq

from collections import deque

#blueprint

class node: 
    def __init__(self, data):
        self.data = data
        self.next = None

#blueprint of tree

class treenode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#blueprint of linked list

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
            last.next = new_node

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(f"[{current.data}]")
            current = current.next
        return " -> ".join(elements) + "-> None"