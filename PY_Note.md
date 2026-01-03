# python 閱讀筆記

### 註解方式

- 單行註解 #    :使用#開頭
- 多行註解 """  :使用""" 上下行包圍

### 區塊範圍

由於python強烈使用位置定義區塊

過長程式碼

> 換行可以使用 '\'
> 或是利用運算子 ex AND

過短程式碼

> 使用分號 ; 串聯前後段

### 宣告

使用方式

1. 變數名稱 = 值
   (不像其他語言,變數名稱前方需要加入定義 let var string 等....)
2. 變數1 , 變數2 = 值1 ,值2

### 型態 Type

- 數值型別：int, float, complex - 用於表示整數、浮點數和複數
- 字串：str - 用於表示文字資料
- 浮點數: float - 用於表示小數點數值 
- 布林：bool - 用於表示真或假 ,使用True和False
- 列表：list - 可變的有序集合 ,使用[]
- 元組：tuple - 不可變的有序集合 ,使用()
- 字典：dict - 鍵值對的集合 ,使用{}
- 集合：set - 無序且不重複的元素集合 ,使用{}
- 空值：None - 表示空值或無值 

- 檢查型態: type(變數)
  type(var_a)
- 小數處理, 使用Decimal
  Decimal(str(value))

Q: WHY Decimal 不能直接是數字?
A: 因為直接輸入浮點數會不精準

```python
from decimal import Decimal, ROUND_HALF_UP
Decimal(10.1)     #10.099999999
Decimal("10.1")   #10.1
```

### VSCode 型態檢查

vscode 直接使用 Pylance

宣告時候直接附帶型態, 錯誤型態直接報錯
![Image](/Image/pyright2.png)

### 型態檢查 isinstance

isinstance(10, int)      # True
isinstance("hello", str) # True
isinstance(10, str)      # False

### 轉型

int()    # 轉為整數，例如 int('123') -> 123
str()    # 轉為字串，例如 str(123) -> '123'
float()  # 轉為浮點數，例如 float('3.14') -> 3.14
bool()   # 轉為布林，例如 bool(0) -> False
list()   # 轉為列表，例如 list('abc') -> ['a', 'b', 'c']
tuple()  # 轉為元組，例如 tuple([1,2,3]) -> (1,2,3)
dict()   # 轉為字典，例如 dict([('a',1),('b',2)]) -> {'a':1, 'b':2}
set()    # 轉為集合，例如 set([1,2,2,3]) -> {1,2,3}

### 直接運算

進入pyhton後
`>>>` 可以直接運算數學

###　運算子

#### 算術運算子

`+`   # 加法：5 + 3 = 8
`-`   # 減法：5 - 3 = 2
`*`   # 乘法：5 * 3 = 15
`/`   # 除法（浮點數）：5 / 2 = 2.5
`//`  # 整數除法（地板除法）：5 // 2 = 2
`%`   # 模數（餘數）：5 % 2 = 1
`**`  # 指數：2 ** 3 = 8

#### 比較運算子

`==`  # 等於：5 == 5 = True
`!=`  # 不等於：5 != 3 = True
`<`   # 小於：3 < 5 = True
`>`   # 大於：5 > 3 = True
`<=`  # 小於等於：3 <= 5 = True
`>=`  # 大於等於：5 >= 5 = True

#### 邏輯運算子

`and` # 且：True and False = False
`or`  # 或：True or False = True
`not` # 非：not True = False

#### 位運算子

`&`   # 位元 AND：5 & 3 = 1
`|`   # 位元 OR：5 | 3 = 7
`^`   # 位元 XOR：5 ^ 3 = 6
`~`   # 位元 NOT：~5 = -6
`<<`  # 左移：5 << 1 = 10
`>>`  # 右移：5 >> 1 = 2

#### 賦值運算子

`=`   # 賦值：x = 5
`+=`  # 加法賦值：x += 3  # x = x + 3
`-=`  # 減法賦值：x -= 3  # x = x - 3
`*=`  # 乘法賦值：x *= 3  # x = x * 3
`/=`  # 除法賦值：x /= 3  # x = x / 3
`//=` # 整數除法賦值：x //= 3  # x = x // 3
`%=`  # 模數賦值：x %= 3  # x = x % 3
`**=` # 指數賦值：x **= 3  # x = x ** 3

