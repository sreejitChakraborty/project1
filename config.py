# set your app config here

class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'hlky288dnp10eskj'
    # FLASK_HTPASSWD_PATH = '/secret/.htpasswd'

    STATIC_FOLDER = 'static',
    TEMPLATE_FOLDER = 'templates'
    FLASK_SECRET = SECRET_KEY


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    SECRET_KEY = 'hlky288dnp10eskj'
   
    FLASK_SECRET = SECRET_KEY
    STATIC_FOLDER = 'static',
    TEMPLATE_FOLDER = 'templates'
