class Student:

    eyesColour = "blue"

    def __init__(self,
                 fullname="Denis Dub",
                 rating=13,
                 height=183,
                 hairColour="black",
                 weight=82,
                 nationality="Ukrainian"):
        self.fullname = fullname
        self.rating = rating
        self.height = height
        self.hairColour = hairColour
        self.weight = weight
        self.nationality = nationality

    def __del__(self):
        print("Student ", self.fullname, " deleted")

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def returnEyesColour():
        return Student.eyesColour
