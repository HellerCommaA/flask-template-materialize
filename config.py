import os
# used to find the base dir for the DB file when running local
basedir = os.path.abspath(os.path.dirname(__file__))

# Secret key for CSRF protection
SECRET_KEY = 'USE-YOUR-OWN-SECRET-KEY-DAMNIT'
# google recaptcha key for no bots!
RECAPTCHA_PUBLIC_KEY = 'TEST'

# AWS RDB instance configs and local DB configs
# SQLALCHEMY_DATABASE_URI = 'mysql://user:PASSWORD@RDS.AWS.COM/mydb'
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')