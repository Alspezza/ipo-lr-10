import collision
from collision import intersectionAreaRect, intersectionAreaMultiRect as func
rectangles = []
try:
        kolvo = int(input("Введите количество прямоугольников: "))
        if kolvo <= 0:
            print("Некорректно введено количество прямоугольников. ")
            sys.exit(1)
            
        print(f"Введите координаты {kolvo} прямоугольников")
        
        for i in range(kolvo):
            print(f"\nПрямоугольник {i+1}: ")
            left_down_x = float(input("Введите x левого нижнего угла: "))
            left_down_y = float(input("Введите y левого нижнего угла: "))
            right_up_x = float(input("Введите x правого верхнего угла: "))
            right_up_y = float(input("Введите y правого верхнего угла: "))
            
            rectangles.append([(left_down_x, left_down_y), (right_up_x, right_up_y)])
        
        area = func(rectangles)
        
        if area > 0:
            print(f"Площадь пересечения всех прямоугольников: {area}")
        else:
            print(f"У прямоугольников нет общего пересечения.")
except ValueError:
    print("Числа введены некорректно")
