import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def read(self):
        try:
            self.x = float(input("Введите координату x: "))
            self.y = float(input("Введите координату y: "))
        except ValueError:
            print("Некорректный ввод. Ожидается число.")

    def display(self):
        print(f"Координаты точки: (x: {self.x}, y: {self.y})")

    def move_x(self, dx):
        self.x += dx

    def move_y(self, dy):
        self.y += dy

    def distance_to_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to_point(self, other):
        if not isinstance(other, Point):
            raise ValueError("Аргумент должен быть экземпляром класса Point.")
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def to_polar(self):
        r = self.distance_to_origin()
        theta = math.atan2(self.y, self.x)
        return r, theta

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

if __name__ == '__main__':
    # Пример использования класса Point
    p1 = Point(3, 4)
    p1.display()
    print(f"Расстояние до начала координат: {p1.distance_to_origin()}")

    p2 = Point()
    p2.read()
    p2.display()
    print(f"Расстояние до точки p1: {p1.distance_to_point(p2)}")

    p1.move_x(2)
    p1.move_y(-1)
    p1.display()
    print(f"Координаты точки p1 в полярных координатах: {p1.to_polar()}")

    print(f"Точки p1 и p2 совпадают: {p1 == p2}")
    print(f"Точки p1 и p2 не совпадают: {p1 != p2}")
