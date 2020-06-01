from Monster_student import *
from Course import *


# Students
sully = MonsterStudent("sully", 23, "S-4117", "blue-purple polka dot", 10001, 1, ["Horns", "Teeth", "Claws"])
print(sully.name)
print(sully.skills)
print(f"Fur: {sully.fur.capitalize()}")

print("-----------")
mike = MonsterStudent("mike Wazowski", 19, "M-9183", None, 10002, 1, ["Intelligent", "Funny"])
print(mike.name)
print(mike.skills)
print(f"Fur: {mike.fur}")

# Append skill
randall = MonsterStudent("randall", 20, "R-4631", None, 10003, 1, [])
print("-----------")
print(randall.name)
print(f"Current portfolio: {randall.skills}")
randall.append_skill("Disguise")
randall.append_skill("Invisibility")
print(f"New portfolio: {randall.skills}")


# Courses & Enrollment
print("-----------")
scare_science = Course("S.O.S: science of scaring", "23-19", "Sept-2020")
print(scare_science.module + ":   " + scare_science.module_code)
print(f"Start date (TBC): {scare_science.commencement}")
print(f"Students enrolled as of yesterday: {scare_science.register}")
print("-----------")
scare_science.append_register(sully.name)
scare_science.append_register(mike.name)
scare_science.append_register(randall.name)
print(f"Students enrolled to date: {scare_science.register}")

