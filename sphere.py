from vector3 import Vector3
import math

def dot(a: Vector3, b: Vector3):
    return (a.x * b.x + a.y * b.y + a.z * b.z)

class Sphere:
    center = Vector3()
    radius = 0

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
    def get_normal(self, pi):
        return (pi  - self.center)
    
    def intersect(self, ray, t):
        o = ray.origin
        d = ray.direction
        oc = (o - self.center)
        b = 2 * dot(oc, d)
        c = dot(oc, oc) - self.radius * self.radius
        disc = b * b - 4 * c
        if (disc < 1e-4): return False
        disc = math.sqrt(disc)
        t0 = -b - disc
        t1 = -b + disc
        t = (t0 < t1) if t0 else t1
        return t

