import time
from CanvasPainter import CanvasPainter

#from memory_profiler import profile #ADD @profile BEFORE FUNCTION NAME TO ANALYSE IT

#@profile
def img800x600():

    start_time = time.time()

    data = CanvasPainter(800,600,24)

    data.setThikness(0)

    data.setColor(0xCC,0xCC,0xCC,CanvasPainter.COLOR_FILL)
    data.setWindow(0,800,0,600,False)

    data.drawLineH(30,10,-100)
    data.flush()

    data.setColor(0,255,0,True)
    data.setWindow(50,300,50,300,False)
    data.setColor(255,0,0)
    data.drawLineH(50,100,100)
    data.flush()
    data.restoreColor(True)

    data.setWindow(0,500,0,500)
    data.setColor(255,255,255)
    data.setColor(0,0,0,CanvasPainter.COLOR_FILL)
    data.drawCircle(250,250,200,True)
    data.restoreColor(True)

    data.setColor(0,0,255)
    data.setColor(255,0,0,CanvasPainter.COLOR_FILL)
    data.drawSquare(40,10,50,True)

    data.setColor(255,0,255,True)
    data.setColor(200,255,255)
    data.drawRectangle(400,400,-100,-100,True)
    data.restoreColor(CanvasPainter.COLOR_FILL)

    data.setColor(255,0,0,CanvasPainter.COLOR_FILL)
    data.drawSquare(200,200,-50,True)

    data.setColor(255,0,0,CanvasPainter.COLOR_FILL)
    data.drawSquare(200,200,-50,True)

    data.setColor(0,0,255)
    data.drawLineV(150,30,100)

    data.setColor(127,127,127)
    data.drawLine(10,100,200,150)
    data.flush()

    data.loadFont('./fonts/font32bits-20X5.bmp')
    data.setWindow(50,300,150,165)
    data.setColor(255,0,0,True)
    data.printChars(1,1,'HEllo World!')
    data.flush()


    data.saveBitmap('./CanvasPainter-v0.2/output-800x600.bmp')

    end_time = time.time()

    print("TIME ", (end_time-start_time))

img800x600()