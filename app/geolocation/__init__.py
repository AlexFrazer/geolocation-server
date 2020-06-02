from flask import Blueprint

bp = Blueprint('geolocation', __name__)

@bp.record_once
def register(state):
  """ Yes """
  from app.geolocation import routes
  from app.geolocation.commands import cli
  state.app.cli.add_command(cli, 'geolocation')