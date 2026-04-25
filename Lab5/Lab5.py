import sys

# Класс для одного узла дерева выражения
class TreeNode:
    def __init__(self, value):
        self.value = value              # хранимые данные (число или оператор)
        self.left = None                # левый потомок
        self.right = None               # правый потомок

# Построение дерева по списку токенов постфиксной записи
def build_expression_tree(tokens):
    stack = []
    for token in tokens:
        if token in '+-*/':
            root = TreeNode(token)      # внутренний узел - оператор
            root.right = stack.pop()    # правый лист - второй операнд
            root.left = stack.pop()     # левый лист - первый операнд
            stack.append(root)
        else:
            root = TreeNode(int(token)) # внутренний узел - целое число
            stack.append(root)
    return stack.pop()                  # возвращаем корень дерева

# Рекурсивное вычисление значения выражения, расположенного в дереве.
def evaluate(root):
    if root.left is None and root.right is None:
        return root.value               # лист - число
    left_value = evaluate(root.left)
    right_value = evaluate(root.right)
    if root.value == '+':
        return left_value + right_value
    elif root.value == '-':
        return left_value - right_value
    elif root.value == '*':
        return left_value * right_value
    elif root.value == '/':
        return left_value / right_value
    else:
        raise ValueError(f"Неизвестный оператор: {root.value}!!!")

# Выражение в префиксной (prefix) форме
def prefix(root):
    if root.left is None and root.right is None:
        return str(root.value)           # лист - число
    left = prefix(root.left)
    right = prefix(root.right)
    return f"{root.value} {left} {right}"

# Основная функция программы
def main():
    line = sys.stdin.readline().strip()  # читаем строку с выражением
    if not line:
        return
    tokens = line.split()
    root = build_expression_tree(tokens)
    result = evaluate(root)
    prefix_line = prefix(root)
    print(f"Результат: {result}\nПрефиксная форма: {prefix_line}")

# Запуск основной функции программы
if __name__ == '__main__':
    main()
