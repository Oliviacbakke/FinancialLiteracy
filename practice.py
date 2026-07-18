class Point():
    def init (self, x, y):
        self.x = 0
        self.y = 0
    def add_vals(self):
        res = self.x + self.y
        return res
p = Point()
p.x = 1
print(p.x)
