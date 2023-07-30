class Stack:
    def __init__(self):
        self.items = []


    def push(self, item):
        self.items.append(item)


    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Error"


    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Error"


    def is_empty(self):
        return len(self.items) == 0


    def __str__(self):
        return " ".join(str(item) for item in self.items)[::-1]


    def __len__(self):
        return len(self.items)


    def list_items(self):
        return self.items
