import astropy
import astropy.coordinates
import astropy.units as u
import datetime
import matplotlib 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def alt_az_to_galactic(alt, az, lat, lon, height, time):
	time = astropy.time.Time(time, format='datetime')
	location = astropy.coordinates.EarthLocation(lat=lat*u.deg, lon=lon*u.deg, height=height*u.m)
	c = astropy.coordinates.SkyCoord(alt=alt*u.deg, az=az*u.deg, obstime=time, location=location, frame='altaz')
	return c.galactic


mean_spec = np.random.uniform(-24, 16.0, (5, 5))
def plot_waterfall(mean_spec):
    fig = plt.figure()
    plt.imshow(mean_spec,aspect='auto',extent=(1180,1300,12,0),vmax=-16,interpolation='nearest')
    plt.colorbar()
    plt.xlabel('MHz')
    plt.ylabel('Hrs')
    plt.show()
plot_waterfall(mean_spec)

times = astropy.time.Time([2458437.71806, 2458438.71806, 2458439.71806, 2458440.71806, 2458441.71806], scale='utc', format='jd')
h1 = [18, 19, 20, 24, 17]

def plot_h1_vs_time(times, h1):
    fig = plt.figure()
    plt.scatter(times.value, h1)
    plt.xlabel('Date (JD)')
    plt.ylabel('H1 Line (cm)')
    plt.ylim((17, 25))
    plt.xticks(rotation=-45)
    plt.tight_layout()
    ax = plt.gca()
    ax.get_xaxis().get_major_formatter().set_useOffset(False)
    plt.show()
plot_h1_vs_time(times, h1)


time = datetime.datetime(2018, 5, 20, 3, 45, 15)
lats = [10, 20, 30, 40, 50]
lons = [-10, -20, -30, -40, -50]
alts = [50, 55, 60, 65, 70]
heights = [100, 200, 300, 400, 500]
azs = [0.1, 0.2, 0.3, 0.4, 0.5]
coords = []
coords2 = []
for x in range(len(lats)):
	coords.append(alt_az_to_galactic(alts[x], azs[x], lats[x], lons[x], heights[x], time))


def plot_h1_vs_coords(coords, h1):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ls = []
	bs = []
	for x in range(len(coords)):
		ls.append(coords[x].data.lon.value)
		bs.append(coords[x].data.lat.value)
	ax.scatter(ls, bs, h1)
	ax.set_xlabel('Galactic Longitude (Radians)')
	ax.set_ylabel('Galactic Latatiude (Radians)')
	ax.set_zlabel('H1 Line (cm)')
	ax.set_zlim(17, 25)
	plt.show()
plot_h1_vs_coords(coords, h1)