from graphics import *

def calculate_perimeter(length, width):
    """Calculate and return the perimeter of a rectangle"""
    return 2 * (length + width)

def calculate_area(length, width):
    """Calculate and return the area of a rectangle"""
    return length * width

def main():
    win = GraphWin("Click to Draw Rectangle", 800, 600)
    win.setBackground("white")
    
    instruction1 = Text(Point(400, 20), "Click two points to draw a rectangle")
    instruction1.draw(win)
    instruction2 = Text(Point(400, 40), "First click: one corner, Second click: opposite corner")
    instruction2.draw(win)
    
    point1 = win.getMouse()
    point1_circle = Circle(point1, 3)
    point1_circle.setFill("red")
    point1_circle.draw(win)
    
    point2 = win.getMouse()
    point2_circle = Circle(point2, 3)
    point2_circle.setFill("red")
    point2_circle.draw(win)
    
    rectangle = Rectangle(point1, point2)
    rectangle.setFill("light blue")
    rectangle.setOutline("black")
    rectangle.draw(win)
    
    length = abs(point2.getX() - point1.getX())
    width = abs(point2.getY() - point1.getY())
    
    perimeter = calculate_perimeter(length, width)
    area = calculate_area(length, width)
    
    results_text = Text(Point(400, 580), f"Length: {length:.1f} pixels, Width: {width:.1f} pixels")
    results_text.draw(win)
    
    perimeter_text = Text(Point(400, 560), f"Perimeter: {perimeter:.1f} pixels")
    perimeter_text.draw(win)
    
    area_text = Text(Point(400, 540), f"Area: {area:.1f} square pixels")
    area_text.draw(win)
    
    print(f"Rectangle dimensions: {length:.1f} x {width:.1f}")
    print(f"Perimeter: {perimeter:.1f}")
    print(f"Area: {area:.1f}")
    close_text = Text(Point(400, 500), "Click anywhere to close")
    close_text.draw(win)
    win.getMouse()
    win.close()

main()