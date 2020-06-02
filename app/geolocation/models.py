import os
import requests
import math

# Estimated radius of earth in metres
radius = 6371e3

def geocode(query, format='json'):
  """ Geocode a specific location """
  payload = {
    'key': os.environ.get('API_KEY'),
    'address': query
  }
  response = requests.get('https://maps.googleapis.com/maps/api/geocode/{format}'.format(format=format), params=payload)
  return response.json()


def reverse_geocode():
  """ Reverse geocodes a location """

def square_sine(x):
  return math.sin(x / 2) ** 2

def get_distance(lat_a, long_a, lat_b, long_b):
  """
  Returns the distance, in meters, between two points
  Uses the haversine formula, i.e.:
    a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
    c = 2 ⋅ atan2( √a, √(1−a) )
    d = R ⋅ c
  Keep in mind this is an "as the crow flies" type of estimation

  Parameters:
    - lat_a: latitude of first point
    - long_a: longitude of second point
    - lat_b: latitude of second point
    - long_b: longitude of second point

  Returns
    A number representing the distance in kilometres
  """
  phi1 = math.radians(lat_a)
  phi2 = math.radians(lat_b)

  delta_phi = phi2 - phi1 
  delta_lamba = math.radians(long_b - long_a)

  # sin²(Δφ/2)
  phi_distance = math.sin(delta_phi / 2) ** 2
  # sin²(Δλ/2)
  delta_distance = math.sin(delta_lamba / 2) ** 2
  # cos φ1 ⋅ cos φ2
  point_cos = math.cos(phi1) * math.cos(phi2)

  # sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
  a = phi_distance + point_cos * delta_distance

  # c = 2 ⋅ atan2( √a, √(1−a) )
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

  return radius * c
