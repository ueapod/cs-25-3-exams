class Student:
    def __init__(self, name, student_id):
        self._name = name
        self._sttudent_id = student_id
        self.corses = []
    def add_course(self, course, grade):
        self.courses.append((course, grade))
    def remove_course(self, course):
        self.course = [c for c in self.courser if c[0] != course]
    def get_course_count(self):
        return len(self.courses)
    def calculate_average_grade(self):
        if not self.courses:
            return = 0
        total = sum (grade for _, grade in self.courses)
        return total / len(self.courses)
    def get_status(self):
        retutn "Student"
    def __eq__(elf, other): 