from fractions import Fraction

class Pair:
    def __init__(self, first, second):
        # Проверка корректности значений аргументов
        if not isinstance(first, int) or first <= 0:
            raise ValueError("Поле first должно быть положительным целым числом.")
        
        # Преобразование second в дробное число, если это строка
        if isinstance(second, str):
            second = Fraction(second)
        elif not isinstance(second, (float, int, Fraction)) or second <= 0:
            raise ValueError("Поле second должно быть положительным дробным числом или строкой-дробью.")
        
        self.first = first
        self.second = float(second)  # Преобразование Fraction в float для хранения

    def read(self):
        # Ввод значений с клавиатуры
        try:
            self.first = int(input("Введите положительное целое число для first: "))
            if self.first <= 0:
                raise ValueError
        except ValueError:
            print("Некорректный ввод для поля first. Ожидается положительное целое число.")
            return

        try:
            second_input = input("Введите положительное дробное число или дробь в формате 'a/b' для second: ")
            if '/' in second_input:
                self.second = float(Fraction(second_input))
            else:
                self.second = float(second_input)
            if self.second <= 0:
                raise ValueError
        except (ValueError, ZeroDivisionError):
            print("Некорректный ввод для поля second. Ожидается положительное дробное число или дробь.")
            return

    def display(self):
        # Вывод значений на экран
        print(f"first: {self.first}, second: {self.second}")

    def power(self):
        # Вычисление общей калорийности продукта
        return self.first * self.second * 10

def make_Pair(first, second):
    # Создание экземпляра класса Pair с проверкой корректности аргументов
    try:
        return Pair(first, second)
    except ValueError as e:
        print(e)
        return None

if __name__ == '__main__':
    # Пример использования класса
    pair = make_Pair(150, "1/2")
    if pair:
        pair.display()
        print(f"Общая калорийность продукта: {pair.power()} ккал")

    # Пример работы метода read
    new_pair = Pair(100, "1/3")
    new_pair.read()
    new_pair.display()
    print(f"Общая калорийность продукта: {new_pair.power()} ккал")
