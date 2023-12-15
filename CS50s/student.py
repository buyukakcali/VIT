class Student:
    def __init__(self, name, house):
        if name == '':
            raise ValueError("Missing name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('Hooop')
        self._name = name


def main():
    stud = Student('Ali', 'Adana')
    stud.name = None
    print(stud)


def get_student():
    name = input('Name:')
    house = input('House')
    return Student(name, house)


if __name__ == '__main__':
    main()
