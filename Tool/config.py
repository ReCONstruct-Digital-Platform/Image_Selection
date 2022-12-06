import os
basedir = os.path.abspath(os.path.dirname(__file__))

# The idea is that a value sourced from an environment variable is preferred, but if the environment
# does not define the variable, then the hardcoded string is used instead as a default.
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')

    #disable to send a signal to the application every time a change is about to be made in the database
    SQLALCHEMY_TRACK_MODIFICATIONS = False