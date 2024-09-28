"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Myra Ribeiro
ID:      169030590
Email:   ribe0590@mylaurier.ca
__updated__ = "2024-08-13"
-------------------------------------------------------
"""
# Imports
# Constants


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListSet:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current:
            if current.value == value:
                return  # Value already exists, no duplicates in set
            if not current.next:
                break
            current = current.next
        current.next = Node(value)

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def delete(self, value):
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return "{" + ", ".join(map(str, values)) + "}"


# Example usage:
linked_list_set = LinkedListSet()
