class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return len(self.items) == 0
 
    def push(self, item):
        self.items.append(item)
 
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
 
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
 
    def size(self):
        return len(self.items)
def decimal_to_octal(decimal_num):
    stack = Stack()  # 建立一個空棧，用於存儲餘數

    while decimal_num > 0:
        remainder = decimal_num % 8  # 計算餘數
        stack.push(remainder)  # 將餘數推入棧中
        decimal_num = decimal_num // 8  # 更新商

    octal_str = ""
    while not stack.is_empty():
        octal_str += str(stack.pop())  # 彈出棧中的餘數，構建八進位字符串

    return octal_str


print(decimal_to_octal(233))  # 输出：'351'
