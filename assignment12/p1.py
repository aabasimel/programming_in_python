from graphics import *

def main():
    win = GraphWin("Click to Create Squares", 700, 400)
    
    for i in range(10):
        p = win.getMouse()
        
      
        shape = Rectangle(Point(p.getX()-20, p.getY()-20), 
                         Point(p.getX()+20, p.getY()+20))
        shape.setFill("red")
        shape.setOutline("red")
        shape.draw(win)
        
        print(f"Square {i+1} created at: {p.getX()}, {p.getY()}")
    
    win.getMouse()
    win.close()

main()
            
