class Wizard():
    @classmethod
    def get(cls, name):
        if not name:
            raise ValueError('Missing name')
            exit()
        cls.name = name
        print('Name is', cls.name)
        return cls.name


class Student(Wizard):
    def __init__(self):
        super.__init__().name = name
        self.house = house

    ...


def main():
    Student.get('')


if __name__ == '__main__':
    main()
