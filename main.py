from tenthLab import Student

petro = Student()

vasya = Student(name="Vasya",
                surname="Chornozem",
                rating=2,
                height=180,
                hair_colour="brown")

oleg = Student(name="Oleg",
               surname="Korovay",
               rating=6,
               height=168,
               hair_colour="blond",
               weight=90,
               nationality="Ukrainian")

print(petro)
print(vasya)
print(oleg)
print(Student.get_eyes_colour())
