import numpy as np
import calfem.geometry as cfg
import calfem.mesh as cfm
import calfem.vis_mpl as cfv
import calfem.core as cfc
import calfem.utils as cfu
a = 10.0
b = 4.0
g = cfg.Geometry()
g.point([a, 0.0]) # point 0
g.point([0.0, a]) # point 1
g.point([-a, 0.0]) # point 2
g.point([0.0, -a]) # point 3
g.point([0.0, 0.0]) # point 4
g.point([b, 0.0]) # point 5
g.point([0.0, b]) # point 6
g.point([-b, 0.0]) # point 7
g.point([0.0, -b]) # point 8
g.circle([0, 4, 1]) # line 0
g.circle([1, 4, 2]) # line 1
g.circle([2, 4, 3]) # line 2
g.circle([3, 4, 0]) # line 3
g.circle([5, 4, 6]) # line 4
g.circle([6, 4, 7]) # line 5
g.circle([7, 4, 8]) # line 6
g.circle([8, 4, 5]) # line 7
g.surface([0, 1, 2, 3], [[4, 5, 6, 7]])
mesh = cfm.GmshMesh(g)
mesh.elType = 16 # Degrees of freedom per node.
mesh.dofsPerNode = 1 # Factor that changes element sizes.
mesh.elSizeFactor = 1 # Element size Factor
coords, edof, dofs, bdofs, elementmarkers = mesh.create()
cfv.figure(fig_size=(10, 10))
cfv.draw_geometry(g)
cfv.figure(fig_size=(10, 10))
# Draw the mesh.
cfv.draw_mesh(
 coords=coords,
 edof=edof,
 dofs_per_node=mesh.dofsPerNode,
 el_type=mesh.elType,
 filled=True,
 title="Example 05"
 )
cfv.showAndWait()
