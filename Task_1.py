# 1 вариант
# 1  задание 
class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
    def get_age(self):
        return int(2026 - self.year)
    def is_old(self):
        if get_age > 20:
            retutn "Old"
        else:
            return "Not old"
    def count_pages_per_year(self):
        return self.pages / get_age
class Textbook(Book):
    def __init__(self, subject):
        self.subject = subject
    def get.is_old(self, is_old):
        return self.is_old
    def set.is_old(self, is_old):
        if get_age > 10:
            retutn "Old"
        else:
            return "Not old"