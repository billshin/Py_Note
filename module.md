### Module 模組

模組是一個包含程式的檔案（.py）或文件夾（包）

### Import 匯入模組方式
使用 import 指令導入模組
可以使用 as 指令重新命名模組

引用整個模組
import {module_name} as m

```python
import random as rd

print(rd.randint(1,10))
```

只引用模組中的指定程式
from {module_name} import {program_name} as p
```python
from random import randint as rdint

print(rdint(1,10))
```

Tips!
> dir() 可以列出模組中所有宣告

### 時間模組


```python
import datetime

# 常用的 datetime 用法示範

# 1. 獲取當前日期和時間
now = datetime.datetime.now()
print("當前時間:", now)

# 2. 創建特定的日期時間
specific_time = datetime.datetime(2023, 12, 25, 10, 30, 0)
print("特定時間:", specific_time)

# 3. 格式化日期時間為字串
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("格式化時間:", formatted)

# 4. 從字串解析日期時間
date_string = "2023-12-25 10:30:00"
parsed = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("解析時間:", parsed)

# 5. 使用 timedelta 進行時間運算 - 加上相對時間
tomorrow = now + datetime.timedelta(days=1 , hours=2, minutes=30)
print("時間相加:", tomorrow)


# 6. 獲取日期部分
today = datetime.date.today()
print("今天日期:", today)

# 7. 時間差計算 - 直接兩個時間相減
time_diff = specific_time - now
print("時間差:", time_diff)

# 8. 獲取年、月、日等組件
print("年:", now.year)
print("月:", now.month)
print("日:", now.day)
print("時:", now.hour)
print("分:", now.minute)
print("秒:", now.second)
```

