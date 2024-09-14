class Stack:
    """
    Implements a stack data structure with a push() function, pop() function,
    and support for len(). Internally, a list is used to store the stack items.
    """

    """
    Creates a list to hold the items.
    """
    def __init__(self, items: list = []):
        self.items = items
    
    """
    Adds an item to the stack and returns the new list length.
    """
    def push(self, *args):
        self.items.append(args)

        return len(self.items)
    
    """
    Removes an item from the stack and returns it.
    """
    def pop(self):
        return self.items.pop()
    
    """
    Gives the number of items in the stack.
    """
    def __len__(self):
        return len(self.items)