import time
from CanvasPainter import CanvasPainter

#from memory_profiler import profile #ADD @profile BEFORE FUNCTION NAME TO ANALYSE IT

def img128x160():
    

    start_time = time.time()

    data = CanvasPainter(128,160,16) #FOR MY TFT SCREEN 160x128

    data.setColor(0,0,0,True)
    data.setWindow(0,128,0,160,False)
    data.loadFont('./fonts/font16bits-20X5.bmp')

    data.setThikness(1)

    data.setColor(0,255,0,CanvasPainter.COLOR_FILL)
    data.setColor(255,255,255)
    data.drawCircle(100,100,25,True)

    data.setColor(255,0,0,CanvasPainter.COLOR_FILL)
    data.setColor(255,255,0)
    data.drawSquare(60,50,-40,True)

    data.setThikness(2)
    
    data.setColor(127,127,127)
    data.drawLine(10,90,10,80)

    data.setColor(0,255,0)
    data.drawLineH(10,40,50)

    data.setColor(255,0,0)
    data.drawLineV(40,60,100)

    data.setThikness(0)
    data.setColor(255,0,255,CanvasPainter.COLOR_FILL)
    data.setColor(200,255,255)
    data.setRotation(30,64,80)
    data.drawRectangle(64-20,80-25,40,50,True)
    data.setRotation()
    data.restoreColor(CanvasPainter.COLOR_FILL)
    
    data.flush()

    data.setWindow(10,50,10,50,True)
    data.setColor(0,255,0,CanvasPainter.COLOR_FILL)
    data.setColor(255,255,255,CanvasPainter.COLOR_TRANSPARENCY)
    data.loadImage(0,0,'./images/picture16bits.bmp')
    data.flush()

    data.setColor(255,255,0)
    data.setWindow(1,128,1,40)
    data.printChars(1,1,'Hello World !',9)
    data.flush()

    data.saveBitmap('./CanvasPainter-v0.2/output-128x160.bmp')


    end_time = time.time()

    print("TIME ", (end_time-start_time))


img128x160()    