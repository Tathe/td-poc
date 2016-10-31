from flask import Flask
from flask_restful import Resource, Api
import os
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')
settings_map = {
    'development': 'config.DevelopmentConfig',
    'testing': 'config.TestingConfig',
    'opcito': 'config.OpcitoConfig',
    'production': 'config.ProductionConfig',
}

config_name = os.getenv('FLASK_CONFIGURATION', 'opcito')
app.config.from_object(settings_map[config_name])

api = Api(app)
CORS(app)
db = SQLAlchemy(app)

# Used for App db migrations and upgrades
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
