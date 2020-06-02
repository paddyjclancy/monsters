from Monster import *
from Monster_student import *
from Course import *


# Students
student10001 = MonsterStudent("sully", 23, "S-4117", "blue-purple polka dot", 10001, 1, ["Horns", "Teeth", "Claws"])

print(student10001.name)
print(student10001.skills)
print(f"Fur: {student10001.fur.capitalize()}")


print("-----------")
student10002 = MonsterStudent("mike Wazowski", 19, "M-9183", None, 10002, 1, ["Intelligent", "Funny"])

print(student10002.name)
print(student10002.skills)
print(f"Fur: {student10002.fur}")

# Append skill
student10003 = MonsterStudent("randall", 20, "R-4631", None, 10003, 1, [])

print("-----------")
print(student10003.name)

print(f"Current portfolio: {student10003.skills}")
student10003.append_skill("Disguise")
student10003.append_skill("Invisibility")
print(f"New portfolio: {student10003.skills}")


# Courses & Enrollment
print("-----------")
scare_science = Course("S.O.S: science of scaring", "23-19", "Sept-2020")

print(scare_science.module + ":   " + scare_science.module_code)
print(f"Start date (TBC): {scare_science.commencement}")
print(f"Students enrolled as of yesterday: {scare_science.register}")

print("-----------")
scare_science.append_register(student10001.name)
scare_science.append_register(student10002.name)
scare_science.append_register(student10003.name)
print(f"Students enrolled to date: {scare_science.register}")
