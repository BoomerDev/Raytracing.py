from vector3 import Vector3
from sphere import Sphere
from ray import Ray

from PIL import Image

def dot(a: Vector3, b: Vector3):
    return (a.x * b.x + a.y * b.y + a.z * b.z)

def clamp255(x):
    if x < 0: return 0
    if x > 255: return 255
    return x

if __name__ == '__main__':
    img = Image.new('RGB', (200,200), "black")
    

    w,h = 200,200

    white = Vector3(255, 255, 255)
    black = Vector3(0, 0, 0)
    red   = Vector3(255, 0, 0)

    sphere = Sphere(Vector3(w * 0.5, h * 0.5, 50), 50)
    light = Sphere(Vector3(0, 0, 50), 2)

    t = 0
    pix_col = red

    # Setup Bitmap
    pixels = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):

            pix_col = red

            ray = Ray(Vector3(x,y,0), Vector3(0,0,1))

            t = sphere.intersect(ray, t)

            if t:
                pi = ray.origin + (ray.direction * t)
                Light = (light.center - pi)
                Normal = sphere.get_normal(pi)
                dt = dot(Light.normalized(), Normal.normalized())

                pix_col = (red + (white * dt)).vector3i()
                pix_col = clamp255(pix_col)

                pixels[x,y] = (pix_col.x, pix_col.y, pix_col.z)
            
            y +=  1
        x += 1

    
    img.save("render.bmp")
