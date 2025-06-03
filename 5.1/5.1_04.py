class Programmer:

    def __init__(self, name, post, experience=0, treasure=0, salary=0):
        self.name = name
        self.post = post
        self.experience = experience
        self.treasure = treasure
        self.salary = salary
        if self.post == "Junior":
            self.salary = 10
        elif self.post == 'Middle':
            self.salary = 15
        elif self.post == 'Senior':
            self.salary = 20

    def work(self, time):
        self.experience += time
        self.treasure += time * self.salary

    def rise(self):
        if self.post == 'Junior':
            self.post = 'Middle'
            self.salary = 15
        elif self.post == 'Middle':
            self.post = 'Senior'
            self.salary = 20
        else:
            self.salary += 1

    def info(self):
        return f"{self.name} {self.experience}ч. {self.treasure}тгр."