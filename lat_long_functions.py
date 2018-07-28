import numpy as np

EARTH_RAD = 6371000.0 # meters
DELTA_LON = 0.01745329251  # 1 degree in radians
RAD_TO_DEGREES = 57.2957795131  # 1 radian to degrees

def haversine(lat1, lon1, lat2, lon2):
    R = EARTH_RAD 
    dLat = np.radians(lat2 - lat1)
    dLon = np.radians(lon2 - lon1)
    lat1 = np.radians(lat1)
    lat2 = np.radians(lat2)

    a = np.sin(dLat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dLon/2)**2
    c = 2*np.arcsin(np.sqrt(a))
    return R * c


def dist_from_lat_lng(lat, lng, dist, bearing):
    """
    :param lat: (float) decimal latittude
    :param lng: (float) decimal longitude
    :param dist: (float) distance (m)
    :param bearing: (float) heading in radians, counter clockwise relative to north

                     N (0)
                      ^
                      |
          W (pi/2) <--+--> E (0,3pi/2)
                      |
                      V
                    S (pi) 

    :rtype: np.array([float, float])

    Given a latittude and longitude (lat, lng), we calculate width and height
    of a square of dimension dist around the point. We then return the number
    of degrees lattitude and longitude respectively associated with the width
    and height of the square patch as a tuple.
    """
    # here, d is measured in 'radians of arc', we convert dist from meters to d
    # using basic geometry (arc_length = radius * arc_angle).
    d = dist / EARTH_RAD 

    lat = np.radians(lat)
    lng = np.radians(lng)

    res_lat = np.arcsin(np.sin(lat)*np.cos(d)+np.cos(lat)*np.sin(d)*np.cos(bearing))
    dlng = np.arctan2(np.sin(bearing)*np.sin(d)*np.cos(lat),np.cos(d)-np.sin(lat)*np.sin(lat))
    res_lng = (lng-dlng+np.pi)%(2*np.pi) - np.pi

    lat_deg = np.degrees(res_lat)
    lng_deg = np.degrees(res_lng)
    return np.array([lat_deg, lng_deg])

if __name__ == '__main__':
    print(haversine(0.0,0.0,0.1,0.0))
    print(haversine(89.9,0.0,90.0,0.0))
