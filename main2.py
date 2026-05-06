class Movie:
    def __init__(self, title, director, duration, year, genre, actors):
        self._title = title
        self._director = director
        self._duration = duration
        self._year = year
        self._genre = genre
        self._actors = actors

    # геттеры/сеттеры (минимум)
    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    # методы
    def get_age(self):
        return 2026 - self._year  # просто руками

    def is_classic(self):
        return self.get_age() > 50

    def list_cast(self):
        for a in self._actors:
            print(a)

    def get_info(self):
        return self._title, self._director, self._year

    def get_genre_info(self):
        return "Жанр: " + self._genre

    # перегрузки
    def __str__(self):
        return f"Movie: {self._title} by {self._director} ({self._year}) - {self._duration} мин"

    def __lt__(self, other):
        return self._duration < other._duration

    def __add__(self, other):
        return self._duration + other._duration

    def __contains__(self, actor):
        for a in self._actors:
            if a == actor:
                return True
        return False


class Documentary(Movie):
    def __init__(self, title, director, duration, year, genre, actors, subject, facts):
        super().__init__(title, director, duration, year, genre, actors)
        self._subject = subject
        self._facts = facts

    def is_classic(self):
        return self.get_age() > 30  # изменили

    def list_cast(self):
        print("Участники:")
        for a in self._actors:
            print(a)

    def get_facts_count(self):
        return len(self._facts)

    def get_genre_info(self):
        return "Документалка про " + self._subject