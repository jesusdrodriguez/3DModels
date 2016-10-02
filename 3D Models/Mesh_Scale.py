import Mesh
mesh = Mesh.Mesh()
mesh.read('path')
Mesh.show(mesh)
mat=FreeCAD.Matrix()
mat.A11=.1
mat.A22=.1
mat.A33=.1
mesh.transform(mat)
Mesh.show(mesh)
mesh.write('path')