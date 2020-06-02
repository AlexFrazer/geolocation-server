import sys
from flask.cli import FlaskGroup
from app import create_app

cli = FlaskGroup(create_app=create_app)

def main():
  args = sys.argv[1:]
  cli.main(args=args, prog_name=None)

if __name__ == '__main__':
  main()