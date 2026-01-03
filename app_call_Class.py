
import class_test 



motor = class_test.Motor()
motor.buildCar()


motor2 = class_test.Motor()
motor2.buildCar()

print(class_test.TestClass.__doc__)
test = class_test.TestClass("MyTest123",20)
test.display()
print(test.__dict__)
test.name = "NewName456"
test.display()
test._speed = 100  # 訪問protected屬性
print(test._speed)  # 訪問protected屬性


# 使用string 讀改屬性 (reflection 可以使用字串修改屬性)
print("----使用string 讀改屬性 (reflection 可以使用字串修改屬性)----")
attr_name = "name"
#hasattr() 看屬性
print(hasattr(test, attr_name))
#getattr() 讀屬性
print(getattr(test, attr_name))
#setatr() 改屬性
setattr(test, attr_name, "ChangedName789")
print(getattr(test, attr_name))
#delattr() 刪屬性
print(test.__dict__)
delattr(test, attr_name)
print(hasattr(test, attr_name))
print(test.__dict__)

data_instance = class_test.DataClassExample(id=1, name="ExampleName")
data_instance.show()