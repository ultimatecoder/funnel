from . import app
import requests
from urlparse import urljoin
from baseframe import cache


@cache.memoize(timeout=86400)
def geonameid_from_location(text):
    """ Accepts a string, checks hascore if there's a location embedded
        in the string, and returns the geonameid for a location found.
        Eg: "Bangalore" -> 1277333
        To detect multiple locations, split them up and pass each location individually
    """
    if 'HASCORE_SERVER' in app.config:
        url = urljoin(app.config['HASCORE_SERVER'], '/1/geo/parse_locations')
        response = requests.get(url, params={'q': text}).json()
        return [field['geoname']['geonameid'] for field in response['result'] if 'geoname' in field.keys()][0]
    return None
