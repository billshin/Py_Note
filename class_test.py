
from dataclasses import dataclass

class Motor:
    def buildCar(self):
        print("Building a car")

# motor = Motor()
# motor.buildCar()

class TestClass:
    '''
    Docstring for TestClass
    '''
    #class下寫的註記 可以呼叫查看 print(class_test.TestClass.__doc__)
    def __init__(self ,name, age) -> None:
        self.name = name
        self.age = age
        self._speed = 0  # protected attribute
        print("Constructor called") 
        print(name)
       
    
    def display(self):
        print("Display method called" , self.name)


# 使用dataclass装饰器 , 自动生成初始化方法等
@dataclass
class DataClassExample:
    '''
    資料容器class範例
    具有自動生成的初始化方法
    '''
    id: int
    name: str

    def show(self):
        '''顯示參數'''
        print(f"ID: {self.id}, Name: {self.name}")