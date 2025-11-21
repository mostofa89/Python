class Box:

    def __init__(self, box_info):
        self.height = box_info[0]
        self.width = box_info[1]
        self.breadth = box_info[2]


# Driver code to test the Box class
print('============= Box 1 =============')
box1 = Box([10, 20, 15])
print(f"Height = {box1.height}")
print(f"Width = {box1.width}")
print(f"Breadth = {box1.breadth}")
print(f"Volume = {box1.height * box1.width * box1.breadth}")

print('============= Box 2 =============')
box2 = Box([5, 10, 8])
print(f"Height = {box2.height}")
print(f"Width = {box2.width}")
print(f"Breadth = {box2.breadth}")
print(f"Volume = {box2.height * box2.width * box2.breadth}")

print('============= Box 3 =============')
box3 = Box([12, 7, 9])
print(f"Height = {box3.height}")
print(f"Width = {box3.width}")
print(f"Breadth = {box3.breadth}")
print(f"Volume = {box3.height * box3.width * box3.breadth}")
        