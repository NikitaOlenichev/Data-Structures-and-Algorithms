# Лабораторная работа 2
## Линейные структуры данных (Array / LinkedList)

### Выполнил Оленичев Никита Романович, группа ИДБ-25-07

### Базовая задача: Музыкальный плейлист (Playlist) 
### Вариативная часть: 7. Формирование списка треков с рейтингом не ниже заданного;  
###                    3. Вывод плейлиста в виде таблицы с выравниванием колонок.

## Обоснование выбора структуры данных:  
### Был выбран динамический массив, так как в плейлисте критически важны операции  
### произвольного доступа по индексу. Динамический массив выполняет их за O(1), а связный  
### список — за O(n), что делает его непригодным для плавной работы при даже средних  
### размерах плейлиста.

### Блок подключения библиотек

```python
import random
import sys
from tabulate import tabulate # библиотека для вывода текста в виде таблицы
```

### Класс для трека (Track)

```python
class Track:
    def __init__(self, name: str, duration: int, genre: str, rating: int):
        if (rating < 0):
            raise ValueError("Рейтинг должен быть положительным числом!!!")
        self.name = name
        self.duration = duration
        self.genre = genre
        self.rating = rating

    # строковое представление одного трека
    def __str__(self):
        return f"Трек: {self.name} ({self.duration}с.)\nЖанр: {self.genre}\nРейтинг: {self.rating}"
```

### Класс для плейлиста (Playlist)

```python
class Playlist:
    def __init__(self):
        self.tracks = [] # динамический массив треков
        self.cur_track_ind = 0
        self.repeat_mode = None
        
    # добавление трека в плейлист
    def add_track(self, track: Track):
        self.tracks.append(track)
        if len(self.tracks) == 1:
            self.cur_track_ind = 0
        print(f"Трек '{track.name}' добавлен.")

    # удаление трека из плейлиста
    def delete_track(self, name: str):
        for i, t in enumerate(self.tracks):
            if t.name == name:
                del self.tracks[i]
                if len(self.tracks) == 0:
                    self.cur_track_ind = 0
                elif self.cur_track_ind >= i:
                    self.cur_track_ind = max(0, self.cur_track_ind - 1)
                print(f"Трек {name} удалён.")
                return
        print(f"Трек с именем {name} не найден.")

    # перемешивание треков в плейлисте
    def shuffle(self):
        random.shuffle(self.tracks)
        if self.tracks:
            self.cur_track_ind = 0
        print("Плейлист перемешан.")

    # установка повтора треков
    def set_repeat_mode(self, mode: str):
        if mode in ('off', 'one', 'all'):
            if mode == 'off':
                self.repeat_mode = None
            else:
                self.repeat_mode = mode
            print(f"Режим повтора установлен: {mode}")
        else:
            print("Неверный режим повтора!\nИспользуйте: off, one, all.")

    # проверка пустой ли плейлист
    def tracks_is_empty(self):
        ...

    # проигрывание трека
    def play(self):
        ...

    # следующий трек
    def next(self):
        ...

    # предыдущий трек
    def previous(self):
        ...

    # вывод списка треков с рейтингом не ниже введенного
    def get_tracks_by_rating(self, rating: int):
        if rating < 0:
            print("Рейтинг должен быть положительным числом!")
            return []
        filtered = [t for t in self.tracks if t.rating >= rating]
        if filtered:
            print(f"Треки с рейтингом не ниже {rating}:")
            for i, t in enumerate(filtered):
                print(f"{i + 1}. {t}")
        else:
            print(f"Нет треков с рейтингом не ниже {rating}.")
        return filtered

    # вывод плейлиста в виде таблицы
    def playlist_table(self):
        self.tracks_is_empty()
        headers = ["№", "Название", "Длительность (с.)", "Жанр", "Рейтинг (*)"]
        rows = [[str(i + 1), t.name, str(t.duration), t.genre, str(t.rating)]
                for i, t in enumerate(self.tracks)]
        print(tabulate(rows, headers=headers, tablefmt="grid", numalign="center"))


# основная функция
def main():
    ...
```

### Детальную реализацию всех методов и функций можно увидеть в файле Lab2.py

### Добавление трека

```python
def add_track(self, track: Track):
        self.tracks.append(track)
        if len(self.tracks) == 1:
            self.cur_track_ind = 0
        print(f"Трек '{track.name}' добавлен.")
```

### Удаление трека

```python
def delete_track(self, name: str):
        for i, t in enumerate(self.tracks):
            if t.name == name:
                del self.tracks[i]
                if len(self.tracks) == 0:
                    self.cur_track_ind = 0
                elif self.cur_track_ind >= i:
                    self.cur_track_ind = max(0, self.cur_track_ind - 1)
                print(f"Трек {name} удалён.")
                return
        print(f"Трек с именем {name} не найден.")
```

### Перемешивание (shuffle)

```python
def shuffle(self):
        random.shuffle(self.tracks)
        if self.tracks:
            self.cur_track_ind = 0
        print("Плейлист перемешан.")
```

### Повтор (repeat one / repeat all)

```python
def set_repeat_mode(self, mode: str):
        if mode in ('off', 'one', 'all'):
            if mode == 'off':
                self.repeat_mode = None
            else:
                self.repeat_mode = mode
            print(f"Режим повтора установлен: {mode}")
        else:
            print("Неверный режим повтора!\nИспользуйте: off, one, all.")
```

### Формирование списка треков с рейтингом не ниже заданного

```python
def get_tracks_by_rating(self, rating: int):
        if rating < 0:
            print("Рейтинг должен быть положительным числом!")
            return []
        filtered = [t for t in self.tracks if t.rating >= rating]
        if filtered:
            print(f"Треки с рейтингом не ниже {rating}:")
            for i, t in enumerate(filtered):
                print(f"{i + 1}. {t}")
        else:
            print(f"Нет треков с рейтингом не ниже {rating}.")
        return filtered
```

### Вывод плейлиста в виде таблицы с выравниванием колонок

```python
def playlist_table(self):
        self.tracks_is_empty()
        headers = ["№", "Название", "Длительность (с.)", "Жанр", "Рейтинг (*)"]
        rows = [[str(i + 1), t.name, str(t.duration), t.genre, str(t.rating)]
                for i, t in enumerate(self.tracks)]
        print(tabulate(rows, headers=headers, tablefmt="grid", numalign="center"))
```
