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


# проверка корректности введенной строки
def is_valid(line):
    stack = Stack() # создание стека
    d_match = {')': '(', ']': '[', '}': '{'} # вспомогательный словарь
    for char in line:
        if char in '([{':
            stack.push(char) # добавление элемента в стек
        elif char in d_match:
            if stack.is_empty() or stack.peek() != d_match[char]: # проверка стека на пустоту или сравнение элементов
                return False
            stack.pop() # удаление элемента из стека
    return stack.is_empty()


# подсчет количества пар скобок в строке
def count_pairs(line):
    stack = Stack() # создание стека
    d_match = {')': '(', ']': '[', '}': '{'} # вспомогательный словарь
    count_p = 0 # количество пар
    for char in line:
        if char in '([{':
            stack.push(char) # добавление элемента в стек
        elif char in d_match:
            if stack.is_empty() or stack.peek() != d_match[char]: # проверка стека на пустоту или сравнение элементов
                return "Invalid line!!!"
            stack.pop() # удаление элемента из стека
            count_p += 1
    if stack.is_empty():
        return count_p
    return "Invalid line!!!"


# основная функция программы
if __name__ == '__main__':
    line = input()
    if is_valid(line):
        print(f"Скобочная последовательность корректна.\nКоличество пар = {count_pairs(line)}.")
    else:
        print("Скобочная последовательность некорректна.")

