import calfem.core as cfc
import calfem.geometry as cfg
import calfem.mesh as cfm
import calfem.vis as cfv
import calfem.utils as cfu
a = 20
b = 15
g = cfg.Geometry()
g.point([0.0, 0.0]) # point 0
g.point([a, 0.0]) # point 1
g.point([a, b]) # point 2
g.point([0, b]) # point 3
g.spline([0, 1]) # line 0
g.spline([1, 2]) # line 1
g.spline([2, 3]) # line 2
g.spline([3, 0]) # line 3
g.surface([0, 1, 2, 3])
cfv.drawGeometry(g)
cfv.showAndWait()
mesh = cfm.GmshMesh(g)
mesh.elType = 3 # Degrees of freedom per node.
mesh.dofsPerNode = 1 # Factor that changes element sizes.
mesh.elSizeFactor = 1 # Element size Factor
coords, edof, dofs, bdofs, elementmarkers = mesh.create()
cfv.figure()
# Draw the mesh.
cfv.drawMesh(
 coords=coords,
 edof=edof,
 dofs_per_node=mesh.dofsPerNode,
 el_type=mesh.elType,
 filled=True,
 title="Example 02"
 )
cfv.showAndWait()
