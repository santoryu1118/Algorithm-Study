from typing import Any
class FixedStack:

    class Empty(Exception):
        pass
    class Full(Exception):
        pass 

    def __init__(self, capacity:int=256)-> None:
        self.stack = [None]* capacity
        self.capacity = capacity
        self.ptr = 0
    
    def __len__(self)-> int:
        return self.ptr

    def size(self)->int:
        return len(self)

    def is_empty(self)-> bool:
        #시작 ptr = 0
        return self.ptr <= 0

    def is_full(self)-> bool:
        #마지막 인자는 ptr-1, 마지막 값 넣어주면 ptr == capacity
        return self.ptr >= self.capacity

    def push(self, value: Any)->None:
        if self.is_full():
            raise FixedStack.Full
        self.stack[self.ptr] = value
        self.ptr +=1
    
    def pop(self)->Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -=1
        return self.stack[self.ptr]
    
    def top(self)->Any:
        if self.is_empty():
            raise FixedStack.Empty

        return self.stack[self.ptr-1]


