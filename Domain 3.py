import calfem.core as cfc
import calfem.geometry as cfg
import calfem.mesh as cfm
import calfem.vis as cfv
import calfem.utils as cfu
g = cfg.Geometry()
g.point([0.0, 0.0]) # point 0
g.point([40.0, 0.0]) # point 1
g.point([40.0, 24.0]) # point 2
g.point([0.0, 24.0]) # point 3
g.point([14.0, 8.0]) # point 4
g.point([26.0, 8.0]) # point 5
g.point([26.0, 16.0]) # point 6
g.point([14.0, 16.0]) # point 7
g.spline([0, 1]) # line 0
g.spline([1, 2]) # line 1
g.spline([2, 3]) # line 2
g.spline([3, 0]) # line 3
g.spline([4, 5]) # line 4
g.spline([5, 6]) # line 5
g.spline([6, 7]) # line 6
g.spline([7, 4]) # line 7
g.surface([0, 1, 2, 3], [[4, 5, 6, 7]])
cfv.drawGeometry(g)
cfv.showAndWait()
mesh = cfm.GmshMesh(g)
mesh.elType = 3 # Degrees of freedom per node.
mesh.dofsPerNode = 1 # Factor that changes element sizes.
mesh.elSizeFactor = 4 # Element size Factor
coords, edof, dofs, bdofs, elementmarkers = mesh.create()
cfv.figure()
# Draw the mesh.
cfv.drawMesh(
 coords=coords,
 edof=edof,
 dofs_per_node=mesh.dofsPerNode,
 el_type=mesh.elType,
 filled=True,
 title="Example 03"
 )
cfv.showAndWait()
