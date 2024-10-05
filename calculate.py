import circle  # Импортируем модуль с функциями для работы с кругом
import square  # Импортируем модуль с функциями для работы с квадратом

figs = ['circle', 'square']  # Доступные фигуры
funcs = ['perimeter', 'area']  # Доступные функции
sizes = {}  # Словарь для хранения количества размеров для каждой фигуры и функции

def calc(fig, func, size):
    """
    Вычисляет заданную функцию (периметр или площадь) для фигуры.

    :param fig: Название фигуры ('circle' или 'square').
    :param func: Название функции ('perimeter' или 'area').
    :param size: Список размерностей фигуры.
    
    :raises AssertionError: Если fig или func не находятся в допустимых списках.
    """
    assert fig in figs  # Проверка, что фигура допустима
    assert func in funcs  # Проверка, что функция допустима

    result = eval(f'{fig}.{func}(*{size})')  # Вычисляем результат с помощью eval
    print(f'{func} of {fig} is {result}')  # Выводим результат

if __name__ == "__main__":
    """
    Основной блок программы, запрашивающий у пользователя ввод данных
    и вызывающий функцию calc для вычисления результата.

    :raises ValueError: Если вводимые размеры не соответствуют ожидаемому количеству.
    """
    func = ''  # Инициализация переменной для функции
    fig = ''  # Инициализация переменной для фигуры
    size = list()  # Инициализация списка для размерностей
    
    # Цикл для ввода фигуры
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")
    
    # Цикл для ввода функции
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")
    
    # Цикл для ввода размерностей
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
    
    # Вызов функции вычисления
    calc(fig, func, size)