#### 成員運算子

`in`      # 在序列中：'a' in 'abc' = True
`not in`  # 不在序列中：'d' not in 'abc' = True

#### 身份運算子

`is`      # 是同一個物件：x is y
`is not`  # 不是同一個物件：x is not y

### 縮排規則

- python 不像其他程式語言使用{}包覆範圍,而是使用tab縮排
- 通常於:之後進行縮排

pass # 空指令 , 如果尚未實作 ,可以先使用pass


```python
if True:
   pass 
```

### if 條件

```python
a:int = 4
b:float = 4.0
if a > b:
    print("a > b")
elif a == b:
    print("a == b")  
else:
    print("a < b")
print("Done")
```

### 三元運算

result = value1 if condition else value2


```python
a:int = 4
b:float = 4.0   
print("a > b") if a > b else print("a < b")


```


### 迴圈 for & while

for 迴圈
其中 enumerate 列舉 可以取得List中的 index 與 value

```python
for str in "python": # p,y,t,h,o,n
    print(str)
print("-----")
for num in range(5): # 0,1,2,3,4
    print(num)
print("-----")
for num in range(5,10):  # 5,6,7,8,9 
    print(num)
print("-----")
for num in range(5,10,2): # 5,7,9
    print(num)
print("-----")

list1 = [10,20,30,40,50]
for i , val in enumerate(list1): # (0,10),(1,20),(2,30),(3,40),(4,50)
    print(i,val)
```

while

```python
num = 0
while num < 10:
    print(num)
    num += 1
```

### Random

```python
import random
print(random.randint(1,10))
```

### 陣列相關

- List : 動態陣列 , 適合存放不確定數量的資料
- Tuple : 靜態陣列, 適合存放確定數量的資料 , 且資料不可更改

存取list 與 tuple

```python
list1 = [10,20,30,40,50]
print(list1[0]) # 10
print(list1[-1]) # 50
print(list1[1:]) # [20,30,40,50]  
print(list1[:3]) # [10,20,30]
print(list1[1:3]) # [20,30]
```

```python
tuple1 = (10,20,30,40,50)
print(tuple1[0]) # 10
```

陣列存取方式

# Python `list` 常用操作方法速查表

#### 1️⃣ 新增元素

| 方法               | 說明                 | 範例                           |
| ------------------ | -------------------- | ------------------------------ |
| `append(x)`        | 尾端新增單一元素     | `a.append(3)`→`[1,2,3]`       |
| `extend(iterable)` | 尾端展開新增多個元素 | `a.extend([3,4])`→`[1,2,3,4]` |
| `insert(i, x)`     | 指定位置插入元素     | `a.insert(1, 99)`→`[1,99,2]`  |

#### 2️⃣ 刪除元素

| 方法        | 說明                                   | 範例                          |
| ----------- | -------------------------------------- | ----------------------------- |
| `pop([i])`  | 移除並回傳指定位置元素（預設最後一個） | `a.pop()`→`4`，a →`[1,2,3]` |
| `remove(x)` | 移除第一次出現的指定元素               | `a.remove(2)`→`[1,3]`        |
| `clear()`   | 清空 list                              | `a.clear()`→`[]`             |

#### 3️⃣ 查找 / 計數

| 方法                       | 說明               | 範例              |
| -------------------------- | ------------------ | ----------------- |
| `index(x[, start[, end]])` | 回傳第一次出現索引 | `a.index(2)`→`1` |
| `count(x)`                 | 計算元素出現次數   | `a.count(2)`→`1` |

index 像是 C#的 IndexOf 方法
#### 4️⃣ 排序 / 反轉
| 方法                            | 說明                           | 範例                                 |
| ------------------------------- | ------------------------------ | ------------------------------------ |
| `sort()` | 原地排序                       | `a.sort()`→`[1,2,3]`                |
| `sorted(a)`                     | 回傳排序後新 list，不改原 list | `sorted(a, reverse=True)`→`[3,2,1]` |
| `reverse()`                     | 原地反轉                       | `a.reverse()`→`[3,2,1]`             |

