class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value

    @property
    def heigth(self):
        return self._heigth

    @heigth.setter
    def heigth(self,value):
        self._heigth = value

    @property
    def resolution(self):
        return self._width*self._heigth


s = Screen()
s.heigth = 768
s.width = 1024
print(s.resolution)
assert s.resolution == 786432, '1024*768 =%d ?' % s.resolution