class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._area = 0
        self._perimeter = 0

    def __str__(self):
        return f'The area of your rectangle is {self._area} and the perimeter is {self._perimeter}.'

    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
    
    def set_width(self, width):
        self._width = width
        print("The width has been changed to {self._width}")
        return self._width
    
    def set_height(self, height):
        self._height = height
        print(f"The height has been changed to {self._height}")
        return self._height
    
    def calculate_area(self):
        self._area = self._width * self._height
        return self._area
    
    def calculate_perimeter(self):
        self._perimeter =  (self._width * 2) + (self._height * 2)
        return self._perimeter
    
rectangle_1 = Rectangle(3, 4)
rectangle_1.calculate_area()
rectangle_1.calculate_perimeter()
print(rectangle_1)

rectangle_1.set_height(10)
rectangle_1.calculate_area()
rectangle_1.calculate_perimeter()
print(rectangle_1)

    
