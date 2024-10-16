from typing import List
def insertion_sort(nums:List[int]):
    size = len(nums)
    for i in range(1,size):
        key = nums[i]
        j = i - 1 
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j-=1
        key, nums[j+1] = nums[j+1],key

class Student:
    def __init__(self,name,grade) -> None:
        self.name = name
        self.grade = grade

    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, value):
        if value > 100:
            return ValueError("Grade must be between 0 to 100...")
        self.__grade = value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == " ":
            return ValueError("Name can't be empty...")
        self.__name = value

    def __gt__(self,other):
        return self.__grade > other.__grade
    
    def __repr__(self) -> str:
        return f"{self.__name} : {self.__grade}"

# s1 = Student("Bob",98); s2 = Student("Jack", 10); s3 = Student("Ann", 45); s4 = Student("Josh", 90); s5 = Student("Tylor", 38)

# students = [s1,s2,s3,s4,s5]
# insertion_sort(students)
# print(students)
import random,time

def insertion_sort2(nums:List[int]):
    size = len(nums)
    for i in range(1,size):
        key = nums[i]
        j = i-1
        flag = False
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j-=1
            flag = True
        if flag:
            key, nums[j+1] = nums[j+1],key

ls = [random.randint(0,100) for i in range(20000)]
# ls = [i for i in range(2000000)]

# print(ls)
start = time.perf_counter()
insertion_sort2(ls)
end = time.perf_counter()
print(f"Time for insertion sort: {round(end - start, 6)} seconds")



