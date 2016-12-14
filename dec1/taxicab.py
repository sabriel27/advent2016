import requests

class Point(object):
    # Direction will be represented with integers
    # N = 0, E = 1, S = 2, W = 3
    dir_map = [(0,1), (1,0), (0,-1), (-1,0)]

    def __init__(self, x=0, y=0):
        self.direction = 0
        self.x = x
        self.y = y

    @property
    def distance(self):
        return abs(self.x) + abs(self.y)

    def r_or_l(self, letter):
        return 1 if letter is "R" else -1

    def change_dir(self, letter):
        self.direction = (self.r_or_l(letter) + self.direction) % 4
#        print "direction: %s" % self.direction

    def move(self, distance):
        self.x = self.x + distance * (self.dir_map[self.direction][0])
        self.y = self.y + distance * (self.dir_map[self.direction][1])
#        print self.x, self.y

    def parse(self, dir, distance):
        print dir, distance
        self.change_dir(dir)
        self.move(distance)

    def __str__(self):
        return str(self.distance)

def get_input(url):
    my_account_session = {'session': '53616c7465645f5f0fa6b95cce777a0097c4dc28ab7befa4e78252949c34e0094ea2aef8425e78a86f03affc51482671'}
    response = requests.get(url, cookies=my_account_session)
    data = response.text
    return data

def solve_advent():
    input = get_input('http://adventofcode.com/2016/day/1/input')
    input_list = input.split(', ')
    input_list_1 = ['R2', 'L3']
    input_list_2 = ['R2', 'R2', 'R2']
    input_list_3 = ['R5', 'L5', 'R5', 'R3']
    find_distance(input_list_1)
    find_distance(input_list_2)
    find_distance(input_list_3)

    find_distance(input_list)

def find_distance(list):
    p = Point()
    for dir in list:
       p.parse(dir[0], int(dir[1:]))

    print "final distance %s" % p

if __name__ == '__main__':
    solve_advent()
