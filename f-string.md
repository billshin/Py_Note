### Python f-string（Formatted String Literal）教學

f-string 是 Python 3.6+ 提供的字串格式化方式，
特色是 直覺、可讀性高、效能好，是目前最推薦的寫法。

1️⃣ 基本概念

在字串前面加上 f，即可在 {} 中放入 變數或表達式
```
name = "Alice"
age = 30

msg = f"{name} is {age} years old"
print(msg)
```

輸出：
```
Alice is 30 years old
```
2️⃣ {} 裡可以放什麼？
變數
```
f"{name}"
```
運算
f"{1 + 2}"

函式
```
f"{len(name)}"
```
方法
```
f"{name.upper()}"
```
3️⃣ 格式化語法總覽
```
f"{value:format_spec}"
```

部分        |說明
---         |---
value	    |變數或表達式
:	        |格式分隔符
format_spec	|格式規則

format_spec |說明                  |範例
---         |---                   |---
d	        |整數格式（int）        |5d
f	        |浮點數格式（float）    |3.14f
(數字)      |字串格式（str）        |"hello"



4️⃣ 整數格式（int）
指定寬度（左補空白）
```
d = 5
f"{d:3d}"     # '  5'
```
左補 0（left pad）
```
f"{d:03d}"    # '005'
```

對齊方式
```
f"{d:<3d}"    # '5  '  左對齊
f"{d:>3d}"    # '  5'  右對齊（預設）
f"{d:^3d}"    # ' 5 '  置中
```

5️⃣ 浮點數格式（float）
小數位數
```
pi = 3.14159
f"{pi:.2f}"   # '3.14'
```

寬度 + 小數
```
f"{pi:6.2f}"  # '  3.14'
```

6️⃣ 字串格式（str）
寬度與對齊
s = "hi"
f"{s:5}"      # 'hi   '
f"{s:>5}"     # '   hi'
f"{s:^5}"     # ' hi  '

7️⃣ 常見實用範例
🔹 left pad（補 0）
```
order_id = 42
f"{order_id:06d}"   # '000042'
```

🔹 表格對齊輸出
```
for i in range(1, 4):
    print(f"{i:>3d} | value")
```

輸出：

  1 | value
  2 | value
  3 | value

🔹 金額顯示
```
price = 1234.5
f"${price:,.2f}"    # '$1,234.50'
```
8️⃣ 跳脫 {}（顯示大括號）
```
f"{{value}}"
```

輸出：
```
{value}
```
9️⃣ 常見錯誤
❌ 型別不符
d = "5"
f"{d:03d}"
# ValueError: Unknown format code 'd' for object of type 'str'


✔ 修正

f"{int(d):03d}"

🔟 與舊寫法比較
舊：format
"{:03d}".format(5)

新：f-string（推薦）
f"{5:03d}"
