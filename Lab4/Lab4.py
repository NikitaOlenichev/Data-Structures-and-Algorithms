# Класс электронного журнала группы
class StudentJournal:
    def __init__(self):
        self.students = {} # словарь студентов, имеет вид: 'id': {'name': имя, 'score': балл}
        self.students_ids = {} # словарь id студентов, имеет вид: 'имя': id
        self.next_id = 1

    # Добавление нового студента в журнал
    def add_student(self, name, score=None):
        if name in self.students_ids:
            raise ValueError(f"Студент с именем {name} уже существует.")
        student_id = self.next_id
        self.students[student_id] = {'name': name, 'score': score}
        self.students_ids[name] = student_id
        self.next_id += 1
        print(f"Студент с именем {name} добавлен.")
        return student_id

    # Выставление или обновление балла студента по его id
    def set_score_by_id(self, student_id, score):
        if student_id not in self.students:
            raise KeyError(f"Студент с id {student_id} не найден.")
        self.students[student_id]['score'] = score

    # Выставление или обновление балла студента по его имени
    def set_score_by_name(self, name, score):
        if name not in self.students_ids:
            raise KeyError(f"Студент с именем {name} не найден.")
        student_id = self.students_ids[name]
        self.students[student_id]['score'] = score

    # Получение балла студента по его id
    def get_score_by_id(self, student_id):
        if student_id not in self.students:
            raise KeyError(f"Студент с ID {student_id} не найден.")
        return self.students[student_id]['score']

    # Получение балла студента по его имени
    def get_score_by_name(self, name):
        if name not in self.students_ids:
            raise KeyError(f"Студент с именем {name} не найден.")
        student_id = self.students_ids[name]
        return self.students[student_id]['score']

    # Получение всех студентов и их результатов
    def get_all_students(self):
        result = []
        for stud_id, data in self.students.items():
            result.append((stud_id, data['name'], data['score']))
        return result

    # Нахождение студента с минимальным баллом
    def find_min_score_student(self):
        if not self.students:
            return None
        candidates = [(stud_id, data['name'], data['score'])
                      for stud_id, data in self.students.items()
                      if data['score'] is not None]
        if not candidates:
            return None
        return min(candidates, key=lambda x:x[2])

    # Вывод журнала студентов
    def __str__(self):
        lines = []
        for stud_id, data in self.students.items():
            name = data['name']
            score = data['score'] if data['score'] is not None else '-'
            lines.append(f"{stud_id}. {name} -> {score}")
        return "\n".join(lines)

# Тестовая функция для демонстрации работы программы
def test():
    journal = StudentJournal()

    # добавление студентов
    id_ivan = journal.add_student("Ivan", 54)
    id_anna = journal.add_student("Anna", 45)
    id_nikita = journal.add_student("Nikita", 37)
    print()

    # вывод всех студентов
    print("Все студенты:")
    print(journal)
    print()

    # получение баллов по имени и id
    print(f"Балл Ивана по имени: {journal.get_score_by_name("Ivan")}")
    print(f"Балл Анны по id: {journal.get_score_by_id(id_anna)}")
    print()

    # обновление балла по имени и id
    journal.set_score_by_name("Anna", 30)
    journal.set_score_by_id(id_nikita, 54)
    print("После обновления баллов:")
    print(journal)
    print()

    # добавление стулента без балла
    id_roman = journal.add_student("Roman")
    print("После добавления Романа:")
    print(journal)
    print()

    # поиск студента с минимальным баллом
    min_student = journal.find_min_score_student()
    if min_student:
        stud_id, name, score = min_student
        print(f"Студент с минимальным баллом: {name} (id {stud_id}) -> {score}")
    else:
        print("Журнал пуст.")

    # попытка получить балл несуществующего студента
    try:
        journal.get_score_by_name("Sergey")
    except KeyError as e:
        print(f"Ошибка: {e}")

# Запуск программы
if __name__ == '__main__':
    test()
