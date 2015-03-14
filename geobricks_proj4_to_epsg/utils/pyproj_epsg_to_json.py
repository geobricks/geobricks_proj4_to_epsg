import requests
import json
from geobricks_proj4_to_epsg.core.proj4_to_epsg import get_proj4_json_from_string

# dirty methods to get epsg/proj4 codes


def clean_pyproj_file():
    epsg_json = []
    with open("../data/pyproj/epsg", "r") as f:
        for row in f.readlines():
            if "#" not in row:
                row = row.replace('<>\n', '').strip()
                values = row.split(" ")
                # print values
                epsg_code = get_epsg_code(values[0])
                proj4_json = get_proj4_json_from_string(row.replace("<" + str(epsg_code) + "> ", ""))
                epsg_json.append({
                    "epsg": str(epsg_code),
                    "proj4": proj4_json
                })
    write_json_file(epsg_json)

def get_epsg_code(v):
    return v[1:len(v)-1]

def write_json_file(json_data):
    with open('../data/epsg.json', 'w') as outfile:
        print "wrinting file"
        # print json_data
        json.dump(json_data, outfile)



clean_pyproj_file()