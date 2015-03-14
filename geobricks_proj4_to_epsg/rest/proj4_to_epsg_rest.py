import json
from flask import Blueprint
from flask import Response
from flask import request
from flask.ext.cors import cross_origin

from geobricks_proj4_to_epsg.core.proj4_to_epsg import get_epsg_code_from_proj4, get_proj4_json_from_epsg_code

app = Blueprint("convert", "convert")


@app.route('/')
@cross_origin(origins='*')
def root():
    """
    Root REST service.
    @return: Welcome message.
    """
    return 'Welcome to Geobricks PROJ4 to EPSG conversion service!'


@app.route('/discovery/')
@app.route('/discovery')
@cross_origin(origins='*')
def discovery():
    """
    Discovery service available for all Geobricks libraries that describes the plug-in.
    @return: Dictionary containing information about the service.
    """
    out = {
        'name': 'Geocovertion PROJ4 to EPSG',
        'description': 'Functionalities to convert PROJ4 to EPSG codes.',
        'type': 'SERVICE'
    }
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')


@app.route('/proj4/<proj4_text>/epsg/', methods=['GET'])
@app.route('/proj4/<proj4_text>/epsg', methods=['GET'])
@cross_origin(origins='*', headers=['Content-Type'])
def get_epsg_code_rest(proj4_text):
    try:
        result = get_epsg_code_from_proj4(proj4_text)
        return Response(json.dumps({"epsg": result}), content_type='application/json; charset=utf-8')
    except Exception, e:
        raise Exception(e)


@app.route('/epsg/<epsg>/proj4/', methods=['GET'])
@app.route('/epsg/<epsg>/proj4', methods=['GET'])
@cross_origin(origins='*', headers=['Content-Type'])
def get_proj4_json_rest(epsg):
    try:
        result = get_proj4_json_from_epsg_code(epsg)
        return Response(json.dumps(result), content_type='application/json; charset=utf-8')
    except Exception, e:
        raise Exception(e)


@app.route('/proj4json/<proj4>/epsg/', methods=['GET'])
@app.route('/proj4json/<proj4>/epsg', methods=['GET'])
@cross_origin(origins='*', headers=['Content-Type'])
def get_epsg_from_proj4json_rest(proj4):
    try:
        print proj4
        result = get_epsg_code_from_proj4(json.loads(proj4))
        return Response(json.dumps({"epsg": result}), content_type='application/json; charset=utf-8')
    except Exception, e:
        raise Exception(e)