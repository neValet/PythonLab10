class Student:
    eyes_colour = "blue"

    def __init__(self,
                 name="Denis",
                 surname="Dub",
                 rating=13,
                 height=183,
                 hair_colour="black",
                 weight=82,
                 nationality="Ukrainian"):
        self.name = name
        self.surname = surname
        self.rating = rating
        self.height = height
        self.hair_colour = hair_colour
        self.weight = weight
        self.nationality = nationality

    def __del__(self):
        print("Student ", self.name + self.surname, " deleted")

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def get_eyes_colour():
        return Student.eyes_colour
