Class Employee:
    def __init__(self, name, employee_id, position, salary, workhours):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
        self.work_hours = work_hours

def get_total_hours(self):
    total = 0
    for i in self.work_hours:
        total += i
    return total

def give_raise(self, amount):
    self.salary += amount

def get_bonus(self):
    return self.salary * 0.1

def display_info(self):
    print('Name:', self.position)
    print('Position:', self.position)
    print('Salary:', self.salary)

def __eq__(self, other):
    return self.salary > other.salary

def __eq__(self, other):
    return self.salary > other.salary

def __gt__(self, other):
    return self.salary > other.salary

def __getitem__(self, index):
    return self.work_hours[index]

def __str__(self):
    return f'Employee:{self.name} - {self.position} {self.salary})'

Class Manager(Employee):
    def __init__(self, name, employee_id, position, salary, work_hours, team_size):
        super().__init__(name, employee_id, position, alary, work_hours)
        self.team_size

    def give_raise(self, amount):
        bonus = self.team_size * 100
        self.salary += amount + bonus

    def get_bonus(self):
        return self.salary * 0,2 + self.team_size * 50

    def get_total_hours(self):
        total = 0
        for i in self.work_hours:
            