#### 5️⃣ 複製 / 合併
| 方法     | 說明                      | 範例                         |
| -------- | ------------------------- | ---------------------------- |
| `copy()` | 複製 list（shallow copy） | `b = a.copy()`               |
| `+`      | 合併 list，產生新 list    | `[1,2] + [3,4]`→`[1,2,3,4]` |
| `*`      | 重複元素                  | `[0] * 3`→`[0,0,0]`         |

---

#### 6️⃣ 其他操作
| 方法                    | 說明           | 範例                       |
| ----------------------- | -------------- | -------------------------- |
| `len(a)`                | list 長度      | `len([1,2,3])`→`3`        |
| `in`                    | 判斷是否存在   | `2 in [1,2,3]`→`True`     |
| `not in`                | 判斷是否不存在 | `5 not in [1,2,3]`→`True` |
| 切片`a[start:end:step]` | 取子序列       | `a[0:2]`→`[1,2]`          |

---

#### 7️⃣ 與迭代相關
| 方法 / 方式    | 說明              | 範例                           |
| -------------- | ----------------- | ------------------------------ |
| `enumerate(a)` | 迭代同時取得索引  | `for i,v in enumerate(a): ...` |
| `zip(a,b)`     | 同時迭代多個 list | `for x,y in zip(a,b): ...`     |

# Python `list` 常用操作方法速查表

## 1️⃣ 新增元素
| 方法               | 說明                 | 範例                           |
| ------------------ | -------------------- | ------------------------------ |
| `append(x)`        | 尾端新增單一元素     | `a.append(3)`→`[1,2,3]`       |
| `extend(iterable)` | 尾端展開新增多個元素 | `a.extend([3,4])`→`[1,2,3,4]` |
| `insert(i, x)`     | 指定位置插入元素     | `a.insert(1, 99)`→`[1,99,2]`  |

## 2️⃣ 刪除元素


| 方法        | 說明                                   | 範例                          |
| ----------- | -------------------------------------- | ----------------------------- |
| `pop([i])`  | 移除並回傳指定位置元素（預設最後一個） | `a.pop()`→`4`，a →`[1,2,3]` |
| `remove(x)` | 移除第一次出現的指定元素               | `a.remove(2)`→`[1,3]`        |
| `clear()`   | 清空 list                              | `a.clear()`→`[]`             |




### 字串處理方式
| 方法              | 說明                   | 範例                           |
| ----------------- | ---------------------- | ------------------------------ |
| `split()`         | 切割字串               | `a = '1,2,3'.split(',')`→`['1','2','3']` |
| `join(iterable)`  | 連接字串               | `','.join(['1','2','3'])`→`'1,2,3'` |
| `replace(old,new)` | 替換字串               | `'abc'.replace('a','A')`→`'Abc'` |
| `strip(chars)`    | 去除字串前尾空白符號(trim) | `'   abc   '.strip() `→`'abc'` |
| `format(...)`     | 格式化字串             | `'{0} {1}'.format('a','b')`→`'a b'` |
| `find()`          | 搜尋字串               | `'abc'.find('b')`→`1` |
| `rfind()`         | 反向搜尋字串           | `'abc'.rfind('b')`→`1` |
| `count()`         | 計算字串出現次數         | `'abc'.count('b')`→`1` |
| `startswith()`    | 判斷是否以指定字串開頭 | `'abc'.startswith('a')`→`True` |
| `endswith()`      | 判斷是否以指定字串結尾   | `'abc'.endswith('c')`→`True` |

join 非 string list 無法使用

### Unpacking

適用於 list / tuple / string / range

1. 基本 unpacking

```python
a, b = [1, 2]
左右數量必須相同
```

2. 交換變數

```python
a, b = b, a
```

3. 使用 *（extended unpacking）

*僅能出現一次
```python
a, *rest = [1, 2, 3]
# a=1, rest=[2,3]

*head, b = [1, 2, 3]
# head=[1,2], b=3

a, *mid, b = [1, 2, 3, 4]
# mid=[2,3]
```

