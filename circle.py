import math

def area(r):
    """
    Вычисляет площадь круга.

    :param r: Радиус круга.
    :return: Площадь круга.
    """
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет периметр (длину окружности) круга.

    :param r: Радиус круга.
    :return: Длина окружности.
    """
    return 2 * math.pi * r
