from Monster import *
from Monster_student import *
from Course import *

# Create two student objects

student10001 = MonsterStudent("sully", 23, "S-4117", "blue-purple polka dot", 10001, 1, ["Horns", "Teeth", "Claws"])
student10002 = MonsterStudent("mike Wazowski", 19, "M-9183", None, 10002, 1, ["Intelligent", "Funny"])

# Add a skill to each of your students

student10001.append_skill("Empathy")
student10002.append_skill("Humour")

# Create a course

scare_science = Course("S.O.S: science of scaring", "23-19", "Sept-2020")

# Append student objects / instances to list of student attributes in course

scare_science.append_register(student10001)
scare_science.append_register(student10002)

# Get list of students, iterate over, print student names

print(f"Students enrolled in course - {scare_science.module} ({scare_science.module_code}):")
for n in scare_science.register:
    print(n.name, ":  ", n.age)
    print(n.skills)
