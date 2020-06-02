import click
import requests
import os
from flask import current_app
from flask.cli import AppGroup
from pprint import pprint
from app.geolocation.models import geocode as geocode_lookup

@click.command(cls=AppGroup)
def cli():
  """ Manage geolocation """

@cli.command()
@click.argument('query')
def geocode(query):
  """ Geocodes a location """
  result = geocode_lookup(query)
  pprint(result)
