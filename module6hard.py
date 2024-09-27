print(f'{"Задание"} {"«Они все так похожи»"}')


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = self._initialize_sides(sides)
        self.__color = list(color)
        self.filled = False

    def _initialize_sides(self, sides):
        if self.is_valid_sides(*sides):
            return list(sides)
        return [1] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255
                   for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Неверный цвет. Цвет не изменён!")

    def is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0
                                                          for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print("Недопустимые стороны. Стороны не изменены")


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color, 1)
        self.__radius = circumference / (2 * 3.14)

    def get_square(self):
        return 3.14 * (self.__radius * 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        if len(self.get_sides()) == 3:
            a, b, c = self.get_sides()
            s = (a + b + c) / 2
            return (s * (s - a) * (s - b) * (s - c)) * 0.5
        return 0


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_lenght = 1):
        super().__init__(color, *([side_lenght] * self.sides_count))

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3


#Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

