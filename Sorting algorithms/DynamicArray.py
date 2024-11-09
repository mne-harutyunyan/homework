from typing import Any, Iterator
class DynamicArray:
    def __init__(self, capacity: int = 10) -> None:
        self.size_of_array = 0  
        self.__capacity = capacity  
        self.__array = [None] * self.__capacity
    def __str__(self) -> str:
        return f"{self.__array}"
    def __repr__(self) -> str:
        return f"DynamicArray({self.__array})"
    def append(self, item):
        if self.size_of_array == self.__capacity:
            self.resize(self.__capacity*2)
        self.__array[self.size_of_array] = item
        self.size_of_array += 1

    def resize(self, new_capacity):
        new_array = new_capacity * [None]
        for i in range(self.size_of_array):
            new_array[i] = self.__array[i]
        self.__array = new_array
        self.__capacity = new_capacity

    def __setitem__(self, index: int, value: Any) -> None:
        if index < 0:
            raise IndexError("Index can't be negative.")
        if index > self.size_of_array:
            raise IndexError("Index is out of range.")
        self.__array[index] = value
        self.size_of_array += 1

    def __getitem__(self, index: int) -> Any:
        if index < 0:
            raise IndexError("Index is out of range")
        return self.__array[index]
    def __len__(self) -> int:
        return self.size_of_array
    
    def __add__(self, other: 'DynamicArray') -> 'DynamicArray':
        result = DynamicArray((self.size_of_array + other.size_of_array))
        for i in range(self.size_of_array):
            result[i] = self.__array[i]
        for j in range(other.size_of_array):
            result[self.size_of_array+j] = other.__array[j]
        return result
    def __iadd__(self, other: 'DynamicArray') -> 'DynamicArray':
        for item in other:
            self.__array.append(item)
        return self
    
    def __ne__(self, other: 'DynamicArray') -> bool:
        if self.size_of_array != other.size_of_array:
            return True
        for i in range(self.size_of_array):
            if self.__array[i] != other.__array[i]:
                return True
        return False

    def __eq__(self, other: 'DynamicArray') -> bool:
        if self.size_of_array != other.size_of_array:
            return False
        for i in range(self.size_of_array):
            if self.__array[i] != other.__array[i]:
                return False
        return True

    def __lt__(self, other: 'DynamicArray') -> bool:
        min_len = min(self.size_of_array, other.size_of_array)
        for i in range(min_len):
            if self.__array[i] < other.__array[i]:
                return True
            elif self.__array[i] > other.__array[i]:
                return False
        return self.size_of_array < other.size_of_array

    def __le__(self, other: 'DynamicArray') -> bool:
        min_len = min(self.size_of_array, other.size_of_array)
        for i in range(min_len):
            if self.__array[i] < other.__array[i]:
                return True
            elif self.__array[i] > other.__array[i]:
                return False
        return self.size_of_array <= other.size_of_array

    def __gt__(self, other: 'DynamicArray') -> bool:
        return not self.__le__(other)

    def __ge__(self, other: 'DynamicArray') -> bool:
        return not self.__lt__(other)
    
    def __hash__(self) -> int:
        raise TypeError('''Unhashble type: "DynamicArray"''')
    
    def __iter__(self) -> Iterator[Any]:
        self.index = 0
        return self
    
    def __next__(self) -> Any:
        if self.index < self.size_of_array:
            result = self.__array[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# examples
d = DynamicArray(3)
d[0] = 1
d[1] = 2
d[2] = 2

b = DynamicArray(3)
b[0] = 1
b[1] = -5
b[2] = 2

# st = {b,d}

d.append(7)
it = iter(d)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
d.append("hello")
d.append("hello")
d.append("hello")

print(d)


