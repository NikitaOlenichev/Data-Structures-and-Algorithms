# Лабораторная работа 3  
## Стек и очередь  

### Выполнил Оленичев Никита Романович, группа ИДБ-25-07  

### Базовая задача: Brackets  
### Вариативная часть: 3. Подсчитать количество пар скобок в строке: ([]) -> 2, ()[]{} -> 3  

### Класс Stack в котором реализована структура данных Стек

```python
class Stack:
    def __init__(self):
        # список для хранения элементов
        self.items = []

    def push(self, value):
        # добавление элемента в стек
        self.items.append(value)

    def pop(self):
        # удаление верхнего элемента
        if self.is_empty():
            print("Стек пуст")
            return None
        return self.items.pop()

    def peek(self):
        # просмотр верхнего элемента без удаления
        if self.is_empty():
            print("Стек пуст")
            return None
        return self.items[-1]

    def is_empty(self):
        # проверка, пуст ли стек
        return len(self.items) == 0

    def size(self):
        # количество элементов
        return len(self.items)
```

### Функция проверки строки с поддержкой (), {}, []

```python
def is_valid(line):
    stack = Stack()
    d_match = {')': '(', ']': '[', '}': '{'}
    for char in line:
        if char in '([{':
            stack.push(char)
        elif char in d_match:
            if stack.is_empty() or stack.peek() != d_match[char]:
                return False
            stack.pop()
    return stack.is_empty()
```

### Функция подсчета количества пар скобок в строке

```python
def count_pairs(line):
    stack = Stack()
    d_match = {')': '(', ']': '[', '}': '{'}
    count_p = 0
    for char in line:
        if char in '([{':
            stack.push(char)
        elif char in d_match:
            if stack.is_empty() or stack.peek() != d_match[char]:
                return "Invalid line!!!"
            stack.pop()
            count_p += 1
    if stack.is_empty():
        return count_p
    return "Invalid line!!!"
```

### Основная функция программы

```python
if __name__ == '__main__':
    line = input()
    if is_valid(line):
        print(f"Скобочная последовательность корректна.\nКоличество пар = {count_pairs(line)}.")
    else:
        print("Скобочная последовательность некорректна.")
```