4. for-loop unpacking

迴圈中使用, 每次loop 都解包到前方指定變數

```python
for a, b in [(1, 2), (3, 4)]:
    pass
```

### Copy

使用 = 的時候要小心, 大部分都是shallow copy
假設物件有獨立性, 務必使用 deepcopy

| 狀況 | 外層容器 | 內層元素 | 結果 |
|------|----------|----------|------|
| b = a | 無 | 無 | 完全共用（不是 copy） |
| b = a[:] | 新 | 共用 | Shallow copy |
| b = list(a) | 新 | 共用 | Shallow copy |
| b = dict(a) | 新 | 共用 | Shallow copy |
| b = set(a) | 新 | 共用 | Shallow copy |
| b = copy.copy(a) | 新 | 共用 | Shallow copy |
| [x for x in a] | 新 | 共用 | Shallow copy |
| copy.deepcopy(a) | 新 | 新 | Deep copy |

```python
import copy

a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]

a = [1, [2, 3], 4]

# Shallow copy
b = copy.copy(a)
b[1].append(99)
print(a)  # [1, [2, 3, 99], 4] → 內層 list 共用
print(b)  # [1, [2, 3, 99], 4]

# Deep copy
c = copy.deepcopy(a)
c[1].append(100)
print(a)  # [1, [2, 3, 99], 4] → 不變
print(c)  # [1, [2, 3, 99, 100], 4]
```

### 字典 dict

無序結構,不會有數字索引

基本宣告{key:value}
讀取使用[key]
先宣告key 使用{}.fromkeys(list)

```python
# 宣告
d = {'a': 1, 'b': 2}
d['c'] = 3
print(d)  # {'a': 1, 'b': 2, 'c': 3}
# 使用
print(d['a'])  # 1

# zip 後對應 > dict  
# 適合將2個長度一樣的list 結合成dict , 例如CSV
list1 = ["name", "age", "email"]
list2 = ["Tom", 35, "tom@test.com"]

result = dict(zip(list1, list2))

# 先宣告key
dt ={}.fromkeys(list1)
print(dt)  # {'name': None, 'age': None, 'email': None}

# 查詢Key是否存在 (但key不存在會error)
key in dt

# 使用get 查詢
dt.get('name')
# - 有找到: 返回value
# - 找不到: 返回None
# get()結果使用 is None判斷

if dt.get('name') is None:
    print('not found')
    else:
        pass


``` 

# 查詢value是否存在
value in dt.values()

```python
# 刪除key
del dt['name']
# 清空
dt.clear()
```

字典方法
方法 | 說明 | 備註 |
|------|----------|------|
| keys() | 返回所有的 key |
| values() | 返回所有的 value |
| items() | 返回所有的 (key, value) 元组 |
| clear() | 清空字典 |
| get() | 返回指定 key 的 value, 如果 key 不存在, 返回None | 使用is None判斷


### Sets Forzenset 集合

只在乎「存不存在」、不要順序、不要重複 → 用 set

無序結構,不會有數字索引
基本宣告{value}
內容不可重複


類別             | 說明       | 當作字典的key| 當作另一個set的成員 |
|------         |----------  |------        | ------|
| set()         | 空集合      | No         | No |
| frozenset()   | 不可變集合  | Yes        | Yes |


```python
# 宣告
s = {1, 2, 3}
s.add(4) # {1, 2, 3, 4}
s.remove(2) # {1, 3, 4}
s.discard(2) # {1, 3, 4}

# 查詢 in
print(3 in s)  # True
print(3 not in s)  # False

 #宣告空frozenset
_frozenset = set() # 而不是{},會被判斷為空dict

#將List去重複
Remove_duplicate = set(List) 

```

方法 | 說明 | 備註 |
|------|----------|------|
| add() | 添加元素 | |
| remove() | 移除元素 | 不存在會error ,也適合判斷|
| discard() | 移除元素 | 無論有無,不會error |
| clear() | 清空集合 | |


### 集合計算

暫不研究
