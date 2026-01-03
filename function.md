### Function

函數宣告

```python
def function_name (args):
  #do something
  return
```

多參數收納
參數可以是 *tuple_arg / **dict_kwargs
但帶*的參數只能存在一次, 可以於參數的前中後分別使用

- tuple_arg 收的是 一串值 , 所以arg 只要是值就好  , 常用於收集參數
- dict_kwargs 收的是 key-value, arg 必須是 key = value ,常用於

```python
def input_tuple_arg (*tuple_arg ):
    print(tuple_arg)

def input_dict_kwargs (**dict_kwargs ):
    print(dict_kwargs)

input_tuple_arg(1, 2, 3, 4)
input_dict_kwargs(a=1, b=2, c=3)

# 向下傳遞多參數
def wrapper(**kwargs):
    return real_func(**kwargs)


```    

### Lambda Function

重點: Lambda 只能是一行

lambda 函数通常与内置函数如 map()、filter() 和 reduce() 一起使用，以便在集合上执行操作。例如：

func | 說明
--- | ---
map | 對集合中的每个元素执行一个函数
filter | 过滤集合中的元素

```python
from functools import reduce

lambda arg1, arg2: arg1 + arg2

cal = lambda x, y: x + y
cal(1, 2)

# map - 列舉
map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#filter - 
filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# [2, 4, 6, 8, 10]

```
