# Документация для Калькулятора
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

## Общее описание решения
Калькулятор предназначен для вычисления площади и периметра фигур (круг, квадрат) по введенным пользователем размерам. Пользователю предлагается указать фигуру, тип вычисления (площадь или периметр) и соответствующие размеры (радиус для круга и длину стороны для квадрата).

## Описание функций

### `calc(fig, func, size)`
Функция для вычисления площади или периметра заданной фигуры.

- **Параметры:**
  - `fig` (str): Название фигуры ('circle' или 'square').
  - `func` (str): Название функции ('perimeter' или 'area').
  - `size` (list): Список размерностей фигуры.
  
- **Примеры вызова:**
  ```python
  calc('circle', 'area', [5])  # Вычисляет площадь круга с радиусом 5
  calc('square', 'perimeter', [4])  # Вычисляет периметр квадрата со стороной 4
