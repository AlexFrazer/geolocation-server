import pkg_resources
from pprint import pprint
from flask import Flask, jsonify

__version__ = pkg_resources.get_distribution('geolocation').version

def create_app(info = None):
  """ Create a new application context. """
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_object('app.config')
  app.config.from_pyfile('config.py', True)

  from app import geolocation

  app.register_blueprint(geolocation.bp, url_prefix='/api/v1/geolocation')

  @app.errorhandler(404)
  def not_found(e):
    return jsonify({ 'message': 'Not found' }), 404

  return app
