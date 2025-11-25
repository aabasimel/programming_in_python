from graphics import *

def draw_archery(circle_data):
    win = GraphWin("Archery Target", 400, 400)
    win.setBackground("white")
    
    colors = ["yellow", "red", "blue", "black", "white"]
    
    for i in range(len(circle_data)-1, -1, -1):
        center_x, center_y, radius = circle_data[i]
        circle = Circle(Point(center_x, center_y), radius)
        
        circle.setFill(colors[i])
        circle.setOutline("black")
        circle.draw(win)
    
    instruction = Text(Point(200, 380), "Click anywhere to close")
    instruction.draw(win)
    win.getMouse()
    win.close()

def main():
    circle_data = [(200, 200, 15), (200, 200, 30), 
                   (200, 200, 45), (200, 200, 60), 
                   (200, 200, 75)]
    draw_archery(circle_data)

main()