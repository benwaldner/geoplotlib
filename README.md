# Personal notes

Examples: https://medium.com/@labdheesheth/visualizing-geographical-data-using-geoplotlib-d732953abcd5

![image](https://user-images.githubusercontent.com/35944883/179499090-73311840-ede9-479d-8ce0-975da581a083.png)

Geospital
![image](https://user-images.githubusercontent.com/35944883/179499213-2fb6f095-d194-40a3-9fa0-541859a4e963.png)



geoplotlib is a python toolbox for visualizing geographical data and making maps

```python
data = read_csv('data/bus.csv')
geoplotlib.dot(data)
geoplotlib.show()
```

This will launch the geoplotlib window and plot the points on OpenStreetMap tiles, also allowing zooming and panning. geoplotlib automatically handles the data loading, the map projection, downloading the map tiles and the graphics rendering with OpenGL.

Examples source code is [here](https://github.com/andrea-cuttone/geoplotlib/tree/master/examples)

# Installation

geoplotlib requires:
* [numpy](http://www.numpy.org/)
* [pyglet 1.2.4](https://bitbucket.org/pyglet/pyglet/wiki/Download)
	* **note:** in order for pyglet to work with ipython on Mac, version 1.2.4 or newer is needed

optional requirements:
* [matplotlib](http://matplotlib.org/) for colormaps
* [scipy](http://www.scipy.org) for some layers
* [pyshp](https://github.com/GeospatialPython/pyshp) for reading .shp files

to install from source run:

```python setup.py install```

or with pip:

```pip install geoplotlib```

# User Guide
A detailed user guide can be found in the [wiki](https://github.com/andrea-cuttone/geoplotlib/wiki/User-Guide)
