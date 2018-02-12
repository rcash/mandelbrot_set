class Mandelbrot:
    def __init__(self, firstcomplex, maxlen):
        self.__limit = maxlen
        self.__cardinality = 0
        zn = firstcomplex
        for x in range(0,maxlen):
            if (abs(zn)) <= 2:
                self.__cardinality += 1
                zn = zn * zn + firstcomplex
        #13 chosen colors
        self.__colormap = ['#ffffff','#ffcccc','#ff0000','#ff9933','#ffff00','#ccff33','#33cc33','#33cccc','#0066ff','#6f00ff','#808080','#3e3e3e','#000000']
        possible_cardinality_values = []
        possible_cardinality_values.extend(range(0,51))
        #52/13 = 4, groups of 4
        self.__colorchunks = [possible_cardinality_values[i:i + 4] for i in range(0, (len(possible_cardinality_values)), 4)]

    def get_color(self):
        for x in range(0,len(self.__colormap)):
            if self.__cardinality in self.__colorchunks[x]:
                return self.__colormap[x]
