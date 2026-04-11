import random
import sys

# Класс для трека
class Track:
    def __init__(self, name: str, duration: int, genre: str, rating: int):
        if (rating < 0):
            raise ValueError("Рейтинг должен быть положительным числом!!!")
        self.name = name
        self.duration = duration
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return f"Трек: {self.name} ({self.duration}с.)\nЖанр: {self.genre}\nРейтинг: {self.rating}"

# Основной класс для плейлиста
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
        if not self.tracks:
            print("Плейлист пуст.")
            return

    # проигрывание трека
    def play(self):
        self.tracks_is_empty()
        print(f"Сейчас играет:\n{self.tracks[self.cur_track_ind]}.")

    # следующий трек
    def next(self):
        self.tracks_is_empty()
        if self.repeat_mode == "one":
            pass
        elif self.repeat_mode == "all":
            self.cur_track_ind = (self.cur_track_ind + 1) % len(self.tracks)
        else:
            if self.cur_track_ind + 1 < len(self.tracks):
                self.cur_track_ind += 1
            else:
                print("Конец плейлиста.\nПовтор выключен.")
                return
        self.play()

    # предыдущий трек
    def previous(self):
        self.tracks_is_empty()
        if self.repeat_mode == "one":
            pass
        elif self.repeat_mode == "all":
            self.cur_track_ind = (self.cur_track_ind - 1) % len(self.tracks)
        else:
            if self.cur_track_ind - 1 < len(self.tracks):
                self.cur_track_ind -= 1
            else:
                print("Начало плейлиста.")
                return
        self.play()

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
        cols = [len(h) for h in headers]
        for row in rows:
            for j, cell in enumerate(row):
                cols[j] = max(cols[j], len(cell))
        print("+" + "+".join("-" * (x + 2) for x in cols) + "+")
        header_line = "| " + " | ".join(h.ljust(cols[i]) for i, h in enumerate(headers)) + " |"
        print(header_line)
        print("+" + "+".join("-" * (x + 2) for x in cols) + "+")
        for row in rows:
            data_line = "| " + " | ".join(cell.ljust(cols[i]) for i, cell in enumerate(row)) + " |"
            print(data_line)
            print("+" + "+".join("-" * (x + 2) for x in cols) + "+")

# основная функция
def main():
    playlist = Playlist()
    commands = {
        'add': 'добавить трек',
        'delete': 'удалить трек по названию',
        'shuffle': 'перемешать плейлист',
        'repeat': 'установить режим повтора (off/one/all)',
        'play': 'воспроизвести текущий трек',
        'next': 'следующий трек',
        'prev': 'предыдущий трек',
        'table': 'показать плейлист в виде таблицы',
        'rating': 'показать треки с рейтингом не ниже N',
        'help': 'показать справку',
        'exit': 'выйти'
    }
    print("Музыкальный плейлист.")
    print("Введите help для списка команд.")
    while True:
        command = input("> ").strip().lower()
        if command == "exit":
            print("До свидания!")
            sys.exit(0)
        elif command == "help":
            for i, name in commands.items():
                print(f"{i} - {name}")
        elif command == "add":
            name = input("Название: ").strip()
            if not name:
                print("Название не может быть пустым.")
                continue
            dur = input("Длительность (секунды или ММ:СС): ").strip()
            try:
                if ":" in dur:
                    dur = int(dur.split(":")[0]) * 60 + int(dur.split(":")[1])
                else:
                    dur = int(dur)
            except ValueError:
                print("Ошибка: неверный формат длительности.")
                continue
            genre = input("Жанр: ").strip()
            if not genre:
                print("Жанр не может быть пустым.")
                continue
            try:
                rating = int(input("Рейтинг: ").strip())
                track = Track(name, dur, genre, rating)
                playlist.add_track(track)
            except ValueError as e:
                print(e)
        elif command == "delete":
            name = input("Название трекhelpа для удаления: ").strip()
            if name:
                playlist.delete_track(name)
            else:
                print("Название не может быть пустым.")
        elif command == "shuffle":
            playlist.shuffle()
        elif command == "repeat":
            mode = input("Режим повтора (off/one/all): ").strip().lower()
            playlist.set_repeat_mode(mode)
        elif command == "play":
            playlist.play()
        elif command == "next":
            playlist.next()
        elif command == "prev":
            playlist.previous()
        elif command == "table":
            playlist.playlist_table()
        elif command == "rating":
            try:
                rat = int(input("Минимальный рейтинг: ").strip())
                playlist.get_tracks_by_rating(rat)
            except ValueError:
                print("Ошибка: введите число.")
        else:
            print("Неизвестная команда. Введите help.")

# запуск программы
if __name__ == '__main__':
    main()