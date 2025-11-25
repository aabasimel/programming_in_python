from graphics import *

def main():
    win = GraphWin("Happy face", 600,600)
    win.setBackground("light green")

    head = Circle(Point(300,300), 150)
    head.setFill("peachpuff")
    head.setOutline("black")
    head.draw(win)

    rightEye= Circle(Point(240,250),30)
    rightEye.setOutline("black")
    rightEye.setFill("white")
    rightEye.draw(win)

    leftEye = Circle(Point(360,250),30)
    leftEye.setOutline("black")
    leftEye.setFill("white")
    leftEye.draw(win)

    left_pupil = Circle(Point(240, 250), 10)
    left_pupil.setFill("black")
    left_pupil.draw(win)

    right_pupil = Circle(Point(360, 250), 10)
    right_pupil.setFill("black")
    right_pupil.draw(win)

    nose = Polygon(Point(300,270),Point(260,330), Point(320,330))
    nose.setFill("peachpuff")
    nose.setOutline("black")
    nose.draw(win)

    mouth_outer = Circle(Point(300, 380), 30)
    mouth_outer.setFill("red")
    mouth_outer.setOutline("black")
    mouth_outer.draw(win)

    left_ear = Circle(Point(150, 280), 30)
    left_ear.setFill("peachpuff")
    left_ear.setOutline("black")
    left_ear.draw(win)

    left_ear = Circle(Point(450, 280), 30)
    left_ear.setFill("peachpuff")
    left_ear.setOutline("black")
    left_ear.draw(win)
    win.getMouse()
    win.close()
    

main()