from tenthLab import Student

petro = Student()

vasya = Student(fullname="Vasya Chornozem",
                rating=2,
                height=180,
                hairColour="brown")

oleg = Student(fullname="Oleg Korovay",
               rating=6,
               height=168,
               hairColour="blonde",
               weight=90,
               nationality="Ukrainian")

print(petro)
print(vasya)
print(oleg)
print(Student.returnEyesColour())
