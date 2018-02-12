class Complex:
    #init to 0 if none passed in
    def __init__(self, real = 0, imag = 0):
        self.__real = real
        self.__imag = imag
    #should be unambiguous
    def __repr__(self):
        if self.__imag == 0:
            return '%.1f' % self.__real
        elif self.__real == 0:
            return '%.1f' % self.__imag
        elif self.__imag < 0:
            stringImaginary = str(self.__imag)
            positive_imaginary = imaginary_string[1:]
            return '%.1f - %.1fi' % (self.__real, positive_imaginary)
        else:
            return '%.1f + %.1fi' % (self.__real, self.__imag)
    #accessors
    def getreal(self):
        return self.__real

    def getimag(self):
        return self.__imag

    #mutators
    def setreal(self, real):
        self.__real = real

    def setimag(self, imag):
        self.__imag = imag

    #add the real parts (k + m) and imaginary (l + n)io
    def __add__(self, rhand):
        k = self.__real
        m = rhand.__real
        l = self.__imag
        n = rhand.__imag
        return Complex(k + m, l + n)

    #cross multiply
    def __mul__(self, rhand):
        rpart = self.__real * rhand.__real - self.__imag * rhand.__imag
        ipart = self.__real * rhand.__imag + self.__imag * rhand.__real
        return Complex(rpart, ipart)

    def __abs__(self):
        #Pythagorean theorem since it's distance from origin:
        #a^2 + b^2 = c^2, solved for c
        return float(self.__real**2 + self.__imag**2)**(1/2)
