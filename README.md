# 期末報告-python堆疊實作進位轉換的範例詳解
## 簡述 
棧（Stack）是計算機科學中常用的資料結構,具有眾多實際應用,其中之一是使用棧來實現進制轉換,將一個數字從一種進製表示轉換為另一種進製表示,本文將深入研究棧的原理,以及如何使用Python實現十進位到二進制、八進制和十六進制的進制轉換。
- [目錄]
   - [了解進位轉換](#了解進位轉換)
   - [進位轉換原理](#進位轉換原理)
   - [範例1：十進位到二進位](#範例1十進位到二進位)
   - [使用堆疊進行進位轉換](#使用堆疊進行進位轉換)
   - [範例2：十進位到八進制](#範例2十進位到八進制)
   - [進制轉換的應用](#進制轉換的應用)
   - [結論](#結論)
## 了解進位轉換
在計算機科學和數學中，進制是一種表示數字的方式，它決定了一個數字的基數和表示規則。最常見的進位包括：  
* 十進制（Decimal）：基數為10，使用0-9這10個數字表示。  
* 二進位（Binary）：基數為2，使用0和1表示。  
* 八進位（Octal）：基數為8，使用0-7表示。  
* 十六進位（Hexadecimal）：基數為16，使用0-9和A-F表示。
 
每種進制都有其獨特的特點和應用場景。進位轉換是將數字從一種進位表示轉換為另一種進位表示的過程。在接下來的部分，我們將重點放在如何將十進制數轉換為其他進制。
## 進位轉換原理
進制轉換的核心原理涉及除法和取餘操作。具體步驟如下：  

* 從十進制數的最右邊開始，連續進行除法和取餘操作。
* 將每次取得的餘數儲存起來，它們構成了新進制下的數值。
* 將商數作為下一輪的被除數，直到商數為0為止。
* 將儲存的餘數依照相反的順序排列，得到新進制的表示。  

讓我們以一個範例來說明如何將十進制數轉換為二進制。
## 範例1：十進位到二進位
我們以十進制數 233 為例，將其轉換為二進制。  

* 用 2（二進位的基數）除以 233，得到商數 116 和餘數 1。
* 然後，將商數 116 除以 2，得到商數 58 和餘數 0。
* 繼續這個過程，直到商數為 0。
* 最後，將所有的餘數從下往上排列，得到二進位表示為 11101001。  

這個轉換過程可以輕鬆地使用堆疊來實作。
## 使用堆疊進行進位轉換
棧是一種理想的資料結構，用於實現進制轉換。我們可以將每次的餘數推入堆疊中，然後以相反的順序從堆疊中彈出這些餘數，從而獲得正確的進位表示。以下是使用Python堆疊實現十進位到二進位轉換的範例程式碼：  
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
    def decimal_to_binary(decimal_num):
    stack = Stack()  # 建立一個空棧，用於存儲餘數

    while decimal_num > 0:
        remainder = decimal_num % 2  # 計算餘數
        stack.push(remainder)  # 將餘數推入棧中
        decimal_num = decimal_num // 2  # 更新商

    binary_str = ""
    while not stack.is_empty():
        binary_str += str(stack.pop())  # 彈出棧中的餘數，構建二進位字符串

    return binary_str  
讓我們測試一下這個函數：  
  ```print(decimal_to_binary(233))  # 輸出：'11101001```  
  輸出結果:  
  
![01](https://github.com/Dopo2002/final_report/blob/main/%E8%BC%B8%E5%87%BA1.jpg)

這個函數使用堆疊來儲存餘數，並將它們按照正確的順序彈出以建立二進位表示。這個方法可以用於任何十進位到二進制的轉換。
## 範例2：十進位到八進制
現在，讓我們來看一個將十進制數轉換為八  
進制的範例。我們只需稍微修改上面的程式碼，將基數從2改為8：  
```
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
 ```
讓我們測試一下這個函數：  
  ```print(decimal_to_octal(233))  # 输出：'351'```  
輸出結果:  
![01](https://github.com/Dopo2002/final_report/blob/main/%E8%BC%B8%E5%87%BA2.jpg)   

這個函數使用堆疊來儲存餘數，並將它們按照正確的順序彈出以建立二進位表示。這個方法可以用於任何十進位到二進制的轉換。
## 進制轉換的應用
進制轉換不僅僅是一個有趣的數學概念，它在電腦科學和電腦程式設計中也有重要的應用。以下是一些應用範例：

* 電腦記憶體管理： 電腦記憶體中的資料通常以二進位形式儲存。進制轉換用於查看和理解記憶體中的資料。

* 網路通訊： 資料在電腦網路中以二進位傳輸。進制轉換有助於理解和解析網路資料包。

* 影像處理： 影像的像素值通常以不同的進位表示，進位轉換可用於修改影像的色彩深度等。

* 程式設計： 程式設計師可能需要在不同的進位之間進行轉換，以便理解和調試程式中的資料。

* 密碼學： 加密和解密演算法中使用了不同進位的數學操作，包括二進位和十六進位。

進制轉換是計算機科學中的一個基本概念，深入了解它將有助於更好地理解電腦系統的內部工作原理。
## 結論
棧是一個強大的資料結構，用於實現進制轉換等許多問題。透過深入理解堆疊的工作原理，您可以更好地理解它的應用，包括電腦記憶體管理、程式設計、網路通訊等領域。
