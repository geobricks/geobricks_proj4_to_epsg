from flask import Flask
from flask.ext.cors import CORS
from geobricks_proj4_to_epsg.config.config import config
from geobricks_proj4_to_epsg.rest import proj4_to_epsg_rest as rest
import logging

# Initialize the Flask app
app = Flask(__name__)

def start():

    # Initialize CORS filters
    cors = CORS(app, resources={r'/*': {'origins': '*'}})

    # Url blueprint prefix
    url_prefix = "/geoconvert"

    # Core services.
    app.register_blueprint(rest.app, url_prefix=url_prefix)

    # Logging level.
    # log = logging.getLogger('werkzeug')
    # log.setLevel(logging.INFO)
    app.run(host=config['settings']['host'], port=config['settings']['port'], debug=config['settings']['debug'], threaded=True)


# Start Flask server
if __name__ == '__main__':
    start()
