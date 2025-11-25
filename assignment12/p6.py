from graphics import *
import random
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python appropi.py <window_size> <num_points>")
        print("Example: python appropi.py 400 10000")
        sys.exit(1)
    
    try:
        d = int(sys.argv[1])
        num_points = int(sys.argv[2])
        
        if d <= 0 or d > 1000:
            print("Error: Window size must be between 1 and 1000 pixels")
            sys.exit(1)
            
        if num_points <= 0:
            print("Error: Number of points must be positive")
            sys.exit(1)
            
    except ValueError:
        print("Error: Both parameters must be integers")
        sys.exit(1)
    
    win = GraphWin(f"Approximate π (Size: {d}, Points: {num_points})", d, d)
    win.setBackground("white")
    
    circle = Circle(Point(d/2, d/2), d/2)
    circle.setOutline("green")
    circle.draw(win)
    
    points_inside = 0
    total_points = 0
    
    info_text = Text(Point(d/2, 20), "")
    info_text.draw(win)
    
    param_text = Text(Point(d/2, d-40), f"Window: {d}x{d}, Points: {num_points}")
    param_text.draw(win)
    
    for i in range(num_points):
        x = random.uniform(0, d)
        y = random.uniform(0, d)
        
        distance_squared = (x - d/2)**2 + (y - d/2)**2
        
        if distance_squared <= (d/2)**2:
            points_inside += 1
            win.plotPixel(int(x), int(y), "red")
        else:
            win.plotPixel(int(x), int(y), "blue")
        
        total_points += 1
        
        display_interval = max(1, num_points // 100) 
        if (i + 1) % display_interval == 0 or i == num_points - 1:
            ratio = points_inside / total_points
            pi_approx = ratio * 4
            
            info_text.setText(f"Points: {total_points}/{num_points}, π ≈ {pi_approx:.6f}")
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

if __name__ == "__main__":
    main()