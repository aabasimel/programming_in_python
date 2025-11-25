from graphics import *
import random

def main():
    d = 400  
    win = GraphWin("Approximate π", d, d)
    win.setBackground("white")
    
    circle = Circle(Point(d/2, d/2), d/2)
    circle.setOutline("green")
    circle.draw(win)
    
    points_inside = 0
    total_points = 0
    
    info_text = Text(Point(d/2, 20), "")
    info_text.draw(win)
    
    for i in range(10000):
        x = random.uniform(0, d)
        y = random.uniform(0, d)
        
        distance_squared = (x - d/2)**2 + (y - d/2)**2
        
        if distance_squared <= (d/2)**2:
            points_inside += 1
            win.plotPixel(int(x), int(y), "red")
        else:
            win.plotPixel(int(x), int(y), "blue")
        
        total_points += 1
        
        if (i + 1) % 100 == 0:
            ratio = points_inside / total_points
            pi_approx = ratio * 4
            
            info_text.setText(f"Points: {total_points}, π ≈ {pi_approx:.6f}")
            print(f"After {total_points} points: π ≈ {pi_approx:.6f}")
    
    final_ratio = points_inside / total_points
    final_pi = final_ratio * 4
    final_text = Text(Point(d/2, d-20), f"Final: π ≈ {final_pi:.6f}")
    final_text.draw(win)
    
    print(f"\nFinal approximation after {total_points} points:")
    print(f"Points inside circle: {points_inside}")
    print(f"Total points: {total_points}")
    print(f"Ratio: {final_ratio:.6f}")
    print(f"π ≈ {final_pi:.6f}")
    
    win.getMouse()
    win.close()

main()