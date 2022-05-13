from vector3 import Vector3

class Ray:
    origin, direction = Vector3(), Vector3()

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction