''' Table for Toy Robot Simulator
Carl Pickering 16th November 2025'''


class Table:
    '''Provides table for Robot to run on'''
    def __init__(self, eastwest, northsouth):
        if eastwest<1 or northsouth<1:
            raise ValueError("Table size out of range")
        self.x_max = eastwest-1
        self.y_max = northsouth-1

    def get_x_max(self):
        return self.x_max

    def get_y_max(self):
        return self.y_max

    def is_valid_position(self, x,y):
        if x<0:
            return False
        if x>self.x_max:
            return False
        if y<0:
            return False
        if y>self.y_max:
            return False
        return True


if __name__=='__main__':
    print("Check Table")
    try:
        not_table = Table(0,1)
    except ValueError as e:
        print("Error received:", e)

    proper_table = Table(4,4)
    print("Is valid 4,8=", proper_table.is_valid_position(4,8))