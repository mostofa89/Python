class Vector3D:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    print(f'Vector <{self.x}, {self.y}, {self.z}> has been created.')


# Driver code to test the Vector3D class
v1 = Vector3D(2, -3, 1)
v2 = Vector3D(-1, 4, 0)
print("Magnitude of the first vector= "+str((v1.x**2 + v1.y**2 + v1.z**2)**.5))
print("Magnitude of the second vector = "+str((v2.x**2 + v2.y**2 + v2.z**2)**.5))
print("Dot product of the two vectors = "+str((v1.x*v2.x + v2.y*v1.y + v2.z*v1.z)))
print("Vector <"+str(v1.y*v2.z - v2.y*v1.z)+", "+str(v1.x*v2.z - v1.z*v2.x)+", "+str(v1.x*v2.y - v1.y*v2.x)+" >has been created.")
print("Cross product of the two vectors =")