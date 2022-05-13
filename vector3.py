import math

class Vector3:
    x = 0
    y = 0
    z = 0

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, what):
        if isinstance(what, Vector3):
            return Vector3(self.x * what.x, self.y * what.y, self.z * what.z)
        else:
            return Vector3(self.x * what, self.y * what, self.z * what)
    
    def __div__(self, what):
        if isinstance(what, Vector3):
            return Vector3(self.x / what.x, self.y / what.y, self.z / what.z)
        else:
            return Vector3(self.x / what, self.y / what, self.z / what)

    def __add__(self, what):
        if isinstance(what, Vector3):
            return Vector3(self.x + what.x, self.y + what.y, self.z + what.z)
        else:
            return Vector3(self.x + what, self.y + what, self.z + what)
    
    def __sub__(self, what):
        if isinstance(what, Vector3):
            return Vector3(self.x - what.x, self.y - what.y, self.z - what.z)
        else:
            return Vector3(self.x - what, self.y - what, self.z - what)

    def __lt__(self, what):
        if isinstance(what, Vector3):
            return self.x < what.x and self.y < what.y and self.z < what.z
        else:
            return self.x < what and self.y < what and self.z < what
    
    def __gt__(self, what):
        if isinstance(what, Vector3):
            return self.x > what.x and self.y > what.y and self.z > what.z
        else:
            return self.x > what and self.y > what and self.z > what

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalized(self):
        l = self.length()
        v = self
        if l > 0:
            v.x /= l
            v.y /= l
            v.z /= l
        
        return v

    def vector3i(self):
        return Vector3(int(self.x), int(self.y), int(self.z))