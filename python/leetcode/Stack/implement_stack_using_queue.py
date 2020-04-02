# https://leetcode.com/problems/implement-stack-using-queues/submissions/

class MyStack:

    def __init__(self):
        self.queue = MyQueue()


    def push(self, x: int) -> None:
        self.queue.push_to_back(x)


    def pop(self) -> int:
        element = None
        new_queue = MyQueue()
        while not self.queue.is_empty():
            element = self.queue.pop_from_front()

            if not self.queue.is_empty():
                new_queue.push_to_back(element)

        self.queue = new_queue
        return element


    def top(self) -> int:
        element = None
        new_queue = MyQueue()
        while not self.queue.is_empty():
            element = self.queue.pop_from_front()
            new_queue.push_to_back(element)

        self.queue = new_queue

        return element


    def empty(self) -> bool:
        return self.queue.is_empty()

class MyQueue:

    def __init__(self):
        self.elements = []
        

    def push_to_back(self, x: int) -> None:
        self.elements.append(x)
        

    def pop_from_front(self) -> int:
        return self.elements.pop(0)
        

    def size(self) -> int:
        return len(self.elements)
        

    def is_empty(self) -> bool:
        return self.elements == []
