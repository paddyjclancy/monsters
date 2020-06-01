from Monster import *

class MonsterStudent(Monster):

    def __init__(self, name, age, tax_number, fur, student_no, year_of_study, skills=[]):
        super().__init__(name, age, tax_number, fur)
        self.student_no = student_no
        self.year_of_study = int(year_of_study)
        self.skills = skills

    def append_skill(self, new_skill):
        self.skills.append(new_skill)
