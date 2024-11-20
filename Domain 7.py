import calfem.geometry as cfg
import calfem.mesh as cfm
import calfem.vis as cfv
g = cfg.Geometry()
g.point([0.0, 0.0]) # point 0
g.point([5.0, 0.0]) # point 1
g.point([2.5, 4.0]) # point 2
g.spline([0, 1]) # line 0
g.spline([1, 2]) # line 1
g.spline([2, 0]) # line 2
g.surface([0, 1, 2])
cfv.drawGeometry(g)
cfv.showAndWait()
mesh = cfm.GmshMesh(g)
mesh.elType = 3 # Degrees of freedom per node.
mesh.dofsPerNode = 1 # Factor that changes element sizes.
mesh.elSizeFactor = .25 # Element size Factor
coords, edof, dofs, bdofs, elementmarkers = mesh.create()
cfv.figure()
# Draw the mesh.
cfv.drawMesh(
 coords=coords,
 edof=edof,
 dofs_per_node=mesh.dofsPerNode,
 el_type=mesh.elType,
 filled=True,
 title="Example 01"
 )
cfv.showAndWait()
