
class Course:

    def __init__(self, module, code, commencement, students=[]):
        self.module = module.title()
        self.module_code = code
        self.commencement = commencement
        self.register = students

    def append_register(self, student):
        self.register.append(student)