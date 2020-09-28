class Pionek:
    def __init__(self,color, size, shape, is_hole):
        self.color = color
        self.size = size
        self.shape = shape
        self.is_hole = is_hole

    def __str__(self):
        return f'color:{self.color}, size:{self.size}, shape: {self.shape}, is hole in pionek: {self.is_hole}'


    def pionek_to_string(self):
        print(str(self.color) + str(self.size) + str(self.shape) + str(self.is_hole))






