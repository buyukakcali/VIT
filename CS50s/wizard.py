class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError('Missing name!')
        self.name = name

    ...


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


def main():
    wizard = Wizard("Albus")
    student = Student("Harry", "Gryffindor")
    professor = Professor("Severus", "Defense Against the Dark Arts")
    print(student.house)


if __name__ == '__main__':
    main()
