from . import settings

# Initialize Flask app
from flask import Flask

app = Flask('ggrc', instance_relative_config=True)
app.config.from_object(settings)

# Configure Flask-SQLAlchemy for app
from . import db
db.app = app
db.init_app(app)

# Configure webassets for app
#from . import assets
#app.jinja_env.add_extension('webassets.ext.jinja2.AssetsExtension')
#app.jinja_env.assets_environment = assets.environment

# Configure Jinja2 extensions for app
#app.jinja_env.add_extension('jinja2.ext.autoescape')
#app.jinja_env.add_extension('jinja2.ext.with_')
#app.jinja_env.add_extension('jinja2_hamlpy.HamlPyExtension')

# Initialize services
from .services import init_all_services
init_all_services(app)

# Initialize views
#import ggrc.views