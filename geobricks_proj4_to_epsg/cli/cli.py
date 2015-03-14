import json
from argh import dispatch_commands
from argh.decorators import named
from geobricks_proj4_to_epsg.core.proj4_to_epsg import get_epsg_code_from_proj4, get_proj4_json_from_epsg_code
from geobricks_proj4_to_epsg.rest import proj4_to_epsg_main


@named('proj4')
def get_epsg_code(proj4_string):
    print get_epsg_code_from_proj4(proj4_string)

@named('epsg')
def get_proj4_json(epsg_code):
    print json.dumps(get_proj4_json_from_epsg_code(epsg_code))

@named('rest')
def rest_engine(opt):
    if opt == "start":
        proj4_to_epsg_main.start()


def main():
    dispatch_commands([get_epsg_code, get_proj4_json, rest_engine])

if __name__ == '__main__':
    main()