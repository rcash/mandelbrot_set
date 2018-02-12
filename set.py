import turtle
from complex import Complex
from mandelbrot_calc import Mandelbrot

class Display:
    def __init__(self):
        self.__drawsize = 300
        self.__llbound = Complex(-2,-2)
        self.__urbound = Complex(2,2)
        self.xcen = 0
        self.ycen = 0
        turtle.hideturtle()
        turtle.bgcolor('#ffffff')
        self.screen = turtle.getscreen()
        turtle.tracer(0,0)
        self.draw(self.xcen,self.ycen)
        self.screen.onclick(self.click)
        self.screen.mainloop()

    def draw(self,xcenter, ycenter):
        turtle.clear()
        for x in range(int(xcenter - self.__drawsize/2), int(xcenter + self.__drawsize/2 + 1)):
            #fixes the white lines when moving from each 'col' of pixels
            turtle.up()
            turtle.goto(x, ycenter - self.__drawsize/2)
            turtle.down()
            for y in range(int(ycenter - self.__drawsize/2), int(ycenter + self.__drawsize/2 + 1)):
                a = (x/self.__drawsize) * (self.__urbound.getreal() - self.__llbound.getreal())
                b = (y/self.__drawsize) * (self.__urbound.getimag() - self.__llbound.getimag())
                loc = Complex(a,b)
                actualcalc = Mandelbrot(loc,50)
                turtle.color(actualcalc.get_color())
                turtle.goto(x,y)

    def zoom(self,x,y):
        self.__llbound.setreal(self.__llbound.getreal()/2)
        self.__llbound.setimag(self.__llbound.getimag()/2)
        self.__urbound.setreal(self.__urbound.getreal()/2)
        self.__urbound.setimag(self.__urbound.getimag()/2)
        self.xcen = x
        self.ycen = y
        self.draw(self.xcen,self.ycen)
        #print(self.xcen)
        #print(self.ycen)



    def click(self,x,y):
        #print(x)
        #print(y)
        if(x > -150 and x < 150 and y > -150 and y < 150):
            self.zoom(x,y)



def main():
    test = Display()

if __name__=='__main__':
    main()
