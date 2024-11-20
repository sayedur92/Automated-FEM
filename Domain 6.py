import numpy as np
import calfem.geometry as cfg
import calfem.mesh as cfm
import calfem.vis_mpl as cfv
import calfem.core as cfc
import calfem.utils as cfu
kx1 = 100
ky1 = 100
t = 1.0
# Gauss points or integration points
n = 2
ep = [t, n]
D = np.matrix([
 [kx1, 0.],
 [0., ky1]
])
g = cfg.Geometry() # Create a GeoData object that holds the geometry.
g.point([0, 0])
g.point([2, 0])
g.point([2, 1])
g.point([0, 1])
g.point([0.5, 0.3])
g.point([0.3, 0.7])
g.point([0.7, 0.7])
g.point([0.8, 0.5])
g.point([1.7, 0.5])
g.point([1.5, 0.5])
g.point([1.7, 0.7])
g.ellipse([7, 8, 9, 10])
g.spline([0, 1])
g.spline([2, 1])
g.spline([3, 2])
g.spline([0, 3])
g.spline([7, 9])
g.spline([10, 9])
g.spline([4, 5, 6, 4])
g.surface([4, 3, 2, 1], [[7], [5, 6, 0]])
mesh = cfm.GmshMesh(g)
mesh.el_type = 16
mesh.dofs_per_node = 1 # Degrees of freedom per node.
mesh.el_size_factor = 0.1 # Factor that changes element sizes.
coords, edof, dofs, bdofs, element_markers = mesh.create()
cfv.figure(fig_size=(10,10))
cfv.draw_geometry(g)
77
cfv.figure(fig_size=(10, 10))
cfv.draw_mesh(
 coords=coords,
 edof=edof,
 dofs_per_node=mesh.dofs_per_node,
 el_type=mesh.el_type,
 filled=True,
 title="Example 01"
)
cfv.showAndWait()