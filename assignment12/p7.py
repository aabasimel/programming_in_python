from graphics import *

def main():
    win = GraphWin("Unique Color Pixels", 255, 255)
    win.setBackground("white")
    
    pixel_count = 0
    total_pixels = 255 * 255
    
    print(f"Generating {total_pixels} unique colors...")
    
    for x in range(255):
        for y in range(255):
            r = x
            g = y
            b = (x + y) % 256  
            
            color = color_rgb(r, g, b)
            
            if pixel_count % 150 != 0:
                win.plotPixel(x, y, color)
            else:
                win.plotPixel(x, y, color)
                if pixel_count % 1500 == 0: 
                    print(f"Plotted pixel {pixel_count} at ({x},{y})")
            
            pixel_count += 1
    
    completion_text = Text(Point(127, 127), f"Completed!\n{pixel_count} unique colors")
    completion_text.setFill("white")
    completion_text.draw(win)
    
    print(f"Completed! Generated {pixel_count} unique colors.")
    print("Each pixel has a unique RGB color combination.")
    
    instruction = Text(Point(127, 10), "Click anywhere to close")
    instruction.draw(win)
    win.getMouse()
    win.close()

main()