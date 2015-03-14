import json
from argh import dispatch_commands
from argh.decorators import named
from geobricks_proj4_to_epsg.core.proj4_to_epsg import get_epsg_code_from_proj4, get_proj4_json_from_epsg_code


@named('proj4')
def get_epsg_code(proj4_string):
    print get_epsg_code_from_proj4(proj4_string)

@named('epsg')
def get_proj4_json(epsg_code):
    print json.dumps(get_proj4_json_from_epsg_code(epsg_code))


# @named('rest')
# def get_proj4_json(type):
#     print type


def main():
    dispatch_commands([get_epsg_code, get_proj4_json])

if __name__ == '__main__':
    main()