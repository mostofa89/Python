import math
class Sphere:

    def __init__(self, id, redius = 1, color = "White"):
        self.id = id
        self.redius = redius
        self.color = color
        self.volume = math.pi * (self.redius ** 3) * (4 / 3)


    def printDetails(self):
        print(f"""Sphere ID: {self.id}
Color: {self.color}
Volume: {self.volume : .2f}""")
        

    def merge_sphere(self, *spheres):
        total_volume = self.volume
        for sphere in spheres:
            total_volume += sphere.volume
            if sphere.color != self.color:
                self.color = "MixedColor"

        self.volume = total_volume
        print("Spheres are being merged")



if __name__ == "__main__":
    sphere1 = Sphere("Sphere 1")
    print("1***************")
    sphere1.printDetails()
    print("2***************")
    sphere2 = Sphere("Sphere 2", 3)
    print("3***************")
    sphere2.printDetails()
    print("4***************")
    sphere3 = Sphere("Sphere 3", 2)
    print("5***************")
    sphere3.printDetails()
    print("6***************")
    sphere3.merge_sphere(sphere1,sphere2)
    print("7***************")
    sphere3.printDetails()
    print("8***************")
    sphere4 = Sphere("Sphere 4", 5, "Purple")
    print("9***************")
    sphere4.merge_sphere(sphere3)
    print("10***************")
    sphere4.printDetails()


        
