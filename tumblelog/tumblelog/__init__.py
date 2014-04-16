from flask import Flask
from flask.ext.mongoengine import MongoEngine
import hashlib

app = Flask(__name__)

HOST = 'oceanic.mongohq.com'
db_settings = {
    'MONGODB_DB': '<db>',
    'MONGODB_USERNAME': '<user>',
    'MONGODB_PASSWORD': '<pass>',
    'MONGODB_PORT': 10046,
}
app.config = dict(list(app.config.items()) + list(db_settings.items()))
app.config["MONGODB_HOST"] = ('mongodb://%(MONGODB_USERNAME)s:%(MONGODB_PASSWORD)s@'+
                               HOST +':%(MONGODB_PORT)s/%(MONGODB_DB)s') % db_settings
secret_key = hashlib.sha1()
app.config["SECRET_KEY"] = secret_key.digest()

db = MongoEngine(app)


def register_blueprints(app):
    # Prevents circular imports
    from tumblelog.views import posts
    from tumblelog.admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
