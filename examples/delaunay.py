from geoplotlib.layers import DelaunayLayer
import geoplotlib
from geoplotlib.utils import read_csv, BoundingBox


data = read_csv('/Users/ancu/Dropbox/phd/code-projects/geoplotlib/examples/data/bus.csv')
geoplotlib.add_layer(DelaunayLayer(data, cmap='hot_r'))
geoplotlib.set_bbox(BoundingBox.DK)
geoplotlib.set_smoothing(True)
geoplotlib.show()