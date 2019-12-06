def func(first, *next, **rest):
    print((first))
    print((next))
    print((rest))


func('a', 332, 32, a=3932, b=3939)


def swapper(x, y):
    return lambda z: y, x


another = swapper(10, 11)
print(another)

name = "Bruno"
id = 3937
print(f"{name} ------ {id}")


class Human:
    def __init__(self, name):
        self.name = name

    @property
    def email(self):
        return self.email


bruno = Human('Kofi')
