import os


class DevelopConfig(object):
    DEBUG = True
    pguser = os.environ.get('PGUSER', 'postgres')
    pgpass = os.environ.get('PGPASSWORD', 'postgres')
    pghost = os.environ.get('PGHOST', 'db')
    pgport = os.environ.get('PGPORT', '5432')
    pgdb = os.environ.get('PGDATABASE', 'basic_data')
    SQLALCHEMY_DATABASE_URI = f'postgres://{pguser}:{pgpass}@{pghost}:{pgport}/{pgdb}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

