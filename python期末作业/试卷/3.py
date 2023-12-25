import math

class Shape:
    def __init__(self, name):
        self.name = name
        self.area = 0
        self.perimeter = 0

    def calArea(self):
        pass

    def calPerimeter(self):
        pass

    def Display(self):
        print(f"图形: {self.name}")
        print(f"面积: {self.area}")
        print(f"周长: {self.perimeter}\n")


class Rectangle(Shape):
    def __init__(self, name):
        super().__init__(name)
        self.length = float(input("请输入矩形的长度: "))
        self.width = float(input("请输入矩形的宽度: "))
        self.calArea()
        self.calPerimeter()

    def calArea(self):
        self.area = self.length * self.width

    def calPerimeter(self):
        self.perimeter = 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, name):
        super().__init__(name)
        self.side1 = float(input("请输入三角形的第一边长: "))
        self.side2 = float(input("请输入三角形的第二边长: "))
        self.side3 = float(input("请输入三角形的第三边长: "))
        self.calArea()
        self.calPerimeter()

    def calArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        self.area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calPerimeter(self):
        self.perimeter = self.side1 + self.side2 + self.side3


class Circle(Shape):
    def __init__(self, name):
        super().__init__(name)
        self.radius = float(input("请输入圆形的半径: "))
        self.calArea()
        self.calPerimeter()

    def calArea(self):
        self.area = math.pi * self.radius ** 2

    def calPerimeter(self):
        self.perimeter = 2 * math.pi * self.radius


# 测试
rectangle = Rectangle("矩形")
rectangle.Display()

triangle = Triangle("三角形")
triangle.Display()

circle = Circle("圆形")
circle.Display()
