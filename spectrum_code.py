import astropy
import astropy.coordinates
import astropy.units as u
import datetime

def alt_az_to_galactic(alt, az, lat, lon, height, time):
	time = astropy.time.Time(time, format='datetime')
	location = astropy.coordinates.EarthLocation(lat=lat*u.deg, lon=lon*u.deg, height=height*u.m)
	c = astropy.coordinates.SkyCoord(alt=alt*u.deg, az=az*u.deg, obstime=time, location=location, frame='altaz')
	print(c.galactic)

time = datetime.datetime(2018, 5, 20, 3, 45, 15)
lat = 41.3
lon = -74
alt = 60.0
height = 100
az = 1.0
alt_az_to_galactic(alt, az, lat, lon, height, time)

