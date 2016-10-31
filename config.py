from app import app
import os


class Config(object):
    '''
    Base Configuration Class
    Contains all Application Constant
    Defaults
    '''
    # Flask Settings
    DEBUG = True
    SECRET_KEY = 'Eg=C}k!5]YG`d{*`#dDZd4=*#'

    # Override FlaskRESTFUL JSON
    RESTFUL_JSON = {"cls": app.json_encoder}

    # Database Settings
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/provision_service'.format(db_user, db_pass, db_host)
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 10
    SQLALCHEMY_POOL_RECYCLE = 500
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class OpcitoConfig(Config):
    '''
    Contains settings and modifications
    for Opcito Development environment
    '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://opcito_user:fr3sca@127.0.0.1/provision_service'
