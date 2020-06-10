from app.geolocation import bp
from functools import wraps
from flask import jsonify, request
from pprint import pprint
from app.geolocation.models import geocode as geocode_lookup, get_distance

def map_distances(latitude, longitude, access_point):
  """
  Adds the distance from a given point
  """
  location = access_point.get('location')
  target_latitude = location.get('latitude')
  target_longitude = location.get('longitude')
  distance = get_distance(latitude, longitude, target_latitude, target_longitude)
  access_point['distance'] = distance
  return access_point

@bp.route('/<string:query>')
def geocode(query):
  """ Return the distance between yourself and a target location """
  loc = geocode_lookup(query)
  print(loc)

  latitude = request.args.get('latitude', type=float)
  longitude = request.args.get('longitude', type=float)
  print(latitude, longitude)

  if latitude is None or longitude is None:
    return jsonify({ 'message': 'Missing latitude or longitude parameter' }), 403

  result = (loc.get('results')[0]).get('access_points')
  data = [x for x in map(lambda point: map_distances(latitude, longitude, point), result)]
  return jsonify(status='success', data=data), 200
