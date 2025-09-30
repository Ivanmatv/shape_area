# Библиотека для вычисления площадей геометрических фигур

Библиотека для вычисления площадей различных геометрических фигур. В настоящее время поддерживает вычисление площади круга и треугольника с дополнительной проверкой на прямоугольность треугольника.

## Особенности
- 🟢 Вычисление площади круга по радиусу
- 🔺 Вычисление площади треугольника по трем сторонам
- 📐 Проверка треугольника на прямоугольность
- 🧪 Полное покрытие юнит-тестами
- 🔧 Легкое добавление новых фигур
- 🎯 Вычисление площади без знания типа фигуры на этапе компиляции

## Установка
```bash
uvicorn app.parcer:app --reload
```
Или установка из исходного кода:
```bash
git clone https://github.com/Ivanmatv/shape_area.git
cd shape_area
pip install .
```

## Использование
### Базовые примеры
```bash
from geometry import Circle, Triangle, calculate_area

# Создание круга
circle = Circle(5)
circle_area = circle.area()
print(f"Площадь круга: {circle_area}")

# Создание треугольника
triangle = Triangle(3, 4, 5)
triangle_area = triangle.area()
is_right = triangle.is_right_angled()
print(f"Площадь треугольника: {triangle_area}")
print(f"Треугольник прямоугольный: {is_right}")

# Универсальное вычисление площади
area1 = calculate_area(circle)
area2 = calculate_area(triangle)
print(f"Универсальный расчет: {area1}, {area2}")
```

### Обработка ошибок
```bash
from geometry import Circle, Triangle
from geometry.exceptions import InvalidShapeError

try:
    circle = Circle(-5)  # Отрицательный радиус
except InvalidShapeError as e:
    print(f"Ошибка: {e}")

try:
    triangle = Triangle(1, 1, 3)  # Некорректные стороны треугольника
except InvalidShapeError as e:
    print(f"Ошибка: {e}")
```

### Добавление новых фигур
Чтобы добавить новую фигуру, нужно:
- Создать новый класс в папке geometry/shapes/
- Унаследовать от базового класса Shape
- Реализовать обязательные методы:
```bash
from geometry.shapes.base import Shape

class NewShape(Shape):
    def __init__(self, *args):
        # Инициализация параметров фигуры
        pass
        
    def area(self) -> float:
        # Реализация вычисления площади
        pass
        
    def is_right_angled(self) -> bool:
        # Проверка на наличие прямого угла
        pass
```

### Тестирование
```bash
python -m pytest tests/
```

Тесты покрывают:
- Корректность вычисления площадей
- Обработку некорректных входных данных
- Проверку треугольников на прямоугольность
- Универсальный калькулятор площадей