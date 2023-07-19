import random

"""class Hat: # Class ın ilk hali
    def __init__(self):
        self.houses = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw']

    def sort(self, name):
        random.shuffle(self.houses)
        print(name, 'is in', random.choice(self.houses))


hat = Hat()
hat.sort('Harry')
"""


class Hat:  # Class ın yeni bir nesne oluşturmadan direkt içindeki class variable ına bağlandığı @classmethod kullanımı
    houses = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw']

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} is from {random.choice(self.houses)}"

    @classmethod
    def sort(cls, name):
        if name:
            print(name, 'is in', random.choice(cls.houses))
            return
        raise ValueError("Missing name")


# 1
hat = Hat('Harry')
print(hat)

# 2
Hat.sort('Harry')
